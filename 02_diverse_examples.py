from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def select_diverse_examples(candidates: list[str], k: int = 3) -> list[str]:
    """Greedily pick k examples that are maximally dissimilar from each other."""
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(candidates)
    sim = cosine_similarity(vectors)
    
    selected = [0]
    while len(selected) < k:
        remaining = [i for i in range(len(candidates)) if i not in selected]
        scores = [(i, 1 - max(sim[i][j] for j in selected)) for i in remaining]
        selected.append(max(scores, key=lambda x: x[1])[0])
    return [candidates[i] for i in selected]

# Example: meeting action item extraction
candidates = [
    "Sarah will send the report by Friday.",
    "Sarah will email the report on Friday.",  # near-duplicate
    "The budget question is still unresolved.",
    "Tom will schedule the follow-up meeting.",
]

diverse = select_diverse_examples(candidates, k=3)
print("Selected examples:")
for ex in diverse:
    print(" -", ex)