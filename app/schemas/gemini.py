from pydantic import BaseModel, Field
from typing import List, Optional

# Chatting Schemas
class PromptRequest(BaseModel):
    prompt: str = Field(..., example="What is the capital of France?")
    
class GeminiResponse(BaseModel):
    response_text: str = Field(..., example="The capital of France is Paris.")
    model_name: str = Field(..., example="gemini-2.0-flash")

# Scoring Schemas  
class ScoredResponse(BaseModel):
    score: int = Field(..., description="Score the prompt based on the criteria. Score should be between 1 and 5.")
    reasons: List[str] = Field(..., description="List of reasons for the score given to the prompt. 1 reason per criteria. Give a suggestion based on the prompt for improvement for each criteria.")
    
class GeneratedContentResponse(BaseModel):
    generated_data: ScoredResponse 
    model_name: str = Field(..., example="gemini-2.0-flash")
    
# Suggestion Schemas
class LineSuggestion(BaseModel):
    line_number: int = Field(..., description="The 1-based line number that has a suggestion.")
    suggested_text: str = Field(..., description="The suggested text to replace the specified line.")
    
class SuggestionResponse(BaseModel):
    suggestions: List[LineSuggestion] = Field(..., description="A list of suggested changes for specific lines")
    model_name: str = Field(..., example="gemini-2.0-flash")