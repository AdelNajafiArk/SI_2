from openai import OpenAI
from pydantic import BaseModel
import json

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

class Pet(BaseModel):
    name: str
    animal: str
    age: int
    color: str | None = None
    favorite_toy: str | None = None

class PetList(BaseModel):
    pets: list[Pet]

schema = PetList.model_json_schema()

text = """Luna is a 3-year-old black cat who loves feather toys. 
Loki is a 5-year-old orange cat who prefers laser pointers."""

response = client.chat.completions.create(
    model="qwen3.5:2b",
    messages=[{
        "role": "user",
        "content": f"Extract pets as JSON: {json.dumps(schema)}\n\nText: {text}"
    }],
    response_format={"type": "json_schema", "json_schema": {"schema": schema}},
    temperature=0,
    extra_body={"options": {"num_gpu": 99}}
)

pets = PetList.model_validate_json(response.choices[0].message.content)
for pet in pets.pets:
    print(f"{pet.name}: {pet.animal}, age {pet.age}, color {pet.color}")