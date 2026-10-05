from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

system_prompt = """You are a senior SQL reviewer at a fintech company.

Rules:
- Always point out potential SQL injection risks.
- Suggest indexes where queries might be slow.
- Keep responses under 150 words.
- Use code blocks for SQL.
- Never approve a query with SELECT * in production code."""

query = """SELECT * FROM users WHERE email = 'user@example.com' AND status = 'active';"""

response = client.chat.completions.create(
    model="qwen3.5:2b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Review this query:\n{query}"}
    ],
    temperature=0,
    extra_body={"options": {"num_gpu": 99}}
)
print(response.choices[0].message.content)