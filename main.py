from fastapi import FastAPI
from app.api.endpoints import scoring as scoring_router
import uvicorn
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Prompt Scorer API",
    description="API for generating and scoring prompts using Gemini AI.",
    version="0.1.0"
)

app.include_router(
    scoring_router.router,
    prefix="/api/v1",
    tags=["scoring"]
)

@app.get("/")
async def root():
    """
    Root endpoint to check if the API is running.
    """
    return {"message": "Welcome to the Prompt Scorer API!"}

if __name__ == "__main__":
    logger.info("Starting FastAPI application...")
    uvicorn.run(app, host="0.0.0.0", port=8000)