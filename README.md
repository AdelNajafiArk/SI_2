# Day 2 — Advanced Prompt Engineering

Practice with four core prompt patterns using Ollama + qwen3.5:4b (local, free).

## What's Covered

1. **Few-Shot Prompting** — teach by example
2. **Structured Output** — JSON schema enforcement
3. **Chain-of-Thought** — step-by-step reasoning
4. **Persona Prompting** — role-based behavior

## Files

| File | Purpose |
|------|---------|
| `01_zero_vs_few.py` | Compare zero-shot vs few-shot |
| `02_diverse_examples.py` | Diversity-aware example selection |
| `03_few_shot_cot.py` | Few-shot chain-of-thought |
| `04_json_mode.py` | Basic JSON output |
| `05_structured_output.py` | Schema-enforced output |
| `06_extraction.py` | Structured data extraction |
| `07_pydantic.py` | Pydantic-validated output |
| `08_zero_shot_cot.py` | CoT improves reasoning |
| `09_structured_cot.py` | Structured CoT template |
| `10_role_prompting.py` | Persona-based prompting |
| `11_persona_constraints.py` | Persona + hard rules |
| `12_test_library.py` | Tests the prompt library |
| `prompt_lib/` | Reusable prompt templates |

## Setup

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install openai pydantic scikit-learn