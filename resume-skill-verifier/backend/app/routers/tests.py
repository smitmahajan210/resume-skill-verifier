from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/questions")
def get_questions(skill: str = Query(default="python")):
    return {
        "skill": skill,
        "questions": [
            f"Explain the fundamentals of {skill}.",
            f"What is one common pitfall in {skill} projects?",
        ],
    }
