"""Test the prompt template library."""

import sys
import os

# Add the day2 directory to sys.path so `prompt_lib` can be imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompt_lib import templates, runner


def test_sentiment():
    print("=" * 60)
    print("TEST 1: Sentiment classification")
    print("=" * 60)
    result = runner.run(templates.SENTIMENT_FEW_SHOT, text="This is amazing!")
    print("Result:", result)
    print()


def test_extraction():
    print("=" * 60)
    print("TEST 2: Action item extraction")
    print("=" * 60)
    transcript = (
        "Sarah: I'll send the report by Friday.\n"
        "Tom: The budget question is still open.\n"
        "Sarah: Actually, let me handle the budget too.\n"
    )
    result = runner.run(templates.EXTRACT_ACTION_ITEMS, transcript=transcript)
    print("Result:\n", result)
    print()


def test_math():
    print("=" * 60)
    print("TEST 3: Step-by-step math")
    print("=" * 60)
    result = runner.run(
        templates.MATH_STEP_BY_STEP, problem="If 3x + 7 = 22, what is x?"
    )
    print("Result:\n", result)
    print()


def test_code_review():
    print("=" * 60)
    print("TEST 4: Code review")
    print("=" * 60)
    code = (
        "def get_user(user_id):\n"
        "    query = 'SELECT * FROM users WHERE id = ' + user_id\n"
        "    return db.execute(query)\n"
    )
    result = runner.run(
        templates.CODE_REVIEWER, language="python", code=code
    )
    print("Result:\n", result)
    print()


if __name__ == "__main__":
    test_sentiment()
    test_extraction()
    test_math()
    test_code_review()