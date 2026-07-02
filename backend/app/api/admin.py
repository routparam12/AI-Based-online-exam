from fastapi import APIRouter, File, UploadFile

from app.services.Admin.upload_service import upload_pdf_service

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):

    return await upload_pdf_service(file)

#if __name__ == "__main__":
    