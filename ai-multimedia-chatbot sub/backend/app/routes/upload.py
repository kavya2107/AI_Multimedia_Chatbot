from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.services.pdf_service import extract_text_from_pdf
from app.services.summary_service import generate_summary

from app.utils.storage import document_text
import app.utils.storage as storage

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = ""
    summary = ""

    # Process PDF
    if file.filename.endswith(".pdf"):

        extracted_text = extract_text_from_pdf(file_path)

        # Save globally for chatbot
        storage.document_text = extracted_text

        summary = generate_summary(extracted_text)

    return {
        "filename": file.filename,
        "message": "File uploaded successfully",
        "summary": summary
    }