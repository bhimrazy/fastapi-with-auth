from fastapi import APIRouter
from app.routers import posts

router = APIRouter(prefix="/api/v1", tags=["api"])

router.include_router(posts.router)


@router.get("/")
async def api():
    """Returns data from api"""
    return {"message": "Welcome to API"}
