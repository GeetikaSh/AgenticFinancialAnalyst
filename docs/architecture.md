# System Architecture

## Overview

Agentic Financial Analyst is a production-grade RAG + agent system for answering complex financial questions from SEC filings and earnings call transcripts.

---

## Current MVP Architecture

```
Raw Financial Documents
        │
        ▼
Ingestion Pipeline
  ├── PDF Parsing
  ├── Table Extraction
  ├── Metadata Extraction
  └── Context Construction
        │
        ▼
Embedding Generation
        │
        ▼
    ChromaDB
        │
        ▼
    Retriever
        │
        ▼
      LLM
        │
        ▼
     Answer
```

---

## Target Production Architecture

```
      User
        │
        ▼
    FastAPI (app/)
        │
        ▼
  Planner Agent (agents/)
        │
        ▼
┌────────────────────────────┐
│  Retriever    (rag/)       │
│  Calculator   (tools/)     │
│  Report Generator          │
│  Verifier                  │
└────────────────────────────┘
        │
        ▼
      LLM  (llm/)
        │
        ▼
Verified Financial Answer
```

---

## Layer Responsibilities

### `app/`
FastAPI application entry point. Exposes REST endpoints for query submission and result retrieval. Handles request validation via Pydantic models.

### `agents/`
LangGraph-based agentic loop. Contains the Planner that decides which tools to invoke and in what order, and the Verifier that checks numerical consistency before returning a final answer.

### `ingestion/`
Document ingestion pipeline:
- PDF parsing and text extraction
- Table detection and structured extraction
- Metadata tagging (company, filing type, reporting period)
- Chunking, markdown conversion, and context construction
- Embedding generation (via `llm/`)

### `rag/`
Retrieval-Augmented Generation layer:
- Embedding storage and semantic querying against ChromaDB
- Context assembly — ranks and deduplicates retrieved chunks

### `llm/`
Provider-agnostic LLM and embedding client. Abstracts over OpenAI-compatible APIs, Anthropic, and open-source models. All model calls route through here.

### `tools/`
Deterministic calculator tools registered with the agent:
- Revenue growth, CAGR, profit margin, EPS
- Year-over-year comparisons and ratio analysis

### `evaluation/`
Offline evaluation harness against ConvFinQA and FinQA benchmarks. Measures exact match, numerical accuracy, and reasoning faithfulness.

---

## Key Design Decisions

See [`adr/`](adr/) for the full reasoning behind each choice.

| Decision | Choice | ADR |
|---|---|---|
| Vector store | ChromaDB | [0001](adr/0001-use-chromadb.md) |
| Web framework | FastAPI | [0002](adr/0002-use-fastapi.md) |
| Retrieval strategy | RAG + tool calling | [0003](adr/0003-rag-with-tool-calling.md) |

---

## Technology Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Web framework | FastAPI |
| Agent framework | LangGraph |
| LLM orchestration | LangChain |
| Vector store | ChromaDB |
| Embeddings | OpenAI `text-embedding-3-small` |
| Chat model | OpenAI `gpt-4.1` (default, configurable) |
| Validation | Pydantic v2 |
| Testing | pytest |
| Linting / types | Ruff, mypy |
| Containerization | Docker |
