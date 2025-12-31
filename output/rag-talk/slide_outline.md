1. Introduces the presentation "From Vectors to Agents: Managing RAG in an Agentic World" by Rajiv Shah.
2. Displays a logo for "ACME GPT," likely representing a hypothetical RAG system.
3. Illustrates a simplified flow diagram of a basic RAG (Retrieval Augmented Generation) system, showing user query to LLM output.
4. Presents a Python code snippet demonstrating a straightforward implementation of a RAG pipeline using LangChain.
5. Highlights that 95% of Gen AI projects, including RAG, fail in production due to challenges in accuracy, latency, scaling, cost, and compliance.
6. Lists numerous variations and advanced techniques within Retrieval Augmented Generation (RAG) beyond the basic approach.
7. Features a humorous, over-engineered cartoon depicting an "Ultimate RAG Solution" that attempts to combine all possible algorithms and data types.
8. Presents a comprehensive multi-stage diagram of RAG as a system, detailing parsing, querying, retrieving, and generation steps.
9. Introduces a RAG design framework highlighting the tradeoffs between problem complexity, latency, and cost, alongside the "cost of a mistake."
10. Outlines RAG considerations and a table categorizing different generation types based on query and retrieval complexity, from simple fact to deep reasoning.
11. Provides examples of increasing query complexity, from simple keyword searches to multi-hop and agentic scenarios.
12. Highlights the "Retrieval" stage within the RAG system diagram, emphasizing the core process of fetching relevant information.
13. Introduces three main retrieval approaches: BM25 (keyword-based), Language Models (semantic embeddings), and Agentic Search (LLM reasoning).
14. Revisits the RAG code snippet, highlighting the lines related to embedding generation and vector database retrieval.
15. Explains BM25 as a probabilistic lexical ranking function, illustrating its mechanism with keyword indexing and a formula.
16. Demonstrates BM25's efficient scaling performance compared to linear and inverted index search across varying document counts.
17. Discusses BM25's failure cases, such as synonym gaps and aliases, concluding it's a strong baseline for keyword-heavy queries needing sub-second response.
18. Directs to a Hugging Face article and GitHub repository for a high-performance Python implementation of BM25.
19. Illustrates how language models convert text into dense embedding vectors through a neural encoder.
20. Visualizes embeddings in a 2D space, demonstrating how semantic similarity groups related concepts and resolves lexical issues.
21. Shows examples of widespread use of semantic search, including Google's BERT and a leaderboard of sentence-transformer models on Hugging Face.
22. Presents a scatter plot comparing inference speed and NDCG@10 scores of various transformer and static models on the NanoBEIR Benchmark, pointing out BM25.
23. Describes static embeddings (Model2Vec) as uncontextualized, fast, and lightweight, but with lower accuracy.
24. Uses a cartoon analogy to explain the difference between Word2Vec (token-level) and Transformer models (sentence-level) in understanding context.
25. Reiterates the scatter plot comparing embedding models, emphasizing the multitude of available models and their performance trade-offs.
26. Introduces the MTEB/RTEB leaderboard on Hugging Face, showcasing performance across hundreds of models, tasks, and languages.
27. Provides a bubble chart for selecting an embedding model based on accuracy, latency, compute requirements (CPU/GPU), and number of parameters.
28. Lists additional considerations for selecting an embedding model, including model size, architecture, embedding dimension, and training data.
29. Explains Matryoshka Embedding Models, which allow truncating embeddings to different dimensions without losing quality.
30. Details Sentence Transformers as models designed for sentence-level meaning, semantic search, and efficient retrieval performance.
31. Illustrates the architecture of a cross-encoder or reranker, showing a two-stage process of initial vector search followed by a more precise reranking.
32. Duplicates the illustration of a cross-encoder or reranker architecture, emphasizing the two-stage retrieval and re-ranking process.
33. Presents a bar chart demonstrating how adding a reranker significantly boosts accuracy in Llama 3.1 70B powered RAG.
34. Shows an approximate execution flow for RAG, highlighting that reranking can account for a substantial portion (28.6%) of the overall latency.
35. Points to a Colab notebook demonstrating a hands-on example of a Retrieve & Re-Rank setup over Simple Wikipedia.
36. Introduces an "Instruction Following Reranker" that can reorder search results based on specific instructions, exemplified by product reviews and safety alerts.
37. Illustrates the benefits of combining multiple retrievers (BM25, BGE, E5 Mistral, Voyager-large-2) and rerankers to improve recall.
38. Presents a diagram from a Kaggle competition demonstrating the use of cascading rerankers to refine retrieval results.
39. Recommends best practices for retrieval, combining semantic search, lexical search, reciprocal rank fusion, and reranking.
40. Provides a taxonomy of embedding models, categorizing them by speed, accuracy, and use cases, from static embeddings to cross-encoders.
41. Showcases several new embedding models, including mmBERT, IBM's Granite, and Google's EmbeddingGemma, indicating ongoing innovation.
42. Lists other advanced retrieval methods like SPLADE, ColBERT Late Interaction, and GraphRAG, acknowledging many RAG flavors exist.
43. Addresses operational concerns for RAG, comparing performance and latency for computing and storing embeddings across different systems (FAISS, Pinecone, ChromaDB).
44. Illustrates a vector database layered storage architecture, optimizing for latency requirements across hot, warm, and cold data tiers.
45. A chart demonstrating that as datastore size increases, improving retrieval performance becomes crucial, especially for cross-encoder and lexical oracle methods.
46. Visually compares search strategies, contrasting traditional RAG with agentic RAG's more exploratory and dynamic approach to finding information.
47. Shows a code example of an agentic reasoning model continually querying until a task, like scientific research evaluation, is satisfied.
48. Presents a flowchart for Agentic RAG, featuring iterative steps of retrieval, grading relevance, and query rewriting until an answer is found.
49. Provides a detailed example of an agent performing complex tool-use and reasoning steps to answer a question about managing published changes.
50. Outlines the "Open Deep Research" pipeline, a multi-agent framework encompassing scope clarification, research, and report generation.
51. Displays the DeepResearch Bench leaderboard, showing model performance on 100 PhD-level research tasks.
52. Shows the user interface of Westlaw AI Deep Research, an agentic system for generating detailed, cited legal research reports.
53. Illustrates the Self RAG process, incorporating nodes for grading retrieval relevance and checking for hallucinations before generating an answer.
54. Features a Reddit post discussing "Self-Reflection RAG," which evaluates retrieved documents and its own generations, deciding when to retrieve or use internal knowledge.
55. Presents a Reddit comment highlighting the inefficiency of agentic RAG's full pipeline restart and suggesting improvements like early stopping and caching.
56. Introduces BRIGHT (Reasoning-based Retrieval) research, analyzing queries across keyword-based, semantic, and reasoning-based retrieval levels.
57. Details the DIVER framework, a component of BRIGHT, which includes document chunking, query expansion, and multi-stage reranking for reasoning-intensive information retrieval.
58. Provides the specific LLM prompts used in DIVER-QExpand for both first-round and subsequent rounds of query expansion.
59. Compares the factuality and latency of One Shot RAG versus Agentic RAG on WixQA, showing higher accuracy for Agentic RAG at the cost of higher latency.
60. Challenges assumptions by showing that BM25 can outperform SBERT in NDCG@10 scores when used with LLM querying, depending on the model.
61. Demonstrates that Agentic RAG, even when restricted to BM25 for retrieval, maintains high factual equivalence on both WixQA and a financial dataset.
62. Discusses Agentic RAG for code search, noting that sophisticated models like Claude Code sometimes rely solely on lexical/iterative search (like `grep`) instead of vectors.
63. Presents a "Response Guardrail" system, a two-tier approach combining NLP embedding guardrails and LLM-based guardrails to ensure compliant and coherent responses.
64. Offers a hands-on resource comparing Agentic RAG using Hugging Face's `smolagents` library against vanilla RAG.
65. Proposes solutions for RAG challenges: rerankers for high-cost mistakes, BM25/static embeddings for low latency, and agentic RAG for complex multi-hop queries.
66. Provides a checklist for choosing a retriever, including keyword/BM25, semantic search/embedding models, and agentic/reasoning LLMs.
67. Reverts to the full RAG system diagram, now integrating an "Instruction Following Reranker" into the retrieval stage.
68. Discusses RAG's generation phase, emphasizing the need for generation models to produce coherent answers rather than just search results.
69. Outlines considerations for selecting a generation model in RAG, including cost, latency, hallucination control, domain specificity, and context window management.
70. Demonstrates "Contextual Chunking," which adds prefix information to document chunks to provide more context during retrieval.
71. Concludes the presentation, restating the title and providing speaker contact information and a GitHub link.