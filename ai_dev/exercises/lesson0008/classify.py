"""classify.py — the same text vectors, two different contracts.

Retrieval:      question -> ranked source texts (no labels required)
Classification: ticket  -> one label from a fixed vocabulary (labels required)

The dataset is intentionally fictional Lingua support-ticket routing. It teaches
the mechanics of supervised classification, not fraud detection, credit risk, or
any production decision in a regulated domain.

Run:  uv run classify.py
      uv run classify.py --threshold 0.75
"""
import argparse
import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.metrics.pairwise import cosine_similarity

DATA = Path("tickets.json")
SEARCH_QUERY = "I was charged twice for premium and need a refund."
AMBIGUOUS_TICKET = "My card was charged twice and I cannot log in after changing phones."


def records_for(records, split):
    return [r for r in records if r["split"] == split]


def main():
    parser = argparse.ArgumentParser(description="Local text classification versus retrieval.")
    parser.add_argument("--threshold", type=float, default=0.60,
                        help="abstain below this maximum class probability (demo only)")
    args = parser.parse_args()

    records = json.loads(DATA.read_text(encoding="utf-8"))
    train = records_for(records, "train")
    test = records_for(records, "test")
    train_text = [r["text"] for r in train]
    train_label = [r["label"] for r in train]
    test_text = [r["text"] for r in test]
    test_label = [r["label"] for r in test]
    labels = sorted(set(train_label))

    # Same sparse TF-IDF vectors serve both tasks. Labels are the difference.
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)
    X_train = vectorizer.fit_transform(train_text)
    X_test = vectorizer.transform(test_text)

    print(f"train: {len(train)} labeled tickets  |  test: {len(test)} held-out tickets")
    print(f"labels: {', '.join(labels)}  |  TF-IDF features: {X_train.shape[1]}\n")

    print("RETRIEVAL — returns source texts, not a decision")
    query_vector = vectorizer.transform([SEARCH_QUERY])
    similarities = cosine_similarity(query_vector, X_train).ravel()
    print(f"  query: {SEARCH_QUERY}")
    for rank, i in enumerate(similarities.argsort()[::-1][:3], start=1):
        print(f"  {rank}. {similarities[i]:.3f}  [{train[i]['label']}] {train[i]['text']}")

    print("\nCLASSIFICATION — learns a fixed label vocabulary from examples")
    classifier = LogisticRegression(max_iter=1_000, random_state=0)
    classifier.fit(X_train, train_label)
    predicted = classifier.predict(X_test)
    macro_f1 = f1_score(test_label, predicted, labels=labels, average="macro")
    matrix = confusion_matrix(test_label, predicted, labels=labels)
    print(f"  held-out macro F1: {macro_f1:.2f}")
    print("  confusion matrix (rows=true, columns=predicted):")
    print(f"             {' '.join(f'{label:>8s}' for label in labels)}")
    for label, row in zip(labels, matrix):
        print(f"    {label:>8s} {' '.join(f'{n:8d}' for n in row)}")

    probabilities = classifier.predict_proba(vectorizer.transform([AMBIGUOUS_TICKET]))[0]
    ranked = sorted(zip(classifier.classes_, probabilities), key=lambda item: -item[1])
    label, confidence = ranked[0]
    action = label if confidence >= args.threshold else "needs_review"
    print("\nDECISION POLICY — probability estimate is not the action")
    print(f"  ticket: {AMBIGUOUS_TICKET}")
    print("  probabilities: " + ", ".join(f"{name}={score:.2f}" for name, score in ranked))
    print(f"  threshold: {args.threshold:.2f}  ->  action: {action}")
    print("  The threshold is a demonstration policy, not learned truth. Tune it on a "
          "separate validation set against the cost of each error — never on this test set.")


if __name__ == "__main__":
    main()
