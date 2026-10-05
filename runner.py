"""Run prompt templates against Ollama."""

import json
from openai import OpenAI
from . import templates  # noqa: F401

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")


def run(template: str, temperature: float = 0, **kwargs) -> str:
    """Render a template and call Ollama."""
    prompt = template.format(**kwargs)
    response = client.chat.completions.create(
        model="qwen3.5:4b",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()


def run_with_system(system: str, user: str, temperature: float = 0) -> str:
    """Call with system + user messages."""
    response = client.chat.completions.create(
        model="qwen3.5:2b",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()


def run_structured(prompt: str, schema: dict, temperature: float = 0):
    """Run with JSON schema enforcement."""
    response = client.chat.completions.create(
        model="qwen3.5:2b",
        messages=[
            {
                "role": "user",
                "content": f"{prompt}\n\nReturn JSON matching: {json.dumps(schema)}",
            }
        ],
        response_format={"type": "json_schema", "json_schema": {"schema": schema}},
        temperature=temperature,
    )
    return json.loads(response.choices[0].message.content)