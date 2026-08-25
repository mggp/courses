"""agent_boundaries.py — inspect an agent's integration boundaries offline.

This is deliberately not an MCP implementation. It is a small, in-memory model
of the boundaries an MCP-backed agent still has to own:

    skill instructions + resource context
        -> model decision -> tool execution -> observation -> next decision

Run:
    uv run agent_boundaries.py
    uv run agent_boundaries.py --approve

The default run refuses the side-effecting note tool. --approve lets the
same loop execute it, making the approval policy visible rather than hiding it
inside a prompt.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass(frozen=True)
class ToolSpec:
    name: str
    description: str
    side_effect: bool
    handler: Callable[..., dict[str, Any]]


@dataclass
class Runtime:
    approved: bool
    notes: list[str] = field(default_factory=list)


TICKET = {
    "id": "T-42",
    "text": "My card was charged twice and I cannot log in after changing phones.",
    "signals": ["billing", "access"],
    "needs_review": True,
}

TRIAGE_RESOURCE = {
    "uri": "lingua://policy/support-triage",
    "text": "Mixed billing and access signals require human review.",
}

TRIAGE_PROMPT = (
    "Review ticket {ticket_id}. Use the policy resource, inspect the ticket, "
    "and add a note only after explicit approval."
)

TRIAGE_SKILL = {
    "name": "support-triage",
    "instructions": "Separate evidence gathering from side-effecting actions.",
    "allowed_tools": {"get_ticket", "add_note"},
}


def get_ticket(ticket_id: str) -> dict[str, Any]:
    if ticket_id != TICKET["id"]:
        return {"status": "error", "message": f"Unknown ticket: {ticket_id}"}
    return {"status": "ok", "ticket": TICKET}


def add_note(runtime: Runtime, ticket_id: str, note: str) -> dict[str, Any]:
    if ticket_id != TICKET["id"]:
        return {"status": "error", "message": f"Unknown ticket: {ticket_id}"}
    if not runtime.approved:
        return {
            "status": "needs_approval",
            "message": "Runtime policy refused the side-effecting tool.",
        }
    runtime.notes.append(note)
    return {"status": "written", "ticket_id": ticket_id}


def model_decide(state: dict[str, Any]) -> dict[str, Any]:
    """A deterministic stand-in for an LLM decision.

    The point is the control loop, not model quality. Replacing this function
    with a real model call changes the decision source, not the boundaries.
    """
    if "ticket" not in state:
        return {
            "kind": "tool",
            "name": "get_ticket",
            "arguments": {"ticket_id": "T-42"},
        }

    if "note_result" not in state:
        return {
            "kind": "tool",
            "name": "add_note",
            "arguments": {
                "ticket_id": "T-42",
                "note": "Mixed billing and access signals; route to human review.",
            },
        }

    if state["note_result"]["status"] == "written":
        action = "The review note was written. Keep the ticket with human review."
    else:
        action = "The note was not written. Keep the ticket with human review."
    return {"kind": "final", "text": action}


def invoke_tool(
    tool: ToolSpec, runtime: Runtime, arguments: dict[str, Any]
) -> dict[str, Any]:
    if tool.name == "get_ticket":
        return tool.handler(**arguments)
    return tool.handler(runtime, **arguments)


def run_agent(approve: bool) -> None:
    runtime = Runtime(approved=approve)
    tools = {
        "get_ticket": ToolSpec(
            name="get_ticket",
            description="Read one support ticket.",
            side_effect=False,
            handler=get_ticket,
        ),
        "add_note": ToolSpec(
            name="add_note",
            description="Write a routing note onto one support ticket.",
            side_effect=True,
            handler=add_note,
        ),
    }

    print("MCP-STYLE CATALOG (in-memory; not the wire protocol)")
    print("  tools:")
    for tool in tools.values():
        marker = "side effect" if tool.side_effect else "read only"
        print(f"    - {tool.name}: {marker} — {tool.description}")
    print(f"  resource: {TRIAGE_RESOURCE['uri']} — {TRIAGE_RESOURCE['text']}")
    print("  prompt: triage-ticket — a reusable message template")
    print(f"  skill: {TRIAGE_SKILL['name']} — {TRIAGE_SKILL['instructions']}")
    print(f"  approval: {'enabled' if approve else 'disabled'}")

    prompt = TRIAGE_PROMPT.format(ticket_id=TICKET["id"])
    state: dict[str, Any] = {"policy": TRIAGE_RESOURCE["text"], "prompt": prompt}
    print("\nHOST CONTEXT")
    print(f"  resource read: {state['policy']}")
    print(f"  prompt rendered: {prompt}")

    print("\nAGENT TRACE")
    for step in range(1, 5):
        decision = model_decide(state)
        if decision["kind"] == "final":
            print(f"  {step:02d} MODEL -> final")
            print(f"      {decision['text']}")
            break

        name = decision["name"]
        if name not in TRIAGE_SKILL["allowed_tools"]:
            raise RuntimeError(f"Skill denied tool: {name}")
        tool = tools[name]
        arguments = decision["arguments"]
        print(f"  {step:02d} MODEL -> {name}({arguments})")
        result = invoke_tool(tool, runtime, arguments)
        print(f"      TOOL  <- {result}")
        if name == "get_ticket" and result["status"] == "ok":
            state["ticket"] = result["ticket"]
        if name == "add_note":
            state["note_result"] = result
    else:
        raise RuntimeError("Agent exceeded its stopping bound")

    print(f"\nAUDIT: notes written = {len(runtime.notes)}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inspect agent integration boundaries offline."
    )
    parser.add_argument(
        "--approve",
        action="store_true",
        help="allow the side-effecting add_note tool to run",
    )
    args = parser.parse_args()
    run_agent(approve=args.approve)


if __name__ == "__main__":
    main()
