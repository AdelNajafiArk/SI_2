from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# Generic
generic = client.chat.completions.create(
    model="qwen3.5:2b",
    messages=[{"role": "user", "content": "Explain what a database index is."}],
    temperature=0,
    extra_body={"options": {"num_gpu": 99}}
)

# Role-primed
role = client.chat.completions.create(
    model="qwen3.5:2b",
    messages=[
        {"role": "system", "content": "You are a senior database administrator with 15 years of experience. You explain concepts using concrete examples and warn about common pitfalls."},
        {"role": "user", "content": "Explain what a database index is."}
    ],
    temperature=0,
    extra_body={"options": {"num_gpu": 99}}
)

print("GENERIC:\n", generic.choices[0].message.content[:400])
print("\nROLE-PRIMED:\n", role.choices[0].message.content[:400])