from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

origins = [
    ".vercel.app",
    "*",
]

def add_cors_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET"],
        allow_headers=["*"],
    )
