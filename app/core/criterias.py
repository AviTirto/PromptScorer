GRADING_CRITERIA_SYSTEM_PROMPT = """
| Dimensions/Score | Excellent = 5 | Great = 4 | Good = 3 | Poor = 2 | Unacceptable = 1 |
| --- | --- | --- | --- | --- | --- |
| Clarity | - Flesch Reading Ease appropriate for audience. 
- Uses only specific action verbs ("analyze," "summarize," "calculate") with no vague terms.
- Every instruction has clear subject-object relationships with no ambiguity.
 - Zero ambiguous pronouns or adjectives; all references are explicit.
- Clear beginning (context/setup), middle (main instructions), and end (output requirements).
- Well-structured with clear sections and transitions. | - Appropriate reading level with minor deviations.
-  Mostly specific action verbs with 1-2 vague terms.
- Clear subject-object relationships.
- Minimal ambiguous pronouns or adjectives; all references are explicit.
- Good beginning-middle-end with slight organizational issues.
-  Good structure and transitions with minor ambiguities.  | - Reading ease  appropriate but inconsistent.
- Mix of vague verbs and actions verbs.
- Somehwhat clear subject-object relationships.
- Several ambiguous pronouns or adjectives
- Some organization but inconsistent.
- Transitions present but often unclear | - Reading ease inappropriate for audience level.
-Predominantly vague verbs ("help," "deal with").
- Multiple unclear subject-object relationships.
- Poor structure with confusing transitions.
 | - Riddled with multiple spelling/grammatical errors. 
- Instructions are incomprehensible or contradictory. 
- Pervasive use of ambiguous language that prevents understanding.
- No clear structure.  |
| Specificity | - Highly detailed task definition with all parameters specified.
- Complete context including all prerequisites and assumptions.
-  Includes relevant examples or templates for all outputs.
- All format, process, content, and quality constraints clearly defined.
- Target user, knowledge level, and decision-making needs all clearly defined | - Well-defined tasks with most parameters specified.
- Decent amount of context provided.
- Examples or templates given for majority of the ouptuts.
-  Most constraints defined.
- Target audience defined with knowledge level implied | -  Basic tasks definition with key parameters defined.
- Missing context to execute the tasks.
-Examples or templates missing.
- Basic constraints provided.
- General audience indication. | - Vague task definition with minimal constraints, or success criteria.
- Limited context.
- Unclear audience. | - Extremely vague with no clear task boundaries, constraints, or success criteria. 
- No meaningful context provided. 
- No audience consideration. |
| Complexity | - Complexity perfectly matched to task requirements. 
- Optimal cognitive load with well-balanced memory requirements, processing steps, and decision points.  
- Clear integration pathways. | - Complexity appropriate with minor areas of unnecessary complication or oversimplification. Generally well-balanced cognitive demands.
- Integration pathways present for most tasks. | - Acceptable complexity level but some imbalance - either unnecessarily complex for simple tasks or oversimplified for complex ones.  | - Poor complexity calibration. 
- Either overwhelming with too many simultaneous variables and decisions, or severely underspecified for the task needs. | - Completely miscalibrated complexity. 
- Either cognitively overwhelming with excessive memory load and integration requirements, or so oversimplified it cannot achieve the goal.
- No consideration of mental processing requirements |
| Completeness | - Comprehensive situation context (who/what/when/where/why)
- Clear task definition with success criteria.
- Detailed action steps with methodology.
-  Exact output format specified. All required elements listed. | - Most essential information included. Minor gaps in context or specifications that don't significantly impact execution.
- Goal and success mostly defined.
- Most steps and requirements specified.
- Format and content well-defined with minor gaps | - Core information present but missing some important details.
- Basic goal stated.
- Key steps outlined but missing other major steps.
- Basic output requirements. | - Significant gaps in essential information.
- Significant gaps in essential information. | - Critical information missing. 
- Lacks fundamental elements needed for task execution. 
- No clear situation, task definition, methodology, or expected results. |
| Consistency | -  No contradictions between any instructions.
- Perfect match between stated goals and detailed instructions.
-  Uniform terminology throughout.
- Produces stable, reproducible outputs across multiple executions. | - Minor logical inconsistencies that don't affect understanding.
- Good goal-instruction alignment with slight deviations.
- Minor terminology shifts.
- Produces relatively stable, reproducible outputs across multiple executions. | - Some inconsistencies requiring clarification, affects understanding.
- General goal-instruction alignment with gaps.
- Occasional terminology switches.
- Outputs mostly stable but some variation in structure/content. | - Notable inconsistencies in logic, terminology, or tone.
- Conflicting instructions or misaligned goals.
- Outputs unstable and unpredictable. | - Severe internal contradiction.
- Goals and instructions completely misaligned.
- No terminological or stylistic consistency.
- Outputs highly unstable and unpredictable. |
"""

SUGGESTION_SYSTEM_PROMPT = """
You are an expert content editor. Your task is to provide specific, actionable suggestions for improving text.
You will be given the original text and a list of reasons for its current score.
For each suggestion, identify the specific 1-based line number that needs modification and provide the fully updated line.
Only provide suggestions for lines that need changes. If a line is perfect, do not include it in the output.

Your output MUST be a JSON array of objects. Each object MUST have two keys: "line_number" (integer) and "suggested_text" (string).
Example:
[
  {"line_number": 1, "suggested_text": "This is the updated first line."},
  {"line_number": 3, "suggested_text": "The third line now looks like this."}
]
"""