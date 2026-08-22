"""faithfulness.py — does the generated answer stick to the retrieved context?

Lessons 1-4 measured retrieval: "did the right chunk come back?" This lesson
measures the answer itself: "did the text the model wrote stay inside the chunk
it was given?" The two are independent — a perfect retriever can still feed a
hallucinating generator.

Mechanic, in three steps (FActScore arXiv:2305.14251; RAGAS arXiv:2309.15217):
  1. decompose the answer into atomic statements
  2. check each statement against the retrieved context with an NLI model
     (entailment = supported; neutral / contradiction = unsupported)
  3. faithfulness = supported statements / total statements

Run:  uv run faithfulness.py          # NLI-check the canned cases
      uv run faithfulness.py --live   # decompose answers with an LLM first
                                       # (needs OPENAI_API_KEY, optional OPENAI_BASE_URL)
"""
import argparse
import json
import os

from sentence_transformers import CrossEncoder

CORPUS = "corpus.md"
NLI_MODEL = "cross-encoder/nli-MiniLM2-L6-H768"
NLI_LABELS = ["contradiction", "entailment", "neutral"]

# Each case is a (question, retrieved context, generated answer) triple plus the
# hand-written decomposition of the answer into atomic statements. The context
# ids are the GOLD chunks — retrieval is assumed to have done its job here, so
# the only thing being measured is whether the answer stays inside that context.
CASES = [
    {
        "name": "faithful",
        "question": "What does the tutor do when it cannot find an answer?",
        "context_ids": ["p9"],
        "answer": "The tutor says it does not know rather than guessing when no chunk is close enough.",
        "statements": [
            "The tutor says it does not know rather than guessing.",
        ],
    },
    {
        "name": "hallucination-sneaks-in",
        "question": "What does the tutor do when it cannot find an answer?",
        "context_ids": ["p9"],
        "answer": "The tutor says it does not know rather than guessing, and when it is unsure it emails the support team for help.",
        "statements": [
            "The tutor says it does not know rather than guessing.",
            "When it is unsure, the tutor emails the support team for help.",
        ],
    },
    {
        "name": "right-chunk-wrong-claim",
        "question": "When will a word be reviewed next?",
        "context_ids": ["p6"],
        "answer": "A word is reviewed next whenever the learner manually requests a review.",
        "statements": [
            "A word is reviewed next whenever the learner manually requests a review.",
        ],
    },
    {
        "name": "compliance-polarity-flip",
        "question": "Does Lingua store audio recordings of learners?",
        "context_ids": ["p10"],
        "answer": "Lingua stores audio recordings of learners for quality review.",
        "statements": [
            "Lingua stores audio recordings of learners for quality review.",
        ],
    },
]

LIVE_PROMPT = (
    "You are an answer auditor for a retrieval-augmented system.\n"
    "Break the following answer into a list of atomic claims. Each claim must\n"
    "be a single verifiable statement with no conjunctions. Return JSON only:\n"
    '  {{"claims": ["claim one", "claim two"]}}\n'
    "Answer: {answer}"
)


def chunk_lookup(text):
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    return {f"p{i}": p for i, p in enumerate(paras)}


def live_decompose(answer):
    from openai import OpenAI

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),
                    base_url=os.environ.get("OPENAI_BASE_URL"))
    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
    reply = client.chat.completions.create(
        model=model,
        messages=[{"role": "user",
                   "content": LIVE_PROMPT.format(answer=answer)}],
        response_format={"type": "json_object"},
    )
    return json.loads(reply.choices[0].message.content)["claims"]


def main():
    parser = argparse.ArgumentParser(description="Faithfulness of generated answers.")
    parser.add_argument("--live", action="store_true",
                        help="decompose answers with an LLM instead of the canned statements")
    args = parser.parse_args()

    text = open(CORPUS, encoding="utf-8").read()
    chunks = chunk_lookup(text)

    print(f"loading NLI model {NLI_MODEL} (first run downloads ~130MB)")
    nli = CrossEncoder(NLI_MODEL)

    print(f"checking {len(CASES)} cases  |  decomposition: "
          f"{'live LLM' if args.live else 'canned'}\n")

    grand_supported = 0
    grand_total = 0
    for case in CASES:
        statements = live_decompose(case["answer"]) if args.live else case["statements"]
        context = " ".join(chunks[cid] for cid in case["context_ids"])
        verdicts = [NLI_LABELS[int(nli.predict([(context, s)])[0].argmax())]
                    for s in statements]
        supported = sum(1 for v in verdicts if v == "entailment")
        grand_supported += supported
        grand_total += len(statements)

        print(f"[{case['name']}]  Q: {case['question']}")
        print(f"    context ({','.join(case['context_ids'])}): {context}")
        print(f"    answer: {case['answer']}")
        for s, v in zip(statements, verdicts):
            mark = "SUPPORTED" if v == "entailment" else ("NOT IN CONTEXT" if v == "neutral" else "CONTRADICTED")
            print(f"      {mark:<14s} {s}")
        print(f"    faithfulness: {supported}/{len(statements)} = {supported/len(statements):.2f}\n")

    print(f"overall faithfulness: {grand_supported}/{grand_total} = "
          f"{grand_supported/grand_total:.2f}")


if __name__ == "__main__":
    main()
