from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.future import select
from sqlalchemy.sql.sqltypes import TIMESTAMP
from app.db import Base, get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=True)
    thumbnail = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    author = relationship('User')

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id}, "
            f")>"
        )

    @classmethod
    async def get_all(cls, db: AsyncSession = Depends(get_session)):
        query = select(cls)
        posts = await db.execute(query)
        posts = posts.scalars().all()
        return posts
