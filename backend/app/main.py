from fastapi import FastAPI
from .api.endpoints import documents # Import the documents router

def create_app() -> FastAPI:
    app = FastAPI(
        title="AI CV & Job Application Assistant API",
        description="API for managing CVs, job applications, and AI-powered assistance.",
        version="0.0.1",
    )

    app.include_router(documents.router, prefix="/api/v1", tags=["Documents"])

    @app.get("/", summary="Root endpoint for API status check")
    async def read_root():
        return {"message": "AI CV & Job Application Assistant API is running!"}
    
    return app

app = create_app()
