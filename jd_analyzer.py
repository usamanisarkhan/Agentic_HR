import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def analyze_job_description(jd_text):
    prompt = f"""
    Analyze the following job description and extract the following fields in JSON format:
    - skills (as a list of strings)
    - years_of_experience (integer or string)
    - education (string or list)

    Respond only in JSON.
    
    Job Description:
    {jd_text}
    """
            

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=payload)

    try:
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print("❌ Error in Groq response:")
        print("Status Code:", response.status_code)
        print("Response Body:", response.text)
        raise e
