from pydantic import BaseModel


class QuestionGenerationRequest(BaseModel):
    query: str
    difficulty: str
    count: int
    question_type: str = "mcq"