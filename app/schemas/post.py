from typing import Optional
from pydantic import BaseModel


# Shared properties
class PostBase(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    thumbnail: Optional[str] = None


# Properties to receive on Post creation
class PostCreate(PostBase):
    title: str
    body: str
    thumbnail: str


# Properties to receive on Post update
class PostUpdate(PostBase):
    pass


# Properties shared by models stored in DB
class PostInDBBase(PostBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Post(PostInDBBase):
    pass


# Properties properties stored in DB
class PostInDB(PostInDBBase):
    pass
