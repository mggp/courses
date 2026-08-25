"""Lesson 11 — compare retrieval shapes and chunking strategies offline.

Run from this directory:
    uv sync
    uv run retrieval_architecture.py
    uv run retrieval_architecture.py --query "What controls limit exposure?"
    uv run retrieval_architecture.py --show-chunks

The keyword ranking is a deliberately small proxy. It is not a vector index,
graph database, or production semantic chunker. The point is to inspect the
architecture choice and the chunk boundaries before adding those dependencies.
"""

from __future__ import annotations

import argparse
import re
from collections.abc import Iterable


DOCUMENT = """
Ownership and control. Northstar Holdings owns 80 percent of Meridian Finance.
Meridian Finance owns the voting shares of Harbor Credit. The filing names
Elena Ruiz as the beneficial owner of Northstar Holdings. These ownership edges
form a path from Elena Ruiz to Harbor Credit through Northstar and Meridian.

Quarterly revenue. Northstar reported revenue of 42 million euros in Q4.
Meridian Finance reported revenue of 11 million euros in Q4. The figures are
reported in the quarterly filing and should be cited at the claim level.

Risk controls. The credit policy requires a human review when aggregate exposure
exceeds 10 million euros. The policy also requires an audit record for every
override and prohibits automatic approval when ownership data is incomplete.
""".strip()

OWNERSHIP_EDGES = [
    ("Elena Ruiz", "BENEFICIAL_OWNER_OF", "Northstar Holdings", "p1"),
    ("Northstar Holdings", "OWNS_80_PERCENT_OF", "Meridian Finance", "p2"),
    ("Meridian Finance", "OWNS_VOTING_SHARES_OF", "Harbor Credit", "p3"),
]

SOURCE_PASSAGES = {
    "p1": "Elena Ruiz is the beneficial owner of Northstar Holdings.",
    "p2": "Northstar Holdings owns 80 percent of Meridian Finance.",
    "p3": "Meridian Finance owns the voting shares of Harbor Credit.",
}

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "be",
    "by",
    "for",
    "from",
    "in",
    "is",
    "of",
    "on",
    "or",
    "the",
    "this",
    "to",
    "what",
    "which",
    "with",
}

RELATION_TERMS = {
    "beneficial",
    "controlled",
    "edges",
    "linked",
    "owns",
    "ownership",
    "path",
    "relationship",
    "relationships",
    "shares",
    "subsidiary",
    "ultimately",
}

EVIDENCE_TERMS = {
    "cite",
    "cited",
    "citation",
    "document",
    "evidence",
    "filing",
    "policy",
    "reported",
    "supports",
}


