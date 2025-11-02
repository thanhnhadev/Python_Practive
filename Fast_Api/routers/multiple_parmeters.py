
from fastapi import APIRouter, Query, Path
router = APIRouter()

@router.get("/user")
async def get_user():
    return {"message": "Hello-World"}