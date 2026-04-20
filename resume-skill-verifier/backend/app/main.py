from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, resumes, tests, results

app = FastAPI(title="AI Resume & Skill Verifier")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(resumes.router, prefix="/resumes", tags=["resumes"])
app.include_router(tests.router, prefix="/tests", tags=["tests"])
app.include_router(results.router, prefix="/results", tags=["results"])

@app.get("/")
def root():
    return {"message": "Resume & Skill Verifier API Running"}
