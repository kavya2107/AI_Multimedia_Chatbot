from fastapi import APIRouter

from app.services.chatbot_service import answer_question
import app.utils.storage as storage

router = APIRouter()


@router.get("/chat")
def chat(question: str):

    if storage.document_text == "":
        return {
            "answer": "No PDF uploaded yet."
        }

    answer = answer_question(
        storage.document_text,
        question
    )

    return {
        "question": question,
        "answer": answer
    }