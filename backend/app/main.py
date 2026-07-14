from fastapi import FastAPI

# Database
from app.db.database import engine, Base

# Models
from app.models.user import User
from app.models.workflow import Workflow

# API Routers
from app.api.users import router as user_router
from app.api.auth import router as auth_router
from app.api.workflows import router as workflow_router

from app.models.document import Document
from app.api.documents import router as document_router

# Create all database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title="IntelliFlow AI API",
    description="Enterprise Intelligence & Workflow Automation Platform",
    version="1.0.0"
)

# Register API Routers
app.include_router(
    user_router,
    prefix="/users",
    tags=["Users"]
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    workflow_router,
    prefix="/workflows",
    tags=["Workflows"]
)

app.include_router(
    document_router,
    prefix="/documents",
    tags=["Documents"]
)

# Root Endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to IntelliFlow AI 🚀",
        "status": "Backend Running Successfully"
    }