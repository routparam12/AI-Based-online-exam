# Import FastAPI framework
from fastapi import FastAPI

# Import routers from different modules
# auth_router handles authentication-related APIs
from app.api.auth import router as auth_router

# admin_router handles admin-related APIs
from app.api.admin import router as admin_router


# Create FastAPI application instance
app = FastAPI(
    title="AI Exam Center API",          # API title shown in Swagger UI
    description="FastAPI Backend",       # API description
    version="1.0.0"                      # Current API version
)


# Register Authentication APIs
# All auth routes will be prefixed with /api/v1
# Example: /api/v1/login, /api/v1/register
app.include_router(auth_router, prefix="/api/v1")


# Register Admin APIs
# All admin routes will also be prefixed with /api/v1
# Example: /api/v1/users, /api/v1/exams
app.include_router(admin_router, prefix="/api/v1")


# Root endpoint
# Used to verify that the API server is running
@app.get("/")
async def root():
    return {
        "message": "API is running"
    }


# Health check endpoint
# Commonly used by load balancers, monitoring tools,
# Docker/Kubernetes health probes, etc.
@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }