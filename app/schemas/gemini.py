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
class SuggestionsResponse(BaseModel):
    score: int = Field(..., example=5)
    reasons: List[str] = Field(..., example=["Most constraints defined.", "Target audience defined with knowledge level implied."])
    suggestions: str = Field(..., example="This is a refactored version of the original prompt, addressing the improvement reasons provided.")
    model_name: str = Field(..., example="gemini-2.0-flash")