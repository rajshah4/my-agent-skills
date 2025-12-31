---
title: "From Vectors to Agents: A Practical Guide to Managing RAG in Production"
date: 2023-10-27
author: Rajiv Shah (Adapted by Technical Editorial Team)
tags: [RAG, AI, Machine Learning, Agents, LLMs, Vector Search]
---

We are living in the golden age of "easy" AI demos. With a few lines of Python, LangChain, and an OpenAI API key, almost anyone can build a Retrieval Augmented Generation (RAG) system that chats with a PDF.

But there is a massive gap between a weekend demo and an enterprise-grade application. As highlighted in a recent technical deep dive, **95% of Gen AI projects fail in production.**

Why? Because while the "Hello World" of RAG is simple, the reality involves complex trade-offs between accuracy, latency, cost, and compliance.

In this post, based on the talk **"From Vectors to Agents"** (watch the full video [here](https://youtu.be/AS_HlJbJjH8)), we will move beyond the basics. We’ll explore a design framework for RAG, dive deep into retrieval algorithms (from BM25 to Embeddings), and look at the emerging world of Agentic RAG.

![Slide 3: Simplified RAG Flow](images/slide_3.png)
*A simplified RAG flow is easy to build, but hard to scale.*

---

## The RAG Reality Check

If you have built a RAG system, you know the feeling. You show it to your CEO, they ask a specific question like "Who is on the Board of Directors?", and the model hallucinates or retrieves the wrong chunk.

> "You can build a very easy RAG demo out of the box... but as you try to move that into production, you figure out that the accuracy isn't that great... or the latency is unbearable."  
> — *[00:01:42](https://youtu.be/AS_HlJbJjH8&t=102s)*

To prevent failure, we need to treat RAG not as a magic black box, but as an engineering system composed of parsing, chunking, querying, retrieving, and generating.

![Slide 8: RAG System Diagram](images/slide_8.png)

### The Design Framework: Trade-offs Matter
Before writing code, you need to understand your constraints. As shown in **Slide 9**, successful RAG implementation requires balancing three factors:

1.  **Problem Complexity:** Are users asking for keywords or complex reasoning?
2.  **Latency/Cost:** Do you need sub-second responses, or can the user wait 30 seconds for a deep research report?
3.  **The Cost of a Mistake:** Is this a code assistant where a developer can catch a bug (low cost), or a medical advisor where an error is fatal (high cost)?

---

## Deep Dive: The Retrieval Layer

The heart of RAG is retrieval. If you don't get the right context to the LLM, the best prompt engineering in the world won't save you. Let's look at the three main approaches to retrieval.

### 1. BM25 (Lexical Search)
BM25 (Best Match 25) is the 25th iteration of a probabilistic scoring framework based on keyword frequency. It creates an inverted index mapping words to documents.

**Why use it?**
*   **Speed:** It is incredibly fast. As demonstrated in **Slide 16**, BM25 scales efficiently even as document counts rise to the millions, whereas linear search creates massive latency.
*   **Exact Matches:** It excels at specific identifiers (e.g., part numbers, specific names).

**The Downside:**
It fails at synonyms. If a user searches for "Physician" but your documents only contain the word "Doctor," BM25 will return nothing.

> "This is a very strong baseline... depending on the type of documents and queries you have, this can be a good fit."  
> — *[00:11:46](https://youtu.be/AS_HlJbJjH8&t=706s)*

### 2. Language Models (Semantic Search)
This is the modern standard. We use an encoder to turn text into dense vectors (embeddings). In this high-dimensional space, "Physician" and "Doctor" are mathematically close to each other.

![Slide 20: Embeddings Visualization](images/slide_20.png)

However, not all embedding models are created equal. **Slide 27** presents a bubble chart comparing models based on:
*   **Accuracy (MTEB Score)**
*   **Latency**
*   **Compute requirements (CPU vs GPU)**

**Key Insight:** You don't always need the massive Transformer models.
*   **Static Embeddings (e.g., Model2Vec):** These are lightweight and fast (CPU-friendly) but lack context awareness (Slide 23).
*   **Sentence Transformers:** Designed for sentence-level meaning, offering a great balance of speed and accuracy (Slide 30).

*Tip: Check the [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) to choose the right model for your specific domain and constraints.*

### 3. The Reranker (Cross-Encoders)
If you need higher accuracy, you can add a second stage to your pipeline: the **Reranker**.

1.  **Retrieve:** Use a fast method (BM25 or Vector Search) to get the top 50 results.
2.  **Rerank:** Use a Cross-Encoder to deeply analyze the relationship between the query and those 50 documents.

As shown in **Slide 33**, adding a reranker significantly boosts accuracy. However, it comes with a latency penalty—potentially accounting for nearly 30% of your total execution time (**Slide 34**).

---

## The New Frontier: Agentic RAG

We are currently witnessing a shift from "Vectors" to "Agents."

Standard RAG is linear: Query $\rightarrow$ Retrieve $\rightarrow$ Generate.
**Agentic RAG** is a loop. The system can "reason" about the data it finds.

![Slide 46: Standard vs Agentic RAG](images/slide_46.png)

### How Agentic RAG Works
As detailed in **Slide 48**, an agentic flow might look like this:
1.  **Retrieve** information.
2.  **Grade** the document: Is this relevant to the user's question?
3.  **Decide:**
    *   *If yes:* Generate an answer.
    *   *If no:* Rewrite the query and search again.

This approach allows for "Self-Correction." If the system realizes it retrieved junk data, it doesn't just hallucinate an answer; it goes back to the library.

### The Trade-off: Accuracy vs. Latency
The results are compelling. **Slide 59** compares One-Shot RAG vs. Agentic RAG on the WixQA dataset. Agentic RAG provides significantly higher factuality.

The catch? **Latency.** Because the model might search, read, think, and search again, a query that took 2 seconds in standard RAG might take 30+ seconds in an agentic workflow.

> "Agentic RAG... even when restricted to BM25 for retrieval, maintains high factual equivalence." — *Slide 61*

This is a crucial finding: A smart agent using a "dumb" search tool (BM25) can often outperform a "dumb" linear chain using smart vectors.

---

## Conclusion: Choosing Your Stack

There is no "Ultimate RAG Solution" (despite the funny cartoon in **Slide 7**). There is only the right solution for your specific constraints.

Here is a quick checklist (**Slide 66**) to guide your architecture decisions:

1.  **Low Latency / Specific Keywords:** Start with **BM25**. It’s fast, cheap, and effective for exact matches.
2.  **The "Middle Ground":** Use **Semantic Search (Embeddings)**. It handles synonyms and intent well.
3.  **High Accuracy Requirement:** Add a **Reranker**. It costs more compute but reduces hallucinations.
4.  **Complex Reasoning / High Cost of Error:** Move to **Agentic RAG**. If you are building a "Deep Research" tool or a legal assistant (like Westlaw AI, **Slide 52**), the extra latency is worth the reasoning capability.

RAG is moving fast. We've gone from simple vector lookups to complex, reasoning agents. By understanding the underlying mechanics of retrieval and the trade-offs of agentic loops, you can build systems that don't just demo well—but actually work in production.

*For the full technical breakdown, code snippets, and benchmarks, watch Rajiv Shah's full presentation [here](https://youtu.be/AS_HlJbJjH8).*