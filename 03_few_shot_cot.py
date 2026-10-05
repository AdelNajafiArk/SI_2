from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

prompt = """Solve each problem step by step, then give the final answer.

Q: A store sells 5 books at $12 each. What's the total?
Reasoning: 5 books × $12 = $60.
Answer: $60

Q: A train travels 120 km in 2 hours. What's its speed?
Reasoning: Speed = distance / time = 120 / 2 = 60 km/h.
Answer: 60 km/h

Q: A shirt costs $25. It's 20% off. What's the final price?
Reasoning: Discount = 25 × 0.20 = $5. Final price = 25 - 5 = $20.
Answer: $20

Q: A recipe needs 3 cups of flour for 12 cookies. How much for 30 cookies?
Reasoning:"""

response = client.chat.completions.create(
    model="qwen3.5:2b",
    messages=[{"role": "user", "content": prompt}],
    temperature=0,
    extra_body={"options": {"num_gpu": 99}}
)
print(response.choices[0].message.content)