Here is a one-sentence summary for each slide:

1.  This is a title slide for a workshop by Rajiv Shah, PhD, on "Hill Climbing: Best Practices for Evaluating LLMs."
2.  The slide introduces the topic of "Evaluating for Gen AI" and provides a QR code and URL for related GitHub resources.
3.  The slide presents a customer support use case where Gen AI can help agents compose emails.
4.  This slide highlights a common initial thought that using Gen AI for tasks like personalized support emails is easy with a simple prompt, referred to as "Vibe Coding."
5.  This slide provides an example of a well-generated support email acknowledging a delayed order.
6.  This slide provides another example of a well-generated support email acknowledging a damaged product and initiating a replacement.
7.  This slide shows an example of a poor AI response that completely misunderstands an "Order Delay Inquiry" and offers information about new product launches instead.
8.  This slide provides a good example of an AI-generated support email addressing a defective espresso machine and confirming a replacement.
9.  The slide outlines the significant risks of LLM mistakes, categorizing them as Reputational, Legal, and Financial.
10. This image visually represents the despair or frustration that can arise from Gen AI challenges.
11. This slide emphasizes the high failure rate of generative AI pilots in companies, citing an MIT report that 95% are failing.
12. The slide asserts that comprehensive evaluation is crucial for improving Gen AI applications and provides a link to a related YouTube video.
13. This concentric diagram explains that evaluation is necessary because things can easily go wrong, and buy-in is needed from human staff and regulators.
14. Evaluation for production applications should consider Technical (F1), Business ($$), and Operational (TCO) aspects.
15. Public benchmarks offer a general idea of new LLMs' performance, with links provided for further exploration.
16. It's crucial to build custom benchmarks that accurately reflect your specific use case, which are defined as a task, a dataset, and an evaluation metric.
17. This slide sets the stage to "tame Gen AI" through structured evaluation practices.
18. The roadmap outlines the workshop's progression: understanding Gen AI, building an evaluation workflow, adding complexity, and considering agents.
19. This slide demonstrates the difficulty of evaluating Gen AI by showing two different responses generated from the same prompt, highlighting variability.
20. The simple diagram illustrates that even identical prompts fed into a model can produce divergent outputs.
21. The slide highlights the problem of inconsistent scores across different benchmarks for various LLMs, making comparison challenging.
22. An overview of MMLU (Massive Multitask Language Understanding) is provided, detailing its 57 tasks across various domains.
23. Prompt sensitivity is explained, showing that minor formatting changes can lead to a significant accuracy shift (>~5%) on MMLU evaluations.
24. Further prompt sensitivity research details specific formatting alterations (e.g., changing parentheses or adding spaces) that impact MMLU accuracy.
25. A bar chart demonstrates that subtle changes in prompt wording can lead to a 5-10% drop in LLM performance (specifically GPT-4o).
26. This slide presents a graph indicating that the tone of a prompt also significantly affects the accuracy and overall performance of LLMs.
27. The slide reiterates that prompt sensitivity, where simple changes in words affect output, remains a persistent problem in LLM interactions.
28. A tweet illustrates a potential bias in the Falcon LLM, which responded with highly positive sentiment about Abu Dhabi, raising questions about its neutrality.
29. Another tweet provides an example where the Falcon LLM appears to "cover up human rights abuses" in Abu Dhabi, failing to provide critical information.
30. The slide suggests inspecting the model's system prompt to understand its inherent instructions and potential biases.
31. The Claude System Prompt is highlighted as being very long (1700 words, 8-9 minutes of reading), emphasizing the importance and complexity of understanding a model's foundational instructions.
32. The diagram shows that evaluating a single LLM response is complex, involving factors like tokenization, prompt styles, prompt engineering, and the system prompt.
33. A heatmap illustrates the "inter-text similarity" between different LLM models, indicating their diverse response patterns.
34. The slide discusses "Sycophantic Models and Bias," showing how AI assistants can generate feedback that agrees with the user, even if it's not objectively correct.
35. The slide demonstrates "Model Drift" and "LLM Drift," showing how the reliability and performance of commercial APIs can degrade or change over time.
36. This timeline illustrates "Degraded Responses" and performance issues in LLMs, such as output corruption errors and context window routing errors, highlighting the need for continuous monitoring.
37. The slide emphasizes that hyperparameters (like temperature and maximum length) significantly influence LLM outputs, and users should understand their impact.
38. Multiple social media posts illustrate "Non-Deterministic Inference in Practice," explaining that LLMs can produce different outputs even with identical inputs due to inherent stochasticity.
39. The slide acknowledges that addressing "Non-deterministic inference" in LLMs is a recognized challenge, with researchers actively working on it, but it's not an easy problem to solve.
40. The updated diagram expands on the complexity of evaluating a single response by including model selection, hyperparameters, non-deterministic inference, and forced updates as factors within the "Model."
41. The slide demonstrates the importance of specifying output formats for multiple-choice questions, showing how different formatting can lead to evaluation errors.
42. This table shows that different implementations and evaluation harnesses can yield varying outputs and interpretations when evaluating MMLU.
43. A table comparing MMLU scores across various models and evaluation harnesses highlights that achieving consistent results is challenging.
44. This slide provides a table showcasing how different LLMs produce varying sentiment analysis outputs for the same input text.
45. Radar charts illustrate that "Tool Use Adds Another Layer of Variance" to LLM performance across different application areas like email, calendar, file management, and terminal interactions.
46. This comprehensive slide summarizes all the reasons "Why LLM Responses Differ," covering inputs, model internal mechanisms (including non-determinism and updates), output evaluation, tool use, and infrastructure variability.
47. This slide concludes that "Why Evaluation Feels Chaotic – and That’s Okay," acknowledging the complexity while presenting a chart of various generative AI evaluation methods based on flexibility and cost.
48. This slide marks a transition to finding "From Chaos to Control – Where to Begin" in the evaluation process.
49. The slide shows an example of how to "Build the evaluation dataset" by listing various prompts for tasks like summarization, extraction, and translation.
50. This slide demonstrates how to "Get Labeled Outputs" by providing the "Gold Output" for each prompt in the evaluation dataset.
51. The slide illustrates how to "Compare to your Model Output" by adding a column for the LLM's generated responses alongside the Gold Output.
52. The slide explains the importance of "Measure Equivalence, Not Exact Matches," using an LLM Judge to score the model's output for semantic equivalence against the gold output.
53. This slide demonstrates how to "Optimize Using Equivalence as Your Metric," showing two configurations (Config A and Config B) with different equivalence scores.
54. The slide explains "Why Global Metrics Don’t Tell the Whole Story," noting their benefits in measuring overall performance but also their limitations in capturing specific nuances or lacking gold answers.
55. This slide advocates for moving "From Global to Targeted Evaluation," stating that maximizing performance requires a deep understanding of the data and identifying specific errors.
56. This slide serves as a transition to the topic of "Building Tests" for LLMs.
57. The slide emphasizes starting with clear "Good Example" and "Bad Example" definitions to guide the desired output quality.
58. The slide encourages users to "Develop an Evaluation Mindset" by observing real-world user problems and interactions.
59. The slide stresses the importance of "Collaborate with Domain Experts and Users" for testing examples and naive bootstrapping to ensure relevant and effective evaluation.
60. The slide advises to "Identify and Categorize Failure Types" by reviewing data and grouping common errors like harmful content, bias, or incorrect information, providing an example chart of error categories.
61. The slide demonstrates how to "Define What Good Looks Like for Your Use Case" by contrasting good and bad examples and outlining specific areas of evaluation focus (e.g., length, tone, context).
62. This slide presents a table showing how to "Document Every Issue and Failure" with human evaluation for each response.
63. The slide suggests that "Good Evaluation Tooling Can Help," showing an example of a custom chat viewer for collecting feedback (but warns against getting sidetracked by tooling).
64. This slide demonstrates how to "Build Your First Test – Length Check" using Python code to evaluate if an email response's word count is acceptable.
65. The slide explains how to "Build Your Second Test – Tone and Style" using an LLM to act as a judge to identify the tone of generated text.
66. This table extends the issue documentation by adding quantitative metrics, `Length_OK` and `Tone_OK`, to each response.
67. The slide emphasizes the importance of "Check LLM Judges Against Humans" to ensure alignment in evaluation, noting that high agreement can be achieved but vigilance is needed.
68. The slide illustrates "Self-Evaluation Bias in LLMs," showing a matrix where models tend to rate their own performance higher than other models or human judges.
69. The slide provides guidelines for "LLM Judges - Check Alignment," highlighting that models can align with humans and advocating for continuous alignment checks.
70. This slide details various known "Biases in LLM Judges," listing different types of biases that can influence their evaluation outcomes.
71. The slide presents "Best Practices for LLM Judges," including calibration with human data, using ensembles, avoiding relevance evaluations, conducting human spot-checks, using discrete ratings, and monitoring for concept drift.
72. This slide illustrates "Error Analysis Using Test Cases" by showing a bar chart that plots failed cases for different models across various categories (e.g., length, tone, professional, context), indicating areas for improvement.
73. Similar to the previous slide, this chart shows "Error Analysis Using Test Cases" comparing two different prompts (Prompt A and Prompt B) on various failure categories.
74. The slide suggests using "Explanations to Guide Improvement," showing how equivalence metadata and explanations from an LLM judge can clarify why responses failed.
75. The slide discusses the "Limits to Model Explanations," reminding that what an LLM explains it is doing is not always exactly what it is doing.
76. The slide proposes to "Build an Evaluation Flywheel," an iterative process of analyzing, improving, and measuring to continuously refine LLM applications.
77. This slide introduces the concept of "Building Even More Tests" by presenting a use case for assessing the style of a financial analyst agent's response.
78. The slide asks, "Use a Global Test?" and provides an example of a broad evaluation question for a financial analyst's language.
79. The slide differentiates "Global versus Unit Tests," providing an example of a broad global test and then breaking it down into specific, measurable unit tests for aspects like context, clarity, and compliance.
80. This slide illustrates "Scoring Global and Unit Tests," showing how a detailed text-based global assessment can be complemented by quantitative unit test scores visualized in a radar chart.
81. The slide explains "Analyzing Failures with Clustered Patterns," using K-means to group and identify different types of LLM failures, such as synthesis, context, hallucination, and incomplete retrieval errors.
82. The slide provides advice on "How to Design Good Unit Tests," emphasizing characteristics like focus, specificity, unambiguous language, assessing desirable qualities, and using small, discrete rating ranges.
83. The slide provides "Examples of Global to Unit Tests" categorized under Legal, Retrieval, and Bias/Fairness, detailing specific sub-metrics for each.
84. This slide illustrates how "Unit Tests to Evaluate New Prompts" are used, showing a bar chart of average scores across different test categories derived from a "good" system prompt.
85. The slide cautions that "Evaluation Tools – No Silver Bullet," advising to master basics first, then log traces/experiments, and to always practice dataset versioning.
86. The slide uses the analogy of "Forest: Global / Integration" and "Trees: Test Case / Unit Tests" for effective "Error Analysis."
87. An "Error Analysis Tip" is provided: compare performance by changing only one setting at a time.
88. This slide lists key "Error Analysis Tips": ablation-style changes, categorizing failures, using examples, and leveraging logs and traces.
89. The slide illustrates "The Evaluation Story We Tell" as a linear progression of accuracy improvement over time, from out-of-the-box performance to specialized applications, user feedback, and expanded topics.
90. The slide presents "The Reality of Progress" as non-linear, highlighting that optimization involves continually evolving paths with varying success for RAG, prompt engineering, and fine-tuning.
91. The slide depicts "Evaluation is a Continual Process" as a cyclical workflow involving problem identification, data collection, optimization, user acceptance testing, and iterative updates.
92. The slide uses the common idiom, "How do you eat an elephant?" as a metaphor for tackling large, complex evaluation tasks.
93. The slide answers the "elephant" metaphor by explaining "Adding Tests Over Time," breaking down the "GenAI Evaluation Elephant" into smaller, manageable "bites" or tests that are gradually introduced.
94. The slide summarizes "Doing Evaluation the Right Way" by listing best practices such as using annotated examples, systematic documentation, continuous error analysis, collaboration, and awareness of generalization/overfitting.
95. This slide introduces the concept of "Agentic use cases," using the dragon metaphor to symbolize new complexities.
96. This slide poses a conceptual problem for an agent, "How should it cross the river?", highlighting decision-making in agentic workflows.
97. This complex flowchart illustrates a "Chat-to-purchase Router" as an example of an agentic workflow, detailing the interaction of LLM calls, internal APIs, and application code.
98. This flowchart demonstrates a "Text to SQL Agent from Snowflake," showcasing another complex agentic workflow with classification, feature extraction, content enrichment, SQL generation, and error correction.
99. The slide illustrates "Evaluating Office-Style Agent Workflows (OdysseyBench)" by showing typical failure cases in agent tasks like converting PDFs, creating folders, using tools, and planning actions.
100. The slide outlines "Error Analysis for Agentic Workflows," focusing on assessing overall performance, routing decisions, and individual agent steps to identify where and why failures occur.
101. This slide explains "Evaluating a Workflow Instead of a Response" by showing a flowchart of a conversational flow and its evaluation against success criteria.
102. The slide discusses that "Agentic Frameworks Help – Until They Don’t," highlighting their benefits in abstraction but also their drawbacks when they break, become outdated, or require customization.
103. The slide presents diagrams illustrating "Abstraction for Agentic Workflows," showing the trade-off between domain-specific intelligence (workflows) and general intelligence (agents) for cost efficiency and branching.
104. The slide explains "When Agent Abstractions Break Down," differentiating between declarative and non-declarative graphs and the challenges in managing dynamic and complex agent workflows.
105. The slide lists key "Lesson from Reproducing Agent Benchmarks," including standardizing evaluation, measuring efficiency, detecting shortcuts, and logging real behavior beyond just accuracy.
106. The final slide, "We did it!", concludes the presentation and provides links to the code and slides.