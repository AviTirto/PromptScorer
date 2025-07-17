from app.core.gemini_client import gemini_client
from app.core.criterias import CONSISTENCY_JUDGE_SYSTEM_PROMPT
from app.schemas.gemini import JudgeScoredResponse

def consistency_judge(prompt: str) -> JudgeScoredResponse:
    response = gemini_client.generate_scored_content(prompt, CONSISTENCY_JUDGE_SYSTEM_PROMPT)
    return JudgeScoredResponse(score=response.score, reason=response.reason)