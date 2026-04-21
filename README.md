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

![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-Frontend-000000?logo=next.js&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Deployable-FF9900?logo=amazonaws&logoColor=white)

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
# from repo root
cd resume-skill-verifier
cp .env.example .env   # edit .env if needed
docker-compose up --build
```

Or run services without Docker:

```bash
# terminal 1 – backend
cd resume-skill-verifier/backend
pip install -r requirements.txt
DATABASE_URL="postgresql://postgres:password@localhost:5432/resume_db" \
  uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# terminal 2 – frontend
cd resume-skill-verifier/frontend
npm install
NEXT_PUBLIC_API_URL=http://localhost:8000 npm run dev
```

Services:
| Service | URL |
|--------|-----|
| Frontend | http://localhost:3000 |
| Backend | http://localhost:8000 |
| Docs | http://localhost:8000/docs |

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

# 🤖 ML Explanation (For Interviews)
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
| GET | `/auth/health` | Auth health check |
| POST | `/resumes/upload` | Upload and parse a resume |
| GET | `/tests/questions?skill=<skill>` | Get skill-based interview questions |
| GET | `/results/{candidate_id}` | Retrieve verification result for a candidate |

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
LinkedIn: https://www.linkedin.com/in/smitmahajan/
