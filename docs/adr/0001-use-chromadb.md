# ADR 0001 — Use ChromaDB as the Vector Store

**Status:** Accepted
**Date:** 2026-06-25

---

## Context

The system needs a vector store to persist document embeddings and support semantic similarity search over financial document chunks. The choice affects local development simplicity, query latency, and how easy it will be to swap the backend later.

Candidates considered:
- **ChromaDB** — embedded, file-persisted, zero-infra
- **Pinecone** — managed cloud, scales horizontally, requires API key and network
- **pgvector** — vector extension on Postgres, good if already running Postgres
- **Weaviate** — self-hosted or cloud, richer filtering but heavier to run locally

---

## Decision

Use **ChromaDB** with file persistence (`CHROMA_PERSIST_DIR`) for the MVP.

---

## Rationale

- Zero external dependencies — runs in-process alongside the Python app, no Docker service or API key needed for local dev.
- Fast iteration: embeddings persist to disk between runs so the ingestion pipeline does not need to re-embed on every restart.
- The `rag/` layer abstracts the vector store interface, so swapping to Pinecone or Weaviate later requires only a new adapter, not changes to retrieval logic.
- For the dataset sizes targeted in MVP (hundreds to low thousands of chunks from SEC filings), ChromaDB performance is more than sufficient.

---

## Consequences

- **Positive:** Simple local setup; no cloud cost during development.
- **Negative:** ChromaDB is not suitable for multi-replica deployments — it has no built-in replication or horizontal scaling.
- **Mitigation:** The vector store is hidden behind an abstract interface in `rag/`. Migration to a managed store is a targeted swap, not a refactor.
