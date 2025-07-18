
# 🧠 Agentic Resume Matcher

Agentic Resume Matcher is an AI-powered tool that intelligently matches candidate resumes to job descriptions using Large Language Models (LLMs) and agentic reasoning. Upload resumes and a job description, and the app will return the **top 5 best-matched candidates** based on skills relevance.

---

## 🚀 Features

- 📄 Upload multiple resumes (PDF/Text)
- 📋 Upload a job description
- 🧠 AI analyzes and extracts relevant skills and experience
- 🔍 Ranks and recommends top 5 matching candidates
- 🌐 Streamlit interface for easy interaction

---

## 🛠️ Technologies Used

- **Python 3**
- **Streamlit** – for web UI
- **Groq API** – for fast and affordable LLM inference (Mistral model)
- **PyMuPDF / pdfminer** – for PDF parsing
- **LangChain** – for agent-like processing logic

---

## 📁 Project Structure

```
📦 Agentic_HR
├── main.py              # Main Streamlit app
├── resume_reader.py     # Extracts text from resumes
├── jd_analyzer.py       # Extracts key info from job descriptions using Groq
├── matcher.py           # Compares resumes and job info, assigns match scores
├── requirements.txt     # Python dependencies
├── README.md            # This file
```

---

## ⚙️ Installation

```bash
git clone https://github.com/usamanisarkhan/Agentic_HR.git
cd Agentic_HR
pip install -r requirements.txt
```

---

## 🔑 Setup

Create a `.env` file with the following:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🧪 Run Locally

```bash
streamlit run main.py
```

---

## ☁️ Deploy on Hugging Face

1. Upload your repo to Hugging Face Spaces.
2. In `README.md`, add:
```yaml
sdk: streamlit
app_file: main.py
```
3. Set your secret in Hugging Face Space → Settings → Repository Secrets → `GROQ_API_KEY`

---

 Use Cases

- HR recruiters shortlisting candidates faster
- Automated resume screening for large hiring rounds
- Candidate-job matching in freelancing platforms


## 📃 License

MIT License
