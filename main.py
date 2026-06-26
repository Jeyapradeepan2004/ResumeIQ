# ==========================
# Imports
# ==========================

from pypdf import PdfReader
from docx import Document
from pathlib import Path
import sqlite3
import csv
import os
import re

# ==========================
# Resume Intelligence System
# ==========================
class RIS:

# ==========================
# Constructor
# ==========================
    def __init__(self):

        self.con = sqlite3.connect(
            "ris.db",
            check_same_thread= False
            )
        self.cur = self.con.cursor()
    
        self.create_tables()
        
        self.populate_master_skills()

# ==========================
# Database Setup
# ==========================
    def create_tables(self):

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS resume(
            resume_id INTEGER PRIMARY KEY AUTOINCREMENT,
            resume_text TEXT
        )""")

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS skills(
            skills_id INTEGER PRIMARY KEY AUTOINCREMENT,
            resume_id INTEGER,
            skill_name TEXT,
            FOREIGN KEY(resume_id)
                REFERENCES resume(resume_id)
        )""")
        
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS master_skills(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_name TEXT UNIQUE,
            category TEXT
        )""")

        self.con.commit()
        
        
# ==========================
# master Skill
# ==========================
    
    def populate_master_skills(self):
        path = Path("RIS/data/master_skills.csv")
        with path.open(mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            
            header = next(reader)
            
            for skill_name, category in reader:
                self.cur.execute("""
                    INSERT OR IGNORE INTO master_skills(
                        skill_name,
                        category
                        )
                        VALUES(?, ?)
                        """, (skill_name, category))
                
            self.con.commit()
            
            
    def load_master_skills(self):
        self.cur.execute("""
            SELECT skill_name
            FROM master_skills
        """)
        
        return {
            row[0].lower()
            for row in self.cur.fetchall()
        }

# ==========================
# File Extraction Methods
# ==========================

    def extract_pdf_text(self, file_path):
        pdf_reader = PdfReader(file_path)

        text = ""

        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"

        return text

    def extract_docx_text(self, file_path):
        document = Document(file_path)

        return "\n".join(
            para.text
            for para in document.paragraphs
        )

    def extract_text(self, file_path):
        extension = os.path.splitext(
            file_path
        )[1].lower()

        if extension == ".pdf":
            return self.extract_pdf_text(file_path)

        if extension == ".docx":
            return self.extract_docx_text(file_path)

        raise ValueError(
            "Unsupported File Format"
        )

# ==========================
# Skills Management
# ==========================

    def extract_skills_from_text(self, text):
        
        master_skills = self.load_master_skills()
        
        text = text.lower()
        
        candidate_skills = set()
        
        for skill in master_skills:
            pattern = rf"\b{re.escape(skill)}\b"
            if re.search(pattern, text):
                candidate_skills.add(skill)
                
        
        return candidate_skills
            
    
# ==========================
# ATS Score Management
# ==========================

    def compare_skills(self, resume_skills, job_skills):
        
        matched = resume_skills & job_skills
        
        missed = job_skills - resume_skills
        
        return matched, missed
    
    
    def calculate_ats_score(self, resume_skills, job_skills):
        
        if not job_skills:
            return 0
        
        matched = resume_skills & job_skills
        
        score = (len(matched) / len(job_skills)) * 100
        
        return round(score, 2)
    
ris = RIS()
# print(ris.load_master_skills())

