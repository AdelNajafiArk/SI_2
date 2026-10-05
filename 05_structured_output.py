from openai import OpenAI
import json

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "capital": {"type": "string"},
        "languages": {"type": "array", "items": {"type": "string"}},
        "population_millions": {"type": "number"}
    },
    "required": ["name", "capital", "languages"]
}

response = client.chat.completions.create(
    model="qwen3.5:2b",
    messages=[{
        "role": "user",
        "content": "Tell me about Canada. Return JSON matching this schema: " + json.dumps(schema)
    }],
    response_format={"type": "json_schema", "json_schema": {"schema": schema}},
    temperature=0,
    extra_body={"options": {"num_gpu": 99}}
)

result = json.loads(response.choices[0].message.content)
print(json.dumps(result, indent=2))