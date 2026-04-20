from fastapi import APIRouter, File, UploadFile

router = APIRouter()


@router.post("/upload")
async def upload_resume(resume: UploadFile = File(...)):
    content = await resume.read()
    return {
        "filename": resume.filename,
        "content_type": resume.content_type,
        "size_bytes": len(content),
        "message": "Resume uploaded successfully",
    }
