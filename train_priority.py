"""Train TF-IDF + Logistic Regression priority model and save it to models/priority_model.joblib."""
import re, joblib
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def clean_text(t: str) -> str:
    return re.sub(r"\s+", " ", str(t).lower()).strip()

train = pd.read_csv("data/university_query_train.csv")
test = pd.read_csv("data/university_query_test.csv")
for d in (train, test):
    print("missing:", int(d.isna().sum().sum()), "| duplicates:", int(d.duplicated().sum()))

X_tr = train["Student_Query"].map(clean_text); y_tr = train["Priority_Label"]
X_te = test["Student_Query"].map(clean_text);  y_te = test["Priority_Label"]

pipe = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
    ("clf", LogisticRegression(max_iter=1000)),
])
pipe.fit(X_tr, y_tr)
pred = pipe.predict(X_te)

print("Accuracy:", round(accuracy_score(y_te, pred), 4))
print(classification_report(y_te, pred))
labels = ["High", "Medium", "Low"]
cm = confusion_matrix(y_te, pred, labels=labels)
sns.heatmap(cm, annot=True, fmt="d", xticklabels=labels, yticklabels=labels, cmap="Blues")
plt.xlabel("Predicted"); plt.ylabel("Actual"); plt.title("Priority Model - Confusion Matrix")
plt.savefig("models/confusion_matrix.png", dpi=120, bbox_inches="tight")

joblib.dump(pipe, "models/priority_model.joblib")
print("Saved models/priority_model.joblib")
