import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from tools.job_api import fetch_jobs
import PyPDF2
import csv

# ✅ Page config
st.set_page_config(page_title="AI Job Finder", page_icon="🚀", layout="wide")

# 🎨 Dark UI
st.markdown("""
<style>
.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
    color: white;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}
.card:hover {
    transform: scale(1.02);
    transition: 0.2s;
}
</style>
""", unsafe_allow_html=True)

# 🎯 Title
st.title("🚀 AI Job Finder")
st.write("Find jobs based on your skills")

# 🔹 Sidebar
st.sidebar.title("🔍 Search")

# 🔹 Upload Resume
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

# 🔹 Extract text
def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

# 🔹 Extract skills
def extract_skills(text):
    skills_list = ["python", "java", "ai", "machine learning", "data", "sql", "react"]
    return [skill for skill in skills_list if skill in text]

# 🔹 Save job
def save_job(job):
    with open("saved_jobs.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([job.get("title"), job.get("company_name"), job.get("url")])

skills = []

# Resume logic
if uploaded_file:
    resume_text = extract_text(uploaded_file)
    skills = extract_skills(resume_text)
    st.success(f"📌 Skills detected: {skills}")

# Manual input
skills_input = st.text_input("Or enter skills manually:", "python, ai")

if not skills:
    skills = [s.strip().lower() for s in skills_input.split(",")]

# 🔹 Button
if st.button("Find Jobs"):

    with st.spinner("⏳ Finding best jobs..."):
        jobs = fetch_jobs()

    st.subheader("🎯 Top Matched Jobs")

    for i, job in enumerate(jobs):
        text = str(job).lower()
        score = sum(skill in text for skill in skills)

        if score > 0:
            # 🎨 Card
            st.markdown(f"""
            <div class="card">
                <h3>{job['title']}</h3>
                <p>🏢 {job['company_name']}</p>
                <p>⭐ Match Score: {score}</p>
            </div>
            """, unsafe_allow_html=True)

            # 🔹 Buttons (IMPORTANT)
            col1, col2 = st.columns(2)

            with col1:
                if "url" in job:
                    st.link_button("👉 Apply", job["url"])

            with col2:
                if st.button("💾 Save Job", key=i):
                    save_job(job)
                    st.success("Saved!")

            st.markdown("---")