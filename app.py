from flask import Flask, render_template, request
from main import RIS

import os
import uuid

app = Flask(__name__)

ris = RIS()

# ==========================
# Upload Folder
# ==========================

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ==========================
# Home Page
# ==========================

@app.route("/")
def home():
    return render_template("home.html")


# ==========================
# Upload Resume
# ==========================

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]
    job_description = request.form["job_description"]

    # Generate unique filename
    extension = os.path.splitext(file.filename)[1]
    filename = f"{uuid.uuid4()}{extension}"

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    # Save uploaded file
    file.save(filepath)

    # Extract resume text
    resume_text = ris.extract_text(filepath)

    # Extract skills
    resume_skills = ris.extract_skills_from_text(resume_text)
    job_skills = ris.extract_skills_from_text(job_description)

    # Compare skills
    matched, missed = ris.compare_skills(
        resume_skills,
        job_skills
    )

    # Calculate ATS Score
    score = ris.calculate_ats_score(
        resume_skills,
        job_skills
    )

    # Render result page
    return render_template(
        "result.html",
        score=score,
        resume_skills=sorted(resume_skills),
        job_skills=sorted(job_skills),
        matched=sorted(matched),
        missed=sorted(missed)
    )


# ==========================
# Run Application
# ==========================

if __name__ == "__main__":
    app.run(debug=True)