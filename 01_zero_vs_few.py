from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# Zero-shot: just instruction
zero_shot_prompt = """Classify the sentiment of each review.

Review: "The product arrived damaged and support was unhelpful."
Sentiment:"""

# Few-shot: with examples
few_shot_prompt = """Classify the sentiment of each review.

Review: "Arrived fast, works great!"
Sentiment: Positive

Review: "Broke in two days, waste of money."
Sentiment: Negative

Review: "It's okay, nothing special."
Sentiment: Neutral

Review: "The product arrived damaged and support was unhelpful."
Sentiment:"""

def call(prompt):
    response = client.chat.completions.create(
        model="qwen3.5:2b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        extra_body={"options": {"num_gpu": 99}}
    )
    return response.choices[0].message.content.strip()

print("ZERO-SHOT:", call(zero_shot_prompt))
print("FEW-SHOT:", call(few_shot_prompt))