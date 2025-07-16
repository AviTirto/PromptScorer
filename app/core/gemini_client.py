import google.generativeai as genai
from app.schemas.gemini.criterias import GRADING_CRITERIA_SYSTEM_PROMPT
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class GeminiClient:
    def __init__(self):
        if not settings.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(
            settings.GEMINI_MODEL_NAME,
            system_instruction=GRADING_CRITERIA_SYSTEM_PROMPT
        )
        logger.info(f"Gemini client initialized with model: {settings.GEMINI_MODEL_NAME}")
        
    async def generate_content(self, prompt: str) -> str:
        """
        Sends a prompt to the Gemini API and returns the generated text.
        """
        try:
            response = await self.model.generate_content_async(prompt)
            if response.candidates and response.candidates[0].content.parts:
                return response.candidates[0].content.parts[0].text
            return "No content generated."
        except Exception as e:
            logger.error(f"Error calling Gemini API: {e}")
            raise
        
gemini_client = GeminiClient()
            