# Development Roadmap

## Phase 1 — MVP Ingestion & Retrieval

**Goal:** End-to-end pipeline from raw document to retrieved answer.

- [ ] PDF parsing with table and metadata extraction
- [ ] Chunking strategy and markdown conversion
- [ ] Embedding generation via OpenAI `text-embedding-3-small`
- [ ] ChromaDB storage and semantic retrieval
- [ ] Basic LLM answer generation from retrieved context

---

## Phase 2 — Agentic Reasoning

**Goal:** Replace single-pass retrieval with a multi-step agent that can use tools.

- [ ] Planner agent (LangGraph) with tool dispatch loop
- [ ] Deterministic financial calculator tools (CAGR, margins, EPS, YoY)
- [ ] Verifier node — checks numerical consistency before response
- [ ] Report generator for structured executive summaries
- [ ] FastAPI endpoints wiring agent to HTTP interface

---

## Phase 3 — Evaluation & Observability

**Goal:** Measure quality and make the system production-observable.

- [ ] Evaluation harness against ConvFinQA and FinQA benchmarks
- [ ] Exact match, numerical accuracy, and faithfulness metrics
- [ ] Structured logging (JSON) and trace IDs across agent steps
- [ ] Latency and token-cost instrumentation
- [ ] Containerization with Docker; Docker Compose for local stack

---

## Future Considerations

- Swap ChromaDB for a managed vector store (Pinecone, Weaviate) for scale
- Add streaming responses via FastAPI `StreamingResponse`
- Multi-document cross-filing comparison queries
- Fine-tuned embedding model on financial domain text
- LangSmith or equivalent for production tracing
