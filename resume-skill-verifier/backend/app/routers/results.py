from fastapi import APIRouter

router = APIRouter()


@router.get("/{candidate_id}")
def get_result(candidate_id: str):
    return {
        "candidate_id": candidate_id,
        "status": "pending",
        "message": "Result generation is not yet implemented",
    }
