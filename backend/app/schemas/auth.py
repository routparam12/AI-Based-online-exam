from pydantic import BaseModel

from app.models.user import UserRole


class LoginRequest(BaseModel):
    roll_number: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    role: UserRole


class CandidateCreate(BaseModel):
    roll_number: str
    full_name: str
    password: str


class UserResponse(BaseModel):
    id: str
    roll_number: str
    full_name: str
    role: UserRole

    model_config = {
        "from_attributes": True
    }