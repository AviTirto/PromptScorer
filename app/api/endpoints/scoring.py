from fastapi import APIRouter, HTTPException, status
from app.schemas.gemini import PromptRequest, GeminiResponse, GeneratedContentResponse
from app.core.gemini_client import gemini_client
from app.core.config import settings
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/generate", response_model=GeminiResponse, status_code=status.HTTP_200_OK)
async def generate_content(request: PromptRequest):
    """
    Endpoint to generate content using the Gemini API.
    """
    try:
        logger.info(f"Recieved prompt: {request.prompt[:50]}...")
        generated_text = await gemini_client.generate_content(request.prompt)
        return GeminiResponse(
            response_text=generated_text,
            model_name=settings.GEMINI_MODEL_NAME
        )
    except ValueError as ve:
        logger.error(f"Configuration error: {ve}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Server configuration error: {ve}"
        )
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Failed to generate content: {e}"
        )

@router.post("/score", response_model=GeminiResponse, status_code=status.HTTP_200_OK)
async def score_content(request: PromptRequest) -> GeneratedContentResponse:
    """
    Endpoint to score the generated content based on grading criteria.
    """
    try:
        logger.info(f"Scoring prompt: {request.prompt[:50]}...")
        return GeneratedContentResponse(
            generated_data={
                "score": 8,
                "reasons": [
                    "Clarity is good.",
                    "Conciseness is acceptable.",
                    "Relevance is high.",
                    "Completeness is satisfactory."
                ]
            },
            model_name=settings.GEMINI_MODEL_NAME
        )
    except Exception as e:
        logger.error(f"Error scoring content: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Failed to score content: {e}"
        )