from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

problem = """A bat and a ball cost $1.10 together. 
The bat costs $1.00 more than the ball. 
How much does the ball cost?"""

# Without CoT
response_no_cot = client.chat.completions.create(
    model="qwen3.5:2b",
    messages=[{"role": "user", "content": problem}],
    temperature=0,
    extra_body={"options": {"num_gpu": 99}}
)

# With CoT
response_cot = client.chat.completions.create(
    model="qwen3.5:2b",
    messages=[{"role": "user", "content": problem + "\n\nLet's think step by step."}],
    temperature=0,
    extra_body={"options": {"num_gpu": 99}}
)

print("WITHOUT CoT:", response_no_cot.choices[0].message.content.strip()[:200])
print("\nWITH CoT:", response_cot.choices[0].message.content.strip()[:300])