from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

prompt = """Solve this problem using the following structure:

1. Restate the problem in your own words.
2. List knowns and unknowns.
3. Show the calculation.
4. Verify by checking.
5. State the final answer.

Problem: A company's revenue increased by 25% to $500,000. What was the original revenue?"""

response = client.chat.completions.create(
    model="qwen3.5:2b",
    messages=[{"role": "user", "content": prompt}],
    temperature=0,
    extra_body={"options": {"num_gpu": 99}}
)
print(response.choices[0].message.content)