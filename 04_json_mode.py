from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

response = client.chat.completions.create(
    model="qwen3.5:2b",
    messages=[{
        "role": "user",
        "content": "Tell me about Canada in JSON with name, capital, and languages."
    }],
    response_format={"type": "json_object"},
    extra_body={"options": {"num_gpu": 99}}
)
print(response.choices[0].message.content)