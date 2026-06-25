# ADR 0003 — RAG Combined with Tool Calling

**Status:** Accepted
**Date:** 2026-06-25

---

## Context

Financial questions fall into two distinct categories:

1. **Qualitative / factual** — "What did management say about supply chain risk?" → needs retrieved document context.
2. **Quantitative / computational** — "What was the 3-year CAGR of Apple's revenue?" → needs precise arithmetic, not retrieval.

A pure RAG approach handles (1) reasonably well but is unreliable for (2): LLMs make arithmetic errors and hallucinate numbers when asked to compute from retrieved text. A pure tool-calling approach handles (2) but has no access to unstructured document content for (1).

---

## Decision

Combine **RAG retrieval** with **deterministic tool calling** inside a LangGraph agent loop.

The Planner agent decides per-query which path (or combination) to take:
- Invoke the **Retriever tool** to fetch relevant document chunks, then pass context to the LLM for synthesis.
- Invoke the **Calculator tool** with extracted numeric inputs for exact financial computation.
- Chain both — retrieve numbers from documents, then feed them into the calculator.

---

## Rationale

- **Correctness for quantitative questions:** Calculator tools are deterministic. Revenue growth is always `(new - old) / old`, regardless of what the LLM thinks.
- **Faithfulness for qualitative questions:** Retrieved chunks ground the LLM's answer in actual document text, reducing hallucination.
- **Flexibility:** The agent can compose tool calls. A multi-hop question ("Compare margin improvement across three filings") can retrieve from all three, then compute.
- **Verifiability:** The Verifier node can check that cited numbers in the final answer match calculator outputs, catching inconsistencies before the response is returned.

---

## Consequences

- **Positive:** Higher accuracy on quantitative benchmarks (FinQA, ConvFinQA) than RAG-only; grounded qualitative answers.
- **Negative:** More complex agent logic and longer latency vs. a single retrieval + LLM call.
- **Mitigation:** Simple factual queries that don't require computation are handled in a single retrieval pass by the Planner; the multi-tool path is only triggered when computation is needed.
