"""Lesson 12 — make delivery architecture and experience boundaries explicit.

Run from this directory:
    uv sync
    uv run delivery_story.py
    uv run delivery_story.py --framework fastapi --provider bedrock
    uv run delivery_story.py --framework flask --provider foundry

The provider adapters are local stand-ins. No cloud SDK or network call is
performed. The point is to inspect the dependency boundary and practise an
honest platform-gap answer.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class GenerationRequest:
    question: str
    context: str


@dataclass(frozen=True)
class GenerationResponse:
    provider: str
    text: str


class ModelPort(Protocol):
    """The use case's stable dependency, independent of a provider SDK."""

    provider_name: str

    def generate(self, request: GenerationRequest) -> GenerationResponse:
        ...


class AuditPort(Protocol):
    def record(self, event: str) -> None:
        ...


class LocalModelAdapter:
    """Deterministic stand-in for a local or hosted model adapter."""

    def __init__(self, provider_name: str) -> None:
        self.provider_name = provider_name

    def generate(self, request: GenerationRequest) -> GenerationResponse:
        text = (
            f"Answer from {self.provider_name}: use the supplied context, "
            f"then evaluate the result before returning it. Context seen: {request.context}"
        )
        return GenerationResponse(provider=self.provider_name, text=text)


class InMemoryAudit:
    def __init__(self) -> None:
        self.events: list[str] = []

    def record(self, event: str) -> None:
        self.events.append(event)


class AnswerService:
    """Application use case: orchestration, not HTTP or provider SDK logic."""

    def __init__(self, model: ModelPort, audit: AuditPort) -> None:
        self.model = model
        self.audit = audit

    def answer(self, question: str, context: str) -> GenerationResponse:
        self.audit.record(f"answer.request provider={self.model.provider_name}")
        response = self.model.generate(GenerationRequest(question, context))
        self.audit.record("answer.generated")
        return response


FRAMEWORKS = {
    "fastapi": (
        "typed request/response contracts, automatic OpenAPI documentation, "
        "dependency injection, and a natural fit for async I/O"
    ),
    "flask": (
        "a small WSGI-oriented core, explicit composition, and a broad extension "
        "ecosystem; async views still retain Flask's WSGI worker semantics"
    ),
}

WEB_BOUNDARIES = {
    "fastapi": (
        "ASGI application callable: scope, receive, and send; await non-blocking I/O, "
        "with HTTP, WebSocket, and lifespan message support"
    ),
    "flask": (
        "WSGI application callable: environ and start_response, then a returned "
        "iterable; async views retain WSGI worker semantics"
    ),
}

PROVIDERS = {
    "local": "local stand-in: no cloud claim",
    "bedrock": "Amazon Bedrock stand-in: managed foundation-model access to evaluate",
    "foundry": "Microsoft Foundry stand-in: managed models/agents/tools surface to evaluate",
    "vertex": "Google Vertex AI stand-in: managed AI-platform surface to evaluate",
}


def print_design_checks() -> None:
    print("\nSOLID DESIGN CHECK")
    print("  SRP  PASS — HTTP, use case, provider adapter, and audit have separate jobs")
    print("  OCP  PASS — add another ModelPort adapter without editing AnswerService")
    print("  LSP  PASS — each adapter returns the GenerationResponse contract")
    print("  ISP  PASS — the use case receives small ModelPort and AuditPort interfaces")
    print("  DIP  PASS — AnswerService depends on ports, not a provider SDK")


def print_web_boundary(framework: str) -> None:
    print("\nWEB SERVER INTERFACE")
    print(f"  {framework.upper()}: {WEB_BOUNDARIES[framework]}")
    print("  ASGI does not make blocking code non-blocking; WSGI concurrency usually comes from workers or threads")


def print_cloud_gap(provider: str) -> None:
    print("\nHONEST PLATFORM STATEMENT")
    if provider == "local":
        print("  This run uses a local deterministic stand-in; it makes no cloud-experience claim.")
        return
    print(f"  {PROVIDERS[provider]}.")
    print("  I have not used this platform hands-on or in production, so I would not claim that experience.")
    print("  My relevant experience is maintaining FastAPI services, integrating MCP tooling, and building RAG mechanics locally.")
    print("  I would evaluate model choice, IAM/identity, network boundaries, retrieval, guardrails, evaluation, latency, cost, and monitoring.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect delivery boundaries and practise an honest platform answer.")
    parser.add_argument("--framework", choices=sorted(FRAMEWORKS), default="fastapi")
    parser.add_argument("--provider", choices=sorted(PROVIDERS), default="local")
    args = parser.parse_args()

    audit = InMemoryAudit()
    service = AnswerService(LocalModelAdapter(PROVIDERS[args.provider]), audit)
    response = service.answer(
        "How should a grounded answer be delivered?",
        "retrieve evidence, validate claims, and record the decision",
    )

    print(f"FRAMEWORK: {args.framework}")
    print(f"  choice signal: {FRAMEWORKS[args.framework]}")
    print_web_boundary(args.framework)
    print("\nDEPENDENCY BOUNDARY")
    print("  HTTP route -> AnswerService -> ModelPort -> local provider adapter")
    print("                         └──> AuditPort -> InMemoryAudit")
    print(f"\nRESPONSE: {response.text}")
    print(f"AUDIT: {audit.events}")
    print_design_checks()
    print_cloud_gap(args.provider)


if __name__ == "__main__":
    main()
