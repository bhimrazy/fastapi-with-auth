from typing import Dict
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from app.routers import api
from http import HTTPStatus

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
