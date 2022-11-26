from http import HTTPStatus
from typing import Dict

from fastapi import Depends, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session

from app.routers import api

# Define application
app = FastAPI(
    title="FastAPI Blog App",
    description="Create Blogs.",
    version="0.1",
)

app.include_router(api.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.on_event("startup")
# async def on_startup():
#     await init_db()


@app.get("/home", tags=["home"])
def get_home():
    """Root Endpoint"""
    return {"message": "Hello World"}


@app.get("/")
def _index() -> Dict:
    """Health check."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {},
    }
    return response
