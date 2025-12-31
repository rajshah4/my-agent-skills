Here's a one-sentence summary for each slide:

1.  **Title Slide:** Introduces the presentation "From Vectors to Agents: Managing RAG in an Agentic World" by Rajiv Shah.
2.  **ACME GPT:** Presents a stylized logo for "ACME GPT" featuring a brain with circuit patterns inside a glowing circle over a city skyline.
3.  **Building RAG is Easy:** Illustrates a basic RAG (Retrieval-Augmented Generation) workflow from user query to LLM output with semantic search.
4.  **Building RAG is Easy (Code Example):** Shows a Python code snippet using LangChain to implement a simple RAG pipeline.
5.  **RAG Reality Check:** Highlights that 95% of Gen AI projects fail to reach production due to challenges in accuracy, latency, scaling, cost, and compliance.
6.  **Maybe try a different RAG?:** Lists a multitude of RAG variants and advanced retrieval techniques, emphasizing the complexity and breadth of the field.
7.  **Ultimate RAG Solution:** Depicts a humorous, over-engineered cartoon machine as a metaphorical "ultimate RAG solution" with many interconnected components.
8.  **RAG as a system:** Breaks down RAG into a four-stage system: Parsing, Querying, Retrieving, and Generation, with detailed sub-steps for each.
9.  **Designing a RAG Solution:** Introduces a triangular framework for RAG tradeoffs focusing on Problem Complexity, Latency, and Cost, alongside the "Cost of a mistake."
10. **RAG Considerations:** Lists key factors to consider for RAG solutions like extraction, latency, query amount, multilingual support, domain difficulty, and data quality, and presents a table categorizing generation tasks by complexity.
11. **Consider Query Complexity:** Provides examples of queries with increasing complexity, from simple keywords to multi-hop and agentic scenarios, to illustrate different RAG demands.
12. **Retrieval (Highlighted):** Highlights the "Retrieving" stage of the RAG system diagram, emphasizing it as the current focus.
13. **Retrieval Approaches:** Outlines three main retrieval approaches: BM25 (keyword-based), Language Models (semantic embeddings), and Agentic Search (dynamic LLM reasoning).
14. **Building RAG is Easy (Code Highlight):** Highlights the vector database and retriever initialization in the earlier Python RAG code, representing basic semantic search.
15. **BM25:** Explains BM25 as a probabilistic lexical ranking function using diagrams of an inverted index and its scoring formula.
16. **BM25 Performance:** Presents a table showing BM25's efficient performance in terms of time taken for search compared to linear scan and inverted index methods as document count increases.
17. **BM25 Failure Cases:** Illustrates scenarios where BM25 fails due to synonym gaps or unrecognized aliases, concluding that it's a strong baseline for keyword-heavy, sub-second queries.
18. **Hands on: BM25s:** References a Hugging Face article and GitHub repository for a high-performance Python implementation of BM25.
19. **Enter Language Models:** Explains how language models encode text into dense embedding vectors to capture semantic meaning.
20. **Embeddings Visualized:** Visualizes embeddings in a 2D space, demonstrating how semantic similarity groups related concepts and resolves lexical issues that BM25 struggles with.
21. **Semantic search is widely used:** Shows a Google SearchLiaison tweet announcing BERT's impact on search and a Hugging Face page listing numerous sentence transformer models.
22. **Which language model?:** Presents a scatter plot comparing the inference speed and NDCG@10 scores of various transformer and static embedding models, including BM25.
23. **Static Embeddings:** Explains static embeddings (like Word2Vec) as uncontextualized, fast, and lightweight but with lower accuracy, using a diagram to show conceptual clustering.
24. **Why Context Matters:** Uses a cartoon comparison between Word2Vec and a Transformer Model to illustrate how transformers understand context, unlike static embeddings.
25. **Many more models!:** Re-displays the scatter plot of embedding models with a red arrow pointing towards higher performance, suggesting a continuous evolution of models.
26. **MTEB/RTEB:** Introduces the Massive Text Embedding Benchmark (MTEB) and the Retrieval Text Embedding Benchmark (RTEB) as comprehensive leaderboards for evaluating embedding models across tasks and languages.
27. **Selecting an embedding model:** Presents a bubble chart showing Mean Task score vs. Number of Parameters for various embedding models, with color intensity indicating Max Tokens, and lists accuracy, latency, and compute as key selection criteria.
28. **Selecting an embedding model (Other Considerations):** Lists additional factors for choosing embedding models, including model size, architecture (CPU/GPU/Quantization), embedding dimension, training data (multilingual/domain), and fine-tuning.
29. **Matryoshka Embedding Models:** Explains Matryoshka embeddings, which allow truncated vectors to retain performance at smaller dimensions, making them flexible for different use cases.
30. **Sentence Transformer:** Describes Sentence Transformers as models designed for sentence-level meaning, semantic search, better retrieval performance, and efficiency, illustrating their Siamese network architecture.
31. **Cross Encoder / Reranker:** Explains the two-stage retrieval process: an initial vector search followed by a cross-encoder reranker to improve relevance, with a diagram of the workflow.
32. **Cross Encoder / Reranker (Duplicate of 31):** This slide is identical to slide 31, reiterating the concept of cross-encoders and rerankers.
33. **Cross Encoder / Reranker (Accuracy Boost):** Shows a bar chart demonstrating that adding a reranker significantly boosts retrieval accuracy (NDCG) in Llama 3.1 70B powered RAG.
34. **Cross Encoder / Reranker (Execution Flow):** Presents an execution flow diagram for a RAG system, highlighting that reranking is a significant component in terms of time taken.
35. **Hands On: Retriever & Reranker:** Provides a screenshot of a Colab notebook demonstrating a retrieve and re-rank setup over Simple Wikipedia, using a SentenceTransformer for initial retrieval and a CrossEncoder for reranking.
36. **Instruction Following Reranker:** Shows an example of an instruction-following reranker that can dynamically rank documents based on specific instructions or criteria, such as "Default ranking" or "Safety Notice Official."
37. **Combine Multiple Retrievers:** Illustrates that combining multiple retrievers (e.g., BM25, BGE, E5 Mistral, Voyager-large-2) and adding a reranker generally improves recall compared to individual retrievers.
38. **Cascading Rerankers in Kaggle:** Features a diagram illustrating a Kaggle competition solution that uses a cascade of rerankers with different models and synthetic data generation to improve retrieval.
39. **Best practices:** Presents a simplified workflow for optimal retrieval, combining Semantic Search and Lexical Search with Reciprocal Rank Fusion, followed by a Reranker.
40. **Families of Embedding Models:** Provides a taxonomy of embedding models, categorizing them by speed and accuracy, and describing their characteristics from Model2Vec to Cross-Encoders.
41. **Lots of New Models:** Showcases new embedding models like mmBERT, IBM Granite, and Google EmbeddingGemma, indicating ongoing innovation in the field.
42. **Other retrieval methods:** Lists alternative retrieval methods beyond standard embeddings, such as SPLADE for sparse retrieval, ColBERT for late interaction, and GraphRAG.
43. **Operational Concerns:** Discusses operational challenges in computing and storing embeddings, comparing the speed of various nearest neighbor search algorithms and vector database solutions.
44. **Vector Database Options:** Presents a "Vector Database Layered Storage Architecture" diagram, categorizing storage tiers (Hot, Warm, Cold) based on latency requirements and application scenarios, with corresponding technical solutions.
45. **Operational Concerns (Datastore Size):** Shows a graph indicating that as datastore size increases, improving retrieval performance (e.g., with cross-encoders or rerankers) becomes critical, outperforming lexical oracle and LM-only approaches.
46. **Search Strategy Comparison:** Compares "Traditional RAG" with "Agentic RAG" visually, suggesting that agentic RAG explores the solution space more dynamically.
47. **Tools use / Reasoning:** Explains the concept of using reasoning models and tools in an agentic system to iteratively query until a satisfactory answer is achieved, with a Python code example.
48. **Agentic RAG (Workflow):** Presents a flowchart illustrating an Agentic RAG workflow involving iterative steps of query, retrieval, grading, relevance check, generation, hallucination check, and query rewrite.
49. **Tools use / Reasoning (Detailed Example):** Shows a detailed example of an agent's reasoning process with tool calls and intermediate steps to answer a complex query about making published changes draft.
50. **Open Deep Research:** Outlines the "Open Deep Research" framework, which involves distinct stages of scoping (user context), research (context gathering via sub-agents), and writing (report generation).
51. **DeepResearch Bench:** Shows a leaderboard for the DeepResearch Bench, highlighting models' performance on 100 PhD-level research tasks, with Gemini 2.5 Pro leading.
52. **Westlaw AI Deep Research:** Presents a screenshot of Westlaw AI Deep Research, demonstrating a real-world application of advanced RAG for legal research with agentic capabilities.
53. **Agentic RAG (Self-RAG):** Re-displays the Agentic RAG workflow, specifically referencing it as "Self RAG" and highlighting its iterative nature with self-reflection.
54. **Agentic RAG (LangChain Reddit):** Shows a Reddit post discussing a Self-Reflection RAG system built with LangChain that evaluates retrieved documents and its own responses.
55. **Agentic RAG (Efficiency Concerns):** Continues the Reddit discussion, addressing the inefficiency of agentic RAG and suggesting solutions like early stopping, circuit breakers, and caching.
56. **Research: BRIGHT:** Introduces "BRIGHT" as a framework for analyzing retrieval reasoning, demonstrating different levels of query complexity (keyword, semantic, reasoning-based) and their corresponding retrieved documents.
57. **BRIGHT #1: DIVER:** Presents a diagram of the "DIVER" system (part of BRIGHT) for reasoning-intensive information retrieval, involving document chunking, query expansion, and a two-stage reranking process.
58. **BRIGHT #1: DIVER (LLM Instructions):** Provides the specific LLM prompts used in DIVER-QExpand for query expansion in both the first and subsequent rounds of an iterative retrieval process.
59. **Agentic RAG on WixQA:** Compares the factuality performance and latency of "One Shot RAG" versus "Agentic RAG" on the WixQA dataset, showing higher accuracy for agentic RAG but with much higher latency.
60. **Rethink your Assumptions:** Presents a graph showing that even for advanced LLM models, a simple BM25 retriever can be competitive or even outperform SBERT and other models in certain scenarios when queried with an LLM.
61. **Agentic RAG with BM25:** Demonstrates that Agentic RAG combined with BM25 (lexical search) can achieve comparable high factuality scores to Agentic RAG with embedding models, on both WixQA and a Financial Dataset.
62. **Agentic RAG for Code Search:** Discusses the surprising effectiveness of lexical search (like `grep`) for code search within Agentic RAG, particularly with models like Anthropic Claude Code, potentially outperforming vector search for this domain.
63. **Combine Retrieval Approaches:** Illustrates a "Response Guardrail System" that uses a two-tier approach of text and LLM-based guardrails (checking groundness, coherence, compliance) to ensure the quality of generated responses.
64. **Hands on: Agentic RAG (Smolagents):** Points to a Colab notebook that provides a hands-on guide to building Agentic RAG using Hugging Face `smolagents` and comparing it to Vanilla RAG.
65. **Solutions for a RAG Solution:** Maps specific RAG solutions to the "Problem Complexity (instead of accuracy)" framework, suggesting Rerankers for high cost of mistakes, BM25 + Static Embeddings for <5s latency, and Agentic RAG for complex multi-hop queries.
66. **Retriever Checklist:** Provides a checklist of retrieval approaches: Keyword/BM25, Semantic Search/Embedding Model, and Agentic/Reasoning LLM.
67. **RAG as a system (Retrieval with Instruction Following Reranker):** Updates the RAG system diagram, specifically replacing "Reranker" with "Instruction Following Reranker" in the retrieval stage.
68. **RAG - Generation:** Discusses the generation stage of RAG, highlighting the goal of producing coherent answers rather than just search results, and noting recent technical improvements in this area.
69. **RAG - Generation (Model Selection):** Explains that choosing a generation model depends on cost/latency budget and specific needs (low hallucination, domain-specific, language-specific), and shows various LLM options.
70. **Chunking approaches:** Compares standard "Original" chunking with "Contextual Chunking," which adds prefix information to document chunks to provide better context for the LLM.
71. **Title Slide (Duplicate):** This slide is identical to slide 1, serving as a concluding title slide.