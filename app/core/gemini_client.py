# import google.generativeai as genai
from google import genai
from app.core.criterias import GRADING_CRITERIA_SYSTEM_PROMPT, SUGGESTION_SYSTEM_PROMPT
from app.schemas.gemini import ScoredResponse
from app.core.config import settings
from typing import List
import logging
import json

logger = logging.getLogger(__name__)

class GeminiClient:
    def __init__(self):
        if not settings.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY,
        )
        logger.info(f"Gemini client initialized with model: {settings.GEMINI_MODEL_NAME}")
        
    def generate_content(self, prompt: str) -> str:
        """
        Sends a prompt to the Gemini API and returns the generated text.
        """
        try:
            response = self.client.models.generate_content(
                model=settings.GEMINI_MODEL_NAME,
                contents=prompt
            )
            if response.candidates and response.candidates[0].content.parts:
                return response.candidates[0].content.parts[0].text
            return "No content generated."
        except Exception as e:
            logger.error(f"Error calling Gemini API: {e}")
            raise
        
    def generate_scored_content(self, prompt: str) -> ScoredResponse:
        try:
            response = self.client.models.generate_content(
                model=settings.GEMINI_MODEL_NAME,
                contents=prompt, 
                config={
                    "system_instruction": GRADING_CRITERIA_SYSTEM_PROMPT,
                    "response_mime_type": "application/json",
                    "response_schema": ScoredResponse
                }
            )
            
            if response.candidates and response.candidates[0].content.parts:
                json_string = response.candidates[0].content.parts[0].text
                logger.info(f"Received raw JSON from Gemini: {json_string}")
                
                scored_data = ScoredResponse.model_validate_json(json_string)
                return scored_data
            
            raise Exception("No content or invalid content structure received from Gemini.")
        
        except json.JSONDecodeError as e:
            logger.error(f"Failed to decode JSON from Gemini response: {e}. Raw response: {response.candidates[0].content.parts[0].text if response.candidates and response.candidates[0].content.parts else 'N/A'}")
            raise ValueError(f"Gemini did not return valid JSON: {e}")
        except Exception as e:
            logger.error(f"Error calling Gemini API: {e}", exc_info=True)
            raise
        
    def generate_suggestions(self, original_text: str, reasons: List[str]) -> str:
        """
        Sends original text and scoring reasons to Gemini to get a completely rewritten prompt.
        Returns a single string representing the rewritten prompt.
        """
        
        suggestion_prompt = (
            f"Original Text:\n```\n{original_text}\n```\n\n"
            f"Reasons for current score:\n- {', '.join(reasons)}\n\n"
            f"Based on these reasons, rewrite the 'Original Text' to improve it. "
            f"Try to keep as many of the original lines or phrases as possible, "
            f"but feel free to add new lines or modify existing ones as needed to address the reasons. "
            f"Provide only the rewritten text, no other formatting or commentary."
        )
            
        try:
            response = self.client.models.generate_content(
                model=settings.GEMINI_MODEL_NAME,
                contents=suggestion_prompt,
                config={
                    "system_instruction": SUGGESTION_SYSTEM_PROMPT,
                }
            )
            if response.candidates and response.candidates[0].content.parts:
                return response.candidates[0].content.parts[0].text
            
            return original_text
        except json.JSONDecodeError as e:
            logger.error(f"Failed to decode JSON from Gemini response: {e}. Raw response: {response.candidates[0].content.parts[0].text if response.candidates and response.candidates[0].content.parts else 'N/A'}")
            raise ValueError(f"Gemini did not return valid JSON: {e}")
        except Exception as e:
            logger.error(f"Error calling Gemini API: {e}", exc_info=True)
            raise
        
        
gemini_client = GeminiClient()
            