def content_words(text: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {word for word in words if word not in STOPWORDS}


def sentences(text: str) -> list[str]:
    normalized = " ".join(text.split())
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", normalized) if part.strip()]


def fixed_size_chunks(text: str, size: int, overlap: int) -> list[str]:
    """Split by word count with deterministic overlap."""
    if size <= 0:
        raise ValueError("size must be positive")
    if not 0 <= overlap < size:
        raise ValueError("overlap must be non-negative and smaller than size")

    words = text.split()
    step = size - overlap
    chunks = []
    for start in range(0, len(words), step):
        chunks.append(" ".join(words[start : start + size]))
        if start + size >= len(words):
            break
    return chunks


def jaccard(left: Iterable[str], right: Iterable[str]) -> float:
    left_set, right_set = set(left), set(right)
    if not left_set and not right_set:
        return 1.0
    return len(left_set & right_set) / len(left_set | right_set)


def semantic_chunks(text: str, max_words: int, threshold: float) -> list[str]:
    """Group nearby sentences while their content vocabulary remains similar.

    Real semantic chunkers commonly use embeddings or a model-derived distance.
    This deterministic Jaccard proxy exists only to make boundary changes
    visible in an offline exercise.
    """
    if max_words <= 0:
        raise ValueError("max_words must be positive")
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")

    chunks: list[str] = []
    current: list[str] = []
    current_words: set[str] = set()

    raw_sentences = sentences(text)
    semantic_units: list[str] = []
    index = 0
    while index < len(raw_sentences):
        sentence = raw_sentences[index]
        # Keep short section labels with the first sentence under that label.
        if len(sentence.split()) <= 4 and index + 1 < len(raw_sentences):
            semantic_units.append(f"{sentence} {raw_sentences[index + 1]}")
            index += 2
        else:
            semantic_units.append(sentence)
            index += 1

    for sentence in semantic_units:
        sentence_words = sentence.split()
        sentence_content = content_words(sentence)
        too_large = current and len(current) + len(sentence_words) > max_words
        topic_changed = current and jaccard(current_words, sentence_content) < threshold
        if too_large or topic_changed:
            chunks.append(" ".join(current))
            current = []
            current_words = set()
        current.extend(sentence_words)
        current_words.update(sentence_content)

    if current:
        chunks.append(" ".join(current))
    return chunks


def keyword_rank(query: str, chunks: list[str], limit: int = 3) -> list[tuple[float, str]]:
    """Use lexical overlap as a transparent stand-in for dense retrieval."""
    query_words = content_words(query)
    scored = []
    for chunk in chunks:
        chunk_words = content_words(chunk)
        score = len(query_words & chunk_words) / max(len(query_words), 1)
        scored.append((score, chunk))
    return sorted(scored, key=lambda item: (-item[0], item[1]))[:limit]


def recommend_architecture(query: str) -> tuple[str, str]:
    words = content_words(query)
    has_relationship = bool(words & RELATION_TERMS)
    needs_evidence = bool(words & EVIDENCE_TERMS)

    if has_relationship and needs_evidence:
        return (
            "HYBRID",
            "Traverse explicit relationships, then retrieve the source text needed to support the answer.",
        )
    if has_relationship:
        return (
            "GRAPH",
            "The question asks for explicit entities, edges, paths, or ownership constraints.",
        )
    return (
        "VECTOR",
        "The question is primarily about finding semantically related evidence in text.",
    )


def show_chunks(label: str, chunks: list[str]) -> None:
    print(f"\n{label.upper()} ({len(chunks)} chunks)")
    for index, chunk in enumerate(chunks, start=1):
        print(f"  [{index}] {len(chunk.split()):>2} words — {chunk}")


def show_ownership_example() -> None:
    print("\nOWNERSHIP EXAMPLE")
    print("  GRAPH PATH")
    for subject, relation, object_, source_id in OWNERSHIP_EDGES:
        print(f"    {subject} --{relation}--> {object_}  [{source_id}]")
    print("  SOURCE PASSAGES")
    for source_id, passage in SOURCE_PASSAGES.items():
        print(f"    [{source_id}] {passage}")
    print("  The graph establishes the path; the passages provide evidence and citations.")
    print("  Apply a domain rule before calling the path 'ultimate control'.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect vector/graph choices and chunk boundaries.")
    parser.add_argument(
        "--query",
        default="Which companies are ultimately controlled by Northstar, and which filing supports that link?",
        help="question to classify and use for the toy lexical ranking",
    )
    parser.add_argument("--fixed-size", type=int, default=28, help="word limit for fixed-size chunks")
    parser.add_argument("--overlap", type=int, default=5, help="overlap between fixed-size chunks")
    parser.add_argument("--semantic-max", type=int, default=40, help="word limit for semantic chunks")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.08,
        help="content-vocabulary similarity needed to keep adjacent sentences together",
    )
    parser.add_argument("--show-chunks", action="store_true", help="print every chunk")
    args = parser.parse_args()

    architecture, reason = recommend_architecture(args.query)
    fixed = fixed_size_chunks(DOCUMENT, args.fixed_size, args.overlap)
    semantic = semantic_chunks(DOCUMENT, args.semantic_max, args.threshold)

    print(f"QUERY: {args.query}")
    print(f"RETRIEVAL SHAPE: {architecture}")
    print(f"WHY: {reason}")
    print("\nVECTOR / GRAPH REMINDER")
    print("  vector: nearest semantic evidence in an embedding space")
    print("  graph:  explicit nodes, edges, properties, and traversable paths")
    print("  hybrid: graph structure plus vector-retrieved source evidence")

    if architecture in {"GRAPH", "HYBRID"}:
        show_ownership_example()

    if args.show_chunks:
        show_chunks("fixed-size chunks", fixed)
        show_chunks("semantic chunks", semantic)
    else:
        print(f"\nFIXED-SIZE: {len(fixed)} chunks")
        print(f"SEMANTIC:   {len(semantic)} chunks")
        print("Use --show-chunks to inspect the boundaries.")

    print("\nTOY LEXICAL RANKING (not embeddings)")
    for score, chunk in keyword_rank(args.query, semantic):
        print(f"  {score:.2f} — {chunk}")

    print("\nEVALUATION PLAN")
    print("  Keep the corpus, embedding model, retriever, k, and generator fixed.")
    print("  Change only the chunker, then measure recall@k, precision@k, faithfulness, latency, and index size.")
    print("  A coherent chunk is a hypothesis; the held-out results decide whether it helps.")


if __name__ == "__main__":
    main()
