# ADR 0002 — Use FastAPI as the Web Framework

**Status:** Accepted
**Date:** 2026-06-25

---

## Context

The system needs an HTTP layer to expose the financial analyst agent to external clients. The framework choice affects developer ergonomics, type safety, async support, and documentation generation.

Candidates considered:
- **FastAPI** — async-first, Pydantic-native, auto-generates OpenAPI docs
- **Flask** — synchronous by default, minimal, wide ecosystem
- **Django REST Framework** — full-featured, higher overhead for a focused AI API

---

## Decision

Use **FastAPI**.

---

## Rationale

- **Async-first:** LLM calls and embedding requests are I/O-bound. FastAPI's native `async/await` support means request handlers can yield the event loop during model calls, enabling concurrent request handling without threads.
- **Pydantic integration:** The project already uses Pydantic v2 for data validation throughout the pipeline. FastAPI's request/response models are Pydantic models — no extra serialization layer.
- **Auto-generated OpenAPI docs:** `/docs` and `/redoc` are available out of the box, which is useful for demonstrating the API to stakeholders.
- **Streaming support:** `StreamingResponse` and Server-Sent Events make it straightforward to stream agent intermediate steps or partial answers in a future iteration.

---

## Consequences

- **Positive:** Type-safe request/response handling; async concurrency; minimal boilerplate.
- **Negative:** FastAPI adds a dependency on Starlette and an ASGI server (Uvicorn); Flask would be lighter if async were not needed.
- **Mitigation:** The agent and RAG logic are fully decoupled from the HTTP layer — the FastAPI routes are thin wrappers, so switching frameworks later would be a contained change.
