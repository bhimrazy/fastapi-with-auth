from app import schemas
from app.models import Post
from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from app.db import Base, get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/posts", tags=["posts"])

# response_model=List[schemas.Post]


@router.get("/")
async def index(session: AsyncSession = Depends(get_session)):
    """Get all posts"""
    # posts = await Post.get_all()
    result = await session.execute(select(Post))
    posts = result.scalars().all()
    print(posts)
    return {"message": "Welcome to Posts"}
