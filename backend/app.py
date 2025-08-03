# UPDATED main application file.
# No major changes needed here, as the router-based design is already scalable.
# We just confirm all modules are correctly wired.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.core.config import settings
from backend.api.v1.routes import schemes, users, community

# --- Initialize the FastAPI App ---
app = FastAPI(
    title=settings.APP_NAME,
    description="An AI-powered platform to help citizens find and apply for government schemes.",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# --- CORS (Cross-Origin Resource Sharing) Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Include API Routers ---
app.include_router(schemes.router, prefix=f"{settings.API_V1_STR}/schemes", tags=["Schemes"])
app.include_router(users.router, prefix=f"{settings.API_V1_STR}/users", tags=["Users"])
app.include_router(community.router, prefix=f"{settings.API_V1_STR}/community", tags=["Community"])

# --- Root Endpoint for Health Check ---
@app.get("/", tags=["Health Check"])
def read_root():
    """A simple health check endpoint to confirm the API is running."""
    return {"status": "ok", "message": f"Welcome to the {settings.APP_NAME}"}