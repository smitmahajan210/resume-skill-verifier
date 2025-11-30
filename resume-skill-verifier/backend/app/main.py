from fastapi import FastAPI
from routers import auth, resumes, tests, results

app = FastAPI(title="AI Resume & Skill Verifier")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(resumes.router, prefix="/resumes", tags=["resumes"])
app.include_router(tests.router, prefix="/tests", tags=["tests"])
app.include_router(results.router, prefix="/results", tags=["results"])

@app.get("/")
def root():
    return {"message": "Resume & Skill Verifier API Running"}