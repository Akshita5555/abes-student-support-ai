"""
Creates university_query_train.csv (5000 rows) and university_query_test.csv (1000 rows)
in ./data. Run only if you do not already have your own CSV files.
Columns: Query_ID, Student_Query, Department, Days_To_Deadline, Priority_Label
Priority rule: <=2 days -> High, 3-7 days -> Medium, >7 days -> Low.
The test set uses different base-query/phrasing combinations from training, so the
accuracy is a more honest measure than train == test data.
"""
import random
import pandas as pd

random.seed(42)

BASE = {
    "Examination": ["download my admit card", "get my hall ticket", "check my exam result",
                    "apply for re-evaluation", "see the exam date sheet", "fix my exam form error"],
    "IT Support": ["reset my portal password", "log in to the student portal",
                   "upload my assignment on LMS", "connect to campus Wi-Fi", "get my college email ID"],
    "Fees": ["pay my semester fees", "get my fee receipt", "fix a failed fee payment", "know the fee due date"],
    "Library": ["issue a book from the library", "renew my library book", "access e-journals"],
    "Hostel": ["apply for a hostel room", "report a hostel room problem", "know hostel gate timings"],
    "Admissions": ["submit my admission documents", "get my ID card", "get a bonafide certificate"],
    "Scholarship": ["apply for a scholarship", "check my scholarship status"],
    "Courses": ["change my elective subject", "get my course syllabus"],
}
OPENERS = ["I cannot", "I am unable to", "How can I", "Please help me", "I want to", "Need help to", "Kindly tell me how to"]

HIGH = ["my exam is tomorrow", "the deadline is today", "the last date is tomorrow", "my exam is in 2 days", "it is very urgent"]
MED = ["the last date is in 5 days", "my deadline is this week", "I have 6 days left", "the deadline is in 4 days"]
LOW = ["no rush", "I have plenty of time", "the deadline is next month", "just asking for information", "the last date is in 20 days"]

def make(n, bases_filter):
    rows = []
    for i in range(n):
        dept = random.choice(list(BASE))
        base = random.choice(BASE[dept])
        opener = random.choice(OPENERS)
        label = random.choice(["High", "Medium", "Low"])
        if label == "High":
            days, cue = random.randint(0, 2), random.choice(HIGH)
        elif label == "Medium":
            days, cue = random.randint(3, 7), random.choice(MED)
        else:
            days, cue = random.randint(8, 45), random.choice(LOW)
        # keep train/test phrasing combos different
        if bases_filter == "train":
            opener = random.choice(OPENERS[:5])
        else:
            opener = random.choice(OPENERS[2:])
        q = f"{opener} {base}, {cue}"
        rows.append((q, dept, days, label))
    return rows

def save(rows, path, start):
    df = pd.DataFrame(rows, columns=["Student_Query", "Department", "Days_To_Deadline", "Priority_Label"])
    df.insert(0, "Query_ID", range(start, start + len(df)))
    df.to_csv(path, index=False)
    print(path, df.shape, df.Priority_Label.value_counts().to_dict())

if __name__ == "__main__":
    save(make(5000, "train"), "data/university_query_train.csv", 1)
    save(make(1000, "test"), "data/university_query_test.csv", 5001)
