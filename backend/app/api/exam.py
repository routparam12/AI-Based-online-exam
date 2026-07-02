from fastapi import APIRouter, HTTPException

from app.schemas.question_request import QuestionGenerationRequest
from app.ai_layer.agent.question_generation_agent import QuestionGenerationAgent
from app.ai_layer.vectorstore.load_vector_store import load_vector_store

router = APIRouter(
    prefix="/exam",
    tags=["Exam"]
)

agent = QuestionGenerationAgent()


@router.post("/generate")
async def generate_questions(
    request: QuestionGenerationRequest
):

    try:

        vector_store = load_vector_store()

        questions = await agent.generate_questions(
            vectorstore=vector_store,
            query=request.query,
            difficulty=request.difficulty,
            count=request.count
        )

        return {
            "success": True,
            "questions": questions
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )