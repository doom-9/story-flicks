from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware
from app.api import api_router

app = FastAPI(
    title="StoryFlicks Backend API",
    description="Backend API for StoryFlicks application",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/tasks", StaticFiles(directory="tasks"), name="tasks")

# Include API router
app.include_router(api_router)

@app.get("/")
async def root():
    return {
        "app_name": "StoryFlicks Backend API",
        "docs_url": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
