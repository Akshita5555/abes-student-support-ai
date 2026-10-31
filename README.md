# AI-Powered Chatbot for University Student Support

Student: Akshita Chaudhary | Roll No: 2400320100144 | ABES Engineering College | Guide: Shoeb Khan

## Project structure
```
app/main.py              FastAPI backend (GET /, GET /status, POST /chat)
app/faq.py               FAQ knowledge base (25 entries)
static/index.html        Chat page (HTML/CSS/JS)
generate_dataset.py      Creates train (5000) / test (1000) CSV files in data/
train_priority.py        TF-IDF + Logistic Regression priority model
models/                  Saved model + confusion matrix
```

## How to run (local)
```bash
python -m venv venv
venv\Scripts\activate            # Windows   (Linux/Mac: source venv/bin/activate)
pip install -r requirements.txt

copy .env.example .env           # then paste your Gemini API key in .env (optional)

python generate_dataset.py       # skip if you already have your own CSV files in data/
python train_priority.py
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000 in the browser.

* No Gemini key? The chatbot still works - it returns the stored FAQ answer (fallback).
* Get a free Gemini key at https://aistudio.google.com/apikey

## API
* `GET /status` -> `{"status": "running", ...}`
* `POST /chat` with `{"message": "..."}` -> query, priority, department, similarity, matched_faq, answer, source

## Notes
* Similarity threshold (default 0.35, env `SIMILARITY_THRESHOLD`): below it the bot says the information is not available.
* If you have your original `university_query_train.csv` / `university_query_test.csv`, put them in `data/` and re-run `train_priority.py`.
