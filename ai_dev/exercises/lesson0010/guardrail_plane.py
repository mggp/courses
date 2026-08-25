"""guardrail_plane.py — a tiny, fail-closed control plane.

This exercise is intentionally deterministic and offline. It models the
application checks around an LLM response; it does not pretend that string
matching is a production faithfulness evaluator.

Run:
    uv run guardrail_plane.py
    uv run guardrail_plane.py --scenario risky
    uv run guardrail_plane.py --scenario clean --approve
    uv run guardrail_plane.py --temperature 0.7 --top-p 0.85
"""

from __future__ import annotations

import argparse
import math
from typing import Any


CONTEXT = {
    "p1": (
        "The ticket contains billing and access signals. "
        "Mixed billing and access signals require human review."
    )
}

SCENARIOS: dict[str, dict[str, Any]] = {
    "clean": {
        "decision": "needs_review",
        "claims": [
            {
                "text": "The ticket contains billing and access signals.",
                "citation": "p1",
            },
            {
                "text": "Mixed billing and access signals require human review.",
                "citation": "p1",
            },
        ],
        "tool_call": {
            "name": "route_to_human",
            "arguments": {"ticket_id": "T-42"},
        },
    },
    "risky": {
        "decision": "approved",
        "claims": [
            {
                "text": "The ticket contains billing and access signals.",
                "citation": "p1",
            },
            {
                "text": "Mixed billing and access signals may be auto-approved.",
                "citation": "p1",
            },
        ],
        "tool_call": {
            "name": "approve_ticket",
            "arguments": {"ticket_id": "T-42"},
        },
    },
}

TOOLS = {
    "route_to_human": {
        "description": "Route the ticket to a human reviewer.",
        "allowed": True,
        "requires_approval": True,
    },
    "approve_ticket": {
        "description": "Approve the ticket without human review.",
        "allowed": False,
        "requires_approval": False,
    },
}

LOGITS = {
    "needs_review": 3.0,
    "route_to_human": 2.4,
    "ask_question": 1.5,
    "approve_ticket": 0.4,
    "invent_detail": 0.0,
}


def validate_schema(answer: dict[str, Any]) -> tuple[bool, str]:
    required = {"decision", "claims", "tool_call"}
    if set(answer) != required:
        return False, "response keys do not match the output schema"
    if not isinstance(answer["decision"], str):
        return False, "decision must be a string"
    if not isinstance(answer["claims"], list) or not answer["claims"]:
        return False, "claims must be a non-empty list"
    for claim in answer["claims"]:
        if set(claim) != {"text", "citation"}:
            return False, "each claim needs text and citation"
        if not all(isinstance(claim[key], str) for key in ("text", "citation")):
            return False, "claim fields must be strings"
    tool_call = answer["tool_call"]
    if set(tool_call) != {"name", "arguments"} or not isinstance(tool_call["name"], str):
        return False, "tool_call must contain a name and arguments"
    if not isinstance(tool_call["arguments"], dict):
        return False, "tool arguments must be an object"
    return True, "shape is valid"


def check_claims(answer: dict[str, Any]) -> tuple[bool, str]:
    failures = []
    for claim in answer["claims"]:
        source = CONTEXT.get(claim["citation"])
        if source is None:
            failures.append(f"missing citation {claim['citation']}")
        elif claim["text"] not in source:
            failures.append(f"unsupported claim: {claim['text']}")
    if failures:
        return False, "; ".join(failures)
    return True, f"{len(answer['claims'])}/{len(answer['claims'])} claims supported"


def check_tool(answer: dict[str, Any], approved: bool) -> tuple[bool, str]:
    call = answer["tool_call"]
    spec = TOOLS.get(call["name"])
    if spec is None:
        return False, f"unknown tool: {call['name']}"
    if not spec["allowed"]:
        return False, f"policy does not allow {call['name']}"
    if spec["requires_approval"] and not approved:
        return False, f"{call['name']} requires human approval"
    return True, f"{call['name']} authorized"


def run_control_plane(scenario: str, approved: bool) -> None:
    answer = SCENARIOS[scenario]
    checks = [
        ("schema", validate_schema(answer)),
        ("claim grounding", check_claims(answer)),
        ("tool authorization", check_tool(answer, approved)),
    ]

    print(f"SCENARIO: {scenario}")
    print(f"  proposed decision: {answer['decision']}")
    print(f"  proposed tool: {answer['tool_call']['name']}")
    print("\nCONTROL PLANE")
    all_passed = True
    for name, (passed, message) in checks:
        marker = "PASS" if passed else "FAIL"
        print(f"  {name:<18} {marker:<4} — {message}")
        all_passed = all_passed and passed

    if all_passed:
        print("\nDECISION: PASS — the candidate may proceed.")
    else:
        print("\nDECISION: ABSTAIN — do not execute; escalate or repair the candidate.")


def softmax(logits: dict[str, float], temperature: float) -> dict[str, float]:
    scaled = {name: value / temperature for name, value in logits.items()}
    maximum = max(scaled.values())
    weights = {name: math.exp(value - maximum) for name, value in scaled.items()}
    total = sum(weights.values())
    return {name: weight / total for name, weight in weights.items()}


def nucleus(probabilities: dict[str, float], top_p: float) -> list[tuple[str, float]]:
    ranked = sorted(probabilities.items(), key=lambda item: -item[1])
    kept: list[tuple[str, float]] = []
    cumulative = 0.0
    for name, probability in ranked:
        kept.append((name, probability))
        cumulative += probability
        if cumulative >= top_p:
            break
    return kept


def show_sampling(temperature: float, top_p: float) -> None:
    probabilities = softmax(LOGITS, temperature)
    kept = nucleus(probabilities, top_p)
    print("\nSAMPLING CONTROLS")
    print(f"  temperature: {temperature:.2f}  (lower sharpens the distribution)")
    print(f"  top_p:       {top_p:.2f}  (keeps the smallest probability nucleus)")
    print("  token distribution:")
    for name, probability in sorted(probabilities.items(), key=lambda item: -item[1]):
        marker = "kept" if any(name == kept_name for kept_name, _ in kept) else "cut"
        print(f"    {name:<16} {probability:.3f}  {marker}")
    print("  Sampling changes variability; it does not authorize tools or prove claims.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect layered guardrails offline.")
    parser.add_argument("--scenario", choices=sorted(SCENARIOS), default="clean")
    parser.add_argument(
        "--approve",
        action="store_true",
        help="allow the clean scenario's human-review routing tool",
    )
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--top-p", dest="top_p", type=float, default=0.85)
    args = parser.parse_args()

    if args.temperature <= 0:
        parser.error("--temperature must be greater than zero")
    if not 0 < args.top_p <= 1:
        parser.error("--top-p must be in (0, 1]")

    run_control_plane(args.scenario, args.approve)
    show_sampling(args.temperature, args.top_p)


if __name__ == "__main__":
    main()
