"""
AI-Powered Chatbot for University Student Support - FastAPI backend.

Run:  uvicorn app.main:app --reload
"""
import os
import re
from pathlib import Path

import joblib
import numpy as np
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

from app.faq import FAQS

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "priority_model.joblib"
STATIC_DIR = BASE_DIR / "static"

GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", "0.35"))

# ---------------------------------------------------------------- load once
priority_model = joblib.load(MODEL_PATH)
embedder = SentenceTransformer("all-MiniLM-L6-v2")
faq_embeddings = embedder.encode(
    [q for _, q, _ in FAQS], normalize_embeddings=True
)  # normalized -> dot product == cosine similarity

gemini_client = None
if os.getenv("GEMINI_API_KEY"):
    try:
        from google import genai

        gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    except Exception as exc:  # SDK missing or bad key -> fallback mode
        print("Gemini disabled:", exc)

app = FastAPI(title="University Student Support Chatbot")


# ---------------------------------------------------------------- helpers
def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", str(text).lower()).strip()


def predict_priority(cleaned: str) -> str:
    return str(priority_model.predict([cleaned])[0])


def retrieve_faq(cleaned: str):
    q_emb = embedder.encode([cleaned], normalize_embeddings=True)[0]
    scores = faq_embeddings @ q_emb
    idx = int(np.argmax(scores))
    category, question, answer = FAQS[idx]
    return category, question, answer, float(scores[idx])


def generate_answer(query: str, priority: str, category: str, faq_q: str, faq_a: str) -> tuple[str, str]:
    """Returns (answer, source) where source is 'gemini' or 'faq'."""
    if gemini_client is None:
        return faq_a, "faq"
    prompt = (
        "You are a helpful university student-support assistant.\n"
        "Answer the student's query using ONLY the FAQ information given below. "
        "Do not invent any university policy, date, fee or phone number. "
        "Be short, polite and clear (max 4 sentences). "
        "If the priority is High, tell the student to contact the concerned office immediately.\n\n"
        f"Student query: {query}\n"
        f"Priority: {priority}\n"
        f"Category: {category}\n"
        f"Matched FAQ question: {faq_q}\n"
        f"FAQ answer: {faq_a}\n"
    )
    try:
        resp = gemini_client.models.generate_content(model=GEMINI_MODEL, contents=prompt)
        text = (resp.text or "").strip()
        if text:
            return text, "gemini"
    except Exception as exc:
        print("Gemini call failed, using FAQ fallback:", exc)
    return faq_a, "faq"


# ---------------------------------------------------------------- API
class ChatRequest(BaseModel):
    message: str


@app.get("/status")
def status():
    """FR-10: confirms the backend is running."""
    return {"status": "running", "gemini_enabled": gemini_client is not None}


@app.post("/chat")
def chat(req: ChatRequest):
    query = req.message.strip()
    if not query:
        return {"query": query, "answer": "Please type your question.", "priority": None,
                "department": None, "similarity": 0.0, "matched_faq": None, "source": "none"}

    cleaned = clean_text(query)
    priority = predict_priority(cleaned)
    category, faq_q, faq_a, score = retrieve_faq(cleaned)

    # Similarity threshold: off-topic queries get a polite "not available" reply
    if score < SIMILARITY_THRESHOLD:
        return {
            "query": query,
            "priority": priority,
            "department": None,
            "similarity": round(score, 2),
            "matched_faq": None,
            "answer": "Sorry, I could not find this information in the university FAQ. "
                      "Please contact the concerned office or the student help desk.",
            "source": "not_found",
        }

    answer, source = generate_answer(query, priority, category, faq_q, faq_a)
    return {
        "query": query,
        "priority": priority,
        "department": category,
        "similarity": round(score, 2),
        "matched_faq": faq_q,
        "answer": answer,
        "source": source,
    }


# ---------------------------------------------------------------- frontend
@app.get("/")
def home():
    """Serves the chat page (status check is available at GET /status)."""
    return FileResponse(STATIC_DIR / "index.html")


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
