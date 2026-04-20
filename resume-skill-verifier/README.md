# 🚀 AI Resume Skill Verifier  
### **By Smit Mahajan**  
### URL: https://github.com/smitmahajan210

## 🌟 Overview
An end-to-end AI-powered platform that analyzes a candidate’s resume, extracts claimed skills, scans real GitHub repositories, and verifies whether those skills are genuinely demonstrated in their code.

This project solves a real recruiting challenge — **resume skill inflation** — using LLMs, embeddings, ML models, and full‑stack cloud engineering.

---

# 🖼️ GitHub Banner  
![banner](https://dummyimage.com/1200x300/000/fff&text=AI+Resume+Skill+Verifier)

---

# 🏆 Badges  
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Python](https://img.shields.io/badge/python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-success)
![Next.js](https://img.shields.io/badge/Next.js-Frontend-black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-DB-blue)
![AWS](https://img.shields.io/badge/AWS-Deployable-orange)
![License](https://img.shields.io/badge/license-MIT-green)

---

# ✨ Features
- 🔍 AI Resume Parsing (LLMs)
- 🧠 Code Intelligence Engine (LLM + Static Code Analysis)
- 📊 ML Trust Score Model
- 🌐 Full Stack Web App (Next.js + FastAPI)
- 🗃 PostgreSQL Database
- 🐳 Full Docker Support
- ☁️ AWS Deployable

---

# 🏗️ Architecture Diagram

```mermaid
flowchart TD
    A[Resume PDF Upload] --> B[FastAPI Backend]
    B --> C[LLM Resume Parser]
    C --> D[Skill Extraction]
    B --> E[GitHub Repo Analyzer]
    E --> F[Code Embeddings + LLM Analysis]
    D --> G[Skill Comparator]
    F --> G
    G --> H[Random Forest Trust Score Model]
    H --> I[Skill Verification Report]
    I --> J[Next.js User Interface]
```

---

# ⚙️ System Flow Diagram

```mermaid
sequenceDiagram
    User->>Frontend: Upload Resume + GitHub Username
    Frontend->>Backend: Send resume file + username
    Backend->>LLM: Parse resume -> skills
    Backend->>GitHub API: Fetch repos
    GitHub API->>Backend: Return repo list + code
    Backend->>ML Engine: Compute embeddings + trust score
    ML Engine->>Backend: Final report
    Backend->>Frontend: Display trust score + report
```

---

# 💻 Tech Stack
### **Frontend**
- Next.js, React, TypeScript, TailwindCSS  

### **Backend**
- FastAPI, Python, LangChain, PyMuPDF  

### **AI/ML**
- SentenceTransformers  
- Random Forest Classifier  
- OpenAI / Groq / Llama 3  

### **Database**
- PostgreSQL (SQLAlchemy ORM)

### **DevOps**
- Docker, Docker Compose  
- AWS S3, ECR, ECS Optional Deployment  

---

# 🚀 How to Run Locally

```bash
docker-compose up --build
```

Or run services without Docker:

```bash
# terminal 1
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# terminal 2
cd frontend
npm install
npm run dev
```

Services:
| Service | 
|---------|
| Frontend| 
| Backend | 
| Docs    |

---

# 📦 Project Structure

```
resume-skill-verifier/
│── backend/
│── frontend/
│── docker-compose.yml
│── README.md
```

---

# 🤖 ML
The ML engine compares **claimed skills** vs **verified GitHub skills**.

### Features Used:
- LLM skill extraction  
- Code embeddings  
- Repo complexity metrics  
- Library detection  

### Model:
- Random Forest Classifier → Trust Score (0–100)

### Interview Pitch:
“I built an ML pipeline that cross-verifies resume skills with real GitHub code using LLMs, embeddings, and a Random Forest model.”

---

# 📑 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/upload_resume` | Extracts data from resume |
| GET | `/github/{username}` | Fetches repos |
| POST | `/verify` | Runs ML trust score |
| GET | `/report/{id}` | Returns final report |

---

# 🖼️ Screenshot Placeholders
Add your own screenshots in `/screenshots`:

```
screenshots/
  ui-dashboard.png
  resume-upload.png
  verification-report.png
  trust-score.png
```

---

# 👨‍💻 Author  
**Smit Mahajan**  
MS in CSE @ University at Buffalo  
GitHub: https://github.com/smitmahajan210  
LinkedIn: Add your link here  

---

# 📜 License  
MIT License  
