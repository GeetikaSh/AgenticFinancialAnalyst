# Agentic Financial Analyst

## Overview

Agentic Financial Analyst is a production-grade AI system that analyzes financial documents and answers complex financial questions using Retrieval-Augmented Generation (RAG), deterministic calculation tools, and agentic reasoning.

The project is designed to simulate how an AI financial analyst would operate in a real enterprise environment by combining document retrieval, financial reasoning, tool usage, and report generation.

The primary objective is to build an end-to-end system that demonstrates modern AI engineering practices suitable for Senior AI Engineer and AI Solution Engineer roles.

---

# Goals

* Analyze SEC 10-K and 10-Q filings.
* Process earnings call transcripts.
* Answer conversational financial questions.
* Perform deterministic financial calculations.
* Generate executive summaries and reports.
* Support multi-step reasoning through an agent architecture.
* Evaluate performance using benchmark datasets such as ConvFinQA and FinQA.

---

# Features

## Document Ingestion

* PDF parsing
* Metadata extraction
* Table extraction
* Markdown conversion
* Context generation

## Retrieval-Augmented Generation (RAG)

* Embedding generation
* Vector database storage
* Semantic retrieval
* Context assembly

## Financial Reasoning

* Revenue growth
* CAGR
* Profit margins
* EPS calculations
* Ratio analysis
* Year-over-year comparisons

## Agentic Workflow

Planner Agent

↓

Retriever

↓

Calculator

↓

LLM

↓

Verifier

↓

Final Response

---

# High-Level Architecture

User

↓

FastAPI

↓

Planner Agent

↓

┌─────────────────────────────────┐

│ Retrieval Tool │

│ Calculator Tool │

│ Report Generator │

│ Memory │

└─────────────────────────────────┘

↓

LLM

↓

Verified Response

---

# Technology Stack

Backend

* Python 3.12
* FastAPI

AI

* OpenAI-compatible models
* LangChain
* LangGraph

Vector Store

* ChromaDB (initial MVP)

Data Validation

* Pydantic

Testing

* pytest

Code Quality

* Ruff
* mypy

Containerization

* Docker

---

# Data Sources

Production Data

* SEC 10-K filings
* SEC 10-Q filings
* Earnings call transcripts
* Financial APIs

Evaluation Data

* ConvFinQA
* FinQA

---

# Repository Structure

```
agentic-financial-analyst/

app/
agents/
ingestion/
rag/
llm/
tools/
evaluation/
tests/
docs/
scripts/
configs/
data/
```

---

# Development Roadmap

Phase 1

* Build ingestion pipeline
* Generate embeddings
* Implement retrieval

Phase 2

* Add financial calculator tools
* Build planner agent
* Implement report generation

Phase 3

* Add evaluation framework
* Introduce observability
* Containerize and deploy

---

# Engineering Principles

* SOLID principles
* Modular architecture
* Dependency injection where appropriate
* Type safety
* Testability
* Provider abstraction
* Clean separation of concerns
* Production-first design

---

# Current Status

🚧 In active development.
