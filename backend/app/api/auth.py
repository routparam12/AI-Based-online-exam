from fastapi import APIRouter, Depends, HTTPException,FastAPI

router = APIRouter()


@router.get("/users")
async def get_users():
    return {
        "users": ["vivek","Param"]
    }
