"""Reusable prompt templates."""

# ============ CLASSIFICATION ============
SENTIMENT_FEW_SHOT = """Classify sentiment. Reply ONLY with Positive, Negative, or Neutral.

Review: "Arrived fast, works great!" → Positive
Review: "Broke in two days." → Negative
Review: "It's okay, nothing special." → Neutral

Review: "{text}" →"""

# ============ EXTRACTION ============
EXTRACT_ACTION_ITEMS = """Extract action items from the transcript below.

Rules:
- One item per line
- Format: [Owner] - [Task] - [Deadline if stated]
- If no owner is confirmed, write UNASSIGNED
- If no deadline is stated, write NO_DEADLINE

Transcript:
{transcript}

Action items:"""

# ============ REASONING ============
MATH_STEP_BY_STEP = """Solve step by step.

1. Restate the problem.
2. List knowns and unknowns.
3. Show calculation.
4. Final answer on the last line, prefixed with "ANSWER:".

Problem: {problem}"""

# ============ ROLE-BASED ============
CODE_REVIEWER = """You are a senior code reviewer. Review the code below.

Check for:
- Security issues
- Performance bottlenecks
- Readability problems
- Missing error handling

Code:
```{language}
{code}"""