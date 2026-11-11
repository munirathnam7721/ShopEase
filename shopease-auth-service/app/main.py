from fastapi import FastAPI

from app.core.config import settings
from app.routers.auth_routes import router as auth_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="ShopEase Authentication Microservice",
)

app.include_router(auth_router)


@app.get("/", tags=["Health"])
def root() -> dict[str, str]:
    """Service health endpoint."""

    return {
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    """Health check endpoint."""

    return {
        "status": "healthy",
    }
