# ResumeIQ

ResumeIQ is a web-based Resume Intelligence System built with **Python**, **Flask**, and **SQLite**. It helps job seekers compare their resumes with a job description by extracting skills, matching them against a master skill database, and calculating an ATS (Applicant Tracking System) score.

---

## Features

- Upload resumes in **PDF** and **DOCX** format.
- Paste a job description.
- Extract skills from resumes.
- Compare resume skills with job requirements.
- Calculate ATS compatibility score.
- Display matched and missing skills.
- Maintain a master skills database using SQLite.

---

## Tech Stack

### Backend
- Python
- Flask
- SQLite

### Frontend
- HTML5
- CSS3

### Libraries
- PyPDF
- python-docx
- pathlib
- csv
- sqlite3
- re

---

## How It Works

1. Upload a resume (PDF or DOCX).
2. Paste the job description.
3. ResumeIQ extracts text from the uploaded resume.
4. Skills are identified using the master skills database.
5. Resume skills are compared with job description skills.
6. An ATS score is calculated.
7. Matched and missing skills are displayed.

---

## Installation

Clone the repository

```bash
git clone https://github.com/Jeyapradeepan2004/ResumeIQ.git
```

Go to the project directory

```bash
cd ResumeIQ
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## Screenshots

### Home Page

![Home Page](images/Home_page.png.png)

### Results Page

![Result Page](images/Result_page.png.png)

---

## Current Features

- Resume upload
- Job description input
- Resume text extraction
- Skill extraction
- ATS score calculation
- Skill matching
- Missing skills identification

---

## Future Improvements

- AI-powered resume recommendations
- Resume builder
- Resume download
- Skill categorization
- User authentication
- Dashboard with analytics
- Multiple resume comparison
- Improved ATS scoring algorithm
- Support for additional file formats

---

## Learning Outcomes

This project helped me learn:

- Flask web development
- File handling in Python
- SQLite database management
- Regular expressions
- Resume parsing
- HTML & CSS
- Git and GitHub
- Project structuring

---

## Author

**Jeya Pradeepan**

GitHub: https://github.com/Jeyapradeepan2004

LinkedIn: *(Add your LinkedIn profile here)*

---

## License

This project is licensed under the MIT License.
