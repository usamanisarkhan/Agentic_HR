import json

def match_score(jd_json_str, resume_text):
    print("🧪 JD String Before JSON Parse:\n", jd_json_str)
    jd = json.loads(jd_json_str)
    jd_skills = set([skill.lower() for skill in jd.get("skills", [])])

    resume_words = set(resume_text.lower().split())

    matched_skills = jd_skills & resume_words
    score = len(matched_skills) / max(len(jd_skills), 1)

    return round(score * 100, 2), list(matched_skills)
