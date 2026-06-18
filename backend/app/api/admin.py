from fastapi import APIRouter, Depends, HTTPException,FastAPI

router = APIRouter()


@router.get("/admin")
async def get_admin():
    return {
        "admin": ["me as admin"]
    }
