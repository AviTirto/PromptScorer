from app.schemas.gemini import ScoredResponse, JudgeScoredResponse
from app.core.judges.clarity_judge import clarity_judge
from app.core.judges.specificity_judge import specificity_judge
from app.core.judges.complexity_judge import complexity_judge
from app.core.judges.completeness_judge import completeness_judge
from app.core.judges.consistency_judge import consistency_judge

def master_judge(prompt: str) -> ScoredResponse:
    clarity: JudgeScoredResponse = clarity_judge(prompt)
    specificity: JudgeScoredResponse = specificity_judge(prompt)
    complexity: JudgeScoredResponse = complexity_judge(prompt)
    completeness: JudgeScoredResponse = completeness_judge(prompt)
    consistency: JudgeScoredResponse = consistency_judge(prompt)

    all_scores = [
        clarity.score,
        specificity.score,
        complexity.score,
        completeness.score,
        consistency.score
    ]
    avg_score = round(sum(all_scores) / len(all_scores))

    reasons = [
        f"Clarity: {clarity.reason}",
        f"Specificity: {specificity.reason}",
        f"Complexity: {complexity.reason}",
        f"Completeness: {completeness.reason}",
        f"Consistency: {consistency.reason}"
    ]

    return ScoredResponse(score=avg_score, reasons=reasons)
