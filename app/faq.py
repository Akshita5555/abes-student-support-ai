"""FAQ knowledge base: 25 entries (category, question, answer)."""

FAQS = [
    # ---------------- IT Support (5) ----------------
    ("IT Support", "How do I reset my university portal password?",
     "Open the student portal, click 'Forgot Password', enter your roll number and registered email, and follow the OTP link. If you do not get the mail, contact the IT Help Desk."),
    ("IT Support", "I cannot log in to the student portal.",
     "Check your roll number and password, clear browser cache, and try again. If the problem continues, use 'Forgot Password' or contact the IT Help Desk with your roll number."),
    ("IT Support", "I cannot upload my assignment on the LMS.",
     "Check that the file is in the allowed format (PDF/DOCX) and within the size limit, and that the submission deadline has not passed. Try another browser; if it still fails, mail the IT Help Desk with a screenshot."),
    ("IT Support", "How do I connect to the campus Wi-Fi?",
     "Select the campus Wi-Fi network and log in with your student portal ID and password. If login fails, ask the IT Help Desk to register your device."),
    ("IT Support", "How do I get my official college email ID?",
     "Official email IDs are created after admission. Check your registered mail for credentials, or request it from the IT Help Desk with your roll number."),
    # ---------------- Examination (5) ----------------
    ("Examination", "How do I download my admit card or hall ticket?",
     "Log in to the examination portal, open 'Admit Card', and download the PDF. If it is not available or shows an error, contact the Examination Cell immediately with your roll number, especially if your exam is close."),
    ("Examination", "Where can I check my exam result?",
     "Results are published on the examination portal. Log in with your roll number and open the 'Results' section."),
    ("Examination", "How do I apply for re-evaluation or rechecking?",
     "Apply on the examination portal within the notified window after results, select the subject, and pay the re-evaluation fee."),
    ("Examination", "Where can I find the exam date sheet?",
     "The date sheet is uploaded on the examination portal and displayed on department notice boards."),
    ("Examination", "What should I do if I missed an exam due to illness?",
     "Submit a written application with a medical certificate to the Examination Cell as early as possible to ask about a supplementary or backlog exam."),
    # ---------------- Fees (3) ----------------
    ("Fees", "How can I pay my university fees?",
     "Log in to the fee portal, choose 'Pay Fees', and pay online by UPI, net banking or card. Keep the receipt for your records."),
    ("Fees", "What is the last date for fee payment?",
     "The last date is given in the fee notice on the portal. Late payment may attract a fine, so please check the latest notice."),
    ("Fees", "My fee payment failed but money was deducted.",
     "Wait 24-48 hours for auto-reversal. If it is not reversed, contact the Accounts Office with the transaction ID and a screenshot."),
    # ---------------- Library (3) ----------------
    ("Library", "What are the library working hours?",
     "The library is open on working days from morning to evening. Exact timings are displayed at the library entrance and on the college website."),
    ("Library", "How many books can I issue from the library?",
     "Students can issue a limited number of books at a time for a fixed period. Check with the library desk for the current limit; late return may attract a fine."),
    ("Library", "How do I access e-journals and the digital library?",
     "Log in to the digital library link on the student portal with your credentials to read e-books and journals."),
    # ---------------- Hostel (3) ----------------
    ("Hostel", "How do I apply for a hostel room?",
     "Fill the hostel application form on the portal or at the Hostel Office, attach the required documents and pay the hostel fee. Rooms are allotted as per availability."),
    ("Hostel", "What are the hostel gate timings?",
     "Hostel gate timings are set by the warden and displayed on the hostel notice board. Late entry requires prior permission."),
    ("Hostel", "How do I report a maintenance problem in my hostel room?",
     "Register a complaint with the hostel warden or on the hostel complaint register/portal, mentioning your room number and the issue."),
    # ---------------- Admissions (2) ----------------
    ("Admissions", "What documents are required for admission?",
     "Usually the 10th and 12th marksheets, transfer certificate, ID proof, passport-size photos, and the entrance score card/counselling letter. Check the admission notice for the exact list."),
    ("Admissions", "How can I get my bonafide certificate or ID card?",
     "Apply at the Student Section / Admission Office with a request form and your roll number. ID cards are issued after admission formalities are complete."),
    # ---------------- Scholarship (2) ----------------
    ("Scholarship", "How do I apply for a scholarship?",
     "Apply on the scholarship portal within the notified dates, upload income and category certificates and marksheets, and submit the form to the college for verification."),
    ("Scholarship", "When will my scholarship amount be credited?",
     "Scholarship amounts are credited after government verification, which can take a few weeks. Check your application status on the scholarship portal."),
    # ---------------- Courses (2) ----------------
    ("Courses", "How do I choose or change my elective subject?",
     "Elective selection opens for a limited period on the student portal. Submit the change request to your department coordinator within that window."),
    ("Courses", "Where can I get the syllabus of my course?",
     "The latest syllabus is available on the university/college website under your department's academic section, and with your department office."),
]

assert len(FAQS) == 25, "Knowledge base must contain exactly 25 entries"
