from openai import OpenAI
import json

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

schema = {
    "type": "object",
    "properties": {
        "pets": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "animal": {"type": "string"},
                    "age": {"type": "integer"},
                    "color": {"type": ["string", "null"]},
                    "favorite_toy": {"type": ["string", "null"]}
                },
                "required": ["name", "animal", "age"]
            }
        }
    },
    "required": ["pets"]
}

text = """I have two cats named Luna and Loki. 
Luna is 3 years old, black, and loves feather toys. 
Loki is 5, orange, and prefers laser pointers."""

response = client.chat.completions.create(
    model="qwen3.5:2b",
    messages=[{
        "role": "user",
        "content": f"Extract pet information as JSON matching this schema: {json.dumps(schema)}\n\nText: {text}"
    }],
    response_format={"type": "json_schema", "json_schema": {"schema": schema}},
    temperature=0,
    extra_body={"options": {"num_gpu": 99}}
)

result = json.loads(response.choices[0].message.content)
print(json.dumps(result, indent=2))