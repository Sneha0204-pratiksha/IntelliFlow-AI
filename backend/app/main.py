from fastapi import FastAPI

from app.db.database import engine, Base
from app.models.user import User
from app.api.users import router as user_router
from app.api.auth import router as auth_router

# Create all database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title="IntelliFlow AI API",
    description="Enterprise Intelligence & Workflow Automation Platform",
    version="1.0.0"
)

# Include API Routers
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

# Root Endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to IntelliFlow AI 🚀",
        "status": "Backend Running Successfully"
    }