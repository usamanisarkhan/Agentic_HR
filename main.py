import streamlit as st
import os
from resume_parser import extract_text_from_pdf
from jd_analyzer import analyze_job_description
from matcher import match_score

##

st.title("🔍 Agentic Resume Matcher")

jd_file = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])
resume_files = st.file_uploader("Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

if jd_file and resume_files:
    with open("temp_jd.pdf", "wb") as f:
        f.write(jd_file.read())
    jd_text = extract_text_from_pdf("temp_jd.pdf")
    jd_info = analyze_job_description(jd_text)

    results = []
    for resume_file in resume_files:
        with open("temp_resume.pdf", "wb") as f:
            f.write(resume_file.read())
        resume_text = extract_text_from_pdf("temp_resume.pdf")
        score, matched_skills = match_score(jd_info, resume_text)
        results.append({
            "name": resume_file.name,
            "score": score,
            "matched_skills": matched_skills
        })

    top_5 = sorted(results, key=lambda x: x["score"], reverse=True)[:5]
    st.subheader("🏆 Top 5 Matching Candidates")
    for r in top_5:
        st.markdown(f"**{r['name']}** — Score: {r['score']}%")
        st.markdown(f"Matched Skills: {', '.join(r['matched_skills'])}")
