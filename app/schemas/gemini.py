from pydantic import BaseModel, Field
from typing import List, Optional

class PromptRequest(BaseModel):
    prompt: str = Field(..., example="What is the capital of France?")
    
class GeminiResponse(BaseModel):
    response_text: str = Field(..., example="The capital of France is Paris.")
    model_name: str = Field(..., example="gemini-2.0-flash")
    
class ScoredResponse(BaseModel):
    score: int = Field(..., description="Score the prompt based on the criteria. Score should be between 1 and 10.")
    reasons: List[str] = Field(..., description="List of reasons for the score given to the prompt. 1 reason per criteria.")
    
class GeneratedContentResponse(BaseModel):
    generated_data: ScoredResponse 
    model_name: str = Field(..., example="gemini-1.5-flash")