from fastapi import APIRouter, HTTPException, status
from app.schemas.gemini import PromptRequest, GeminiResponse, GeneratedContentResponse, SuggestionsResponse
from app.core.gemini_client import gemini_client
from app.core.config import settings
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/generate", response_model=GeminiResponse, status_code=status.HTTP_200_OK)
def generate_content(request: PromptRequest):
    """
    Endpoint to generate content using the Gemini API.
    """
    try:
        logger.info(f"Recieved prompt: {request.prompt[:50]}...")
        generated_text = gemini_client.generate_content(request.prompt)
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

@router.post("/score", response_model=GeneratedContentResponse, status_code=status.HTTP_200_OK)
def score_content(request: PromptRequest):
    """
    Receives a prompt and returns generated text from the Gemini API,
    formatted with a score and reasons based on grading criteria.
    """
    try:
        logger.info(f"Recieved prompt: {request.prompt[:50]}...")
        scored_data = gemini_client.generate_scored_content(request.prompt)
        return GeneratedContentResponse(
            generated_data=scored_data,
            model_name=settings.GEMINI_MODEL_NAME
        )
    except ValueError as ve:
        logger.error(f"Data validation error: {ve}")
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Invalid data received from Gemini: {ve}"
        )
    except Exception as e:
        logger.error(f"Error processing request: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate content: {e}"
        )
        
@router.post("/suggestions", response_model=SuggestionsResponse, status_code=status.HTTP_200_OK)
def get_suggestions(request: PromptRequest):
    try:
        logger.info(f"Recieved prompt: {request.prompt[:50]}...")
        scored_data = gemini_client.generate_scored_content(request.prompt)
        suggestions = gemini_client.generate_suggestions(request.prompt, scored_data.reasons)
        return SuggestionsResponse(
            score=scored_data.score,
            reasons=scored_data.reasons,
            suggestions=suggestions,
            model_name=settings.GEMINI_MODEL_NAME
        )
    except ValueError as ve:
        logger.error(f"Data validation error: {ve}")
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Invalid data received from Gemini: {ve}"
        )
    except Exception as e:
        logger.error(f"Error processing request: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate content: {e}"
        )
        