import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.config.settings import settings
from app.routers.product_routes import router as product_router


# Configure application logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="ShopEase Product Management Microservice"
)


# Register Product Router
app.include_router(product_router)


@app.get("/", tags=["Health"])
def root():
    return {
        "message": "Welcome to ShopEase Product Service",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "Running"
    }


@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "service": settings.APP_NAME
    }


@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):
    """Handle unexpected application errors safely."""

    logger.exception(
        "Unexpected error while processing %s %s",
        request.method,
        request.url.path
    )

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error"
        }
    )