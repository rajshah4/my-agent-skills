---
title: "From Vectors to Agents: Managing RAG in an Agentic World - Full Talk"
date: 2025-10-27
video: https://youtu.be/AS_HlJbJjH8
author: Rajiv Shah
type: annotated-transcript
---

Retrieval Augmented Generation (RAG) has moved rapidly from simple demos to complex, agentic systems. In this comprehensive technical talk, Rajiv Shah takes us on a journey through the evolution of RAG, focusing specifically on the nuances of retrieval strategies.

Moving beyond the basic "vector search" tutorial, this session dives into the practical realities of production RAG: the trade-offs between BM25 and semantic search, the rise of agentic reasoning for information retrieval, and how to manage cost and latency in high-stakes environments.

Below is the full, annotated transcript of the presentation, complete with all 71 slides from the original deck to help you follow along with the technical concepts and benchmarks discussed.

---

## Introduction to RAG and the Problem Space

![Slide 1: Title - From Vectors to Agents](images/slide_1.png)
*Rajiv Shah introduces the session on managing RAG in an agentic world.*

[00:00:00](https://youtu.be/AS_HlJbJjH8?t=0s) Are you ready for a deep dive into rag, especially around retrieval? What I want to do today is talk to you about what the problems are with rag, how you scope out rag use cases, but most of what we're going to focus on is a technical deep dive around some specific retrieval approaches, BM25, language models, and then finally, agentic search and rag.

![Slide 2: ACME GPT Logo](images/slide_2.png)
*The ubiquitous "ACME GPT" represents the standard starting point for many organizations.*

[00:00:22](https://youtu.be/AS_HlJbJjH8?t=22s) This is a presentation I gave recently at a conference at the MLOps conference. What I'm going to do today is going to go a little bit faster through the content. You're going to miss some of the jokes, some of the setups like that, but I want to give everybody a chance to understand some of the content that I was able to share out there. Now, to start out with, I like to focus on where we are with Rag today. And lots of folks are out there kind of building their own RAG solutions because after all, we see chat GBT, you're inside a company, you want to be able to ask questions, right?

[00:00:55](https://youtu.be/AS_HlJbJjH8?t=55s) No, the CEO wants to know, hey, can I get the list of board of directors from your fancy chat GBT solution? And you quickly find out, no, it doesn't because you need your enterprise knowledge in there.

![Slide 3: Simplified RAG Flow](images/slide_3.png)
*A high-level view of the standard RAG process: Query -> Retrieve -> Generate.*

[00:01:10](https://youtu.be/AS_HlJbJjH8?t=70s) All of you probably at this point know, right? You can build a very easy rag demo out of the box by just grabbing some data, using an embedding model, creating vectors, doing the similarity. The code is out there.

![Slide 4: Python Code Snippet for Basic RAG](images/slide_4.png)
*A typical LangChain implementation of a basic RAG pipeline.*

[00:01:23](https://youtu.be/AS_HlJbJjH8?t=83s) Many of us have kind of run through code like this before where we take our information, we chunk it down, we can then retrieve it, pass it to a language model. I'm going to assume everybody here kind of knows the basics for kind of building rag. And it's easy to build a rag solution like this. But where I come in and hope why you're probably here is you know that the reality is you can build that quick demo but as you try to move that into production you figure out that the accuracy of what you did isn't that great because maybe you focused on some using some synthetic data to generate to evaluate your model that was based around simple extraction but your users ask much more complex type of questions.

![Slide 5: Why RAG Projects Fail](images/slide_5.png)
*The harsh reality: 95% of Gen AI projects fail due to accuracy, latency, scaling, and cost.*

[00:02:05](https://youtu.be/AS_HlJbJjH8?t=125s) So your accuracy drops as soon as you move it into production. Or it could be you had so many calls that the latency is just unbearable and your users don't want to wait that long. It could be just a problem of scaling, right? Going from a 100 documents to a,000, 10,000, a million documents. Lots of issues around scaling there that happen. Finally, it's the cost, right? Your demo works great, but we're seeing a lot of push back in enterprises as you built a very complex multi-agent rag system that all of a sudden each query costs like a dollar for each search. It's like it's crazy. And then finally, and this is the thing most people miss, but inside an enterprise, not everybody gets to read every document. You need to have some way to work with compliance, some method for entitlements. So, not everybody can see every document like that.

![Slide 6: RAG Variations and Techniques](images/slide_6.png)
*The landscape of RAG techniques is vast, leading to analysis paralysis.*

[00:03:00](https://youtu.be/AS_HlJbJjH8?t=180s) And I know I say this and many of you will scour and look at your algorithms and be like, well, you know what, Raj, I'm just going to go search out on archive and there's got to be a better paper out there. And there's lots of papers out there on rag like that. But what I want to do is the answer is not in here of pulling together like a bunch of archive papers and doing this. So I want to give people a framework for thinking through how to solve the rag problems and not ending up with something that looks like this.

![Slide 7: The "Ultimate" Over-Engineered RAG](images/slide_7.png)
*A humorous look at trying to combine every possible algorithm into one system.*

## RAG as a System

[00:03:33](https://youtu.be/AS_HlJbJjH8?t=213s) So as a starting point, let me give you the idea first of all is you have to think of rag as a system. It's not just one or two models. You're going to have a lot of different parts together as you build a rag production system.

![Slide 8: Comprehensive RAG System Diagram](images/slide_8.png)
*RAG is a multi-stage system involving parsing, querying, retrieving, and generation.*

[00:03:46](https://youtu.be/AS_HlJbJjH8?t=226s) And that involves parsing the documents cleanly getting it out. something that's vastly overlooked, but especially when you get to complex documents, you need a good system for getting that information out cleanly. How you query your documents, the retrieval, finding those chunks, and then generating a response. So, this out here is kind of a baseline system for today. What I want to first do is talk about how we figure out where to improve and what type of system we need.

![Slide 9: RAG Design Framework](images/slide_9.png)
*Balancing problem complexity against latency, cost, and the cost of mistakes.*

[00:04:18](https://youtu.be/AS_HlJbJjH8?t=258s) And this is where like whenever somebody comes to me with a rag problem before we jump into the technical details, I like to know what are the trade where are they thinking in terms of tradeoffs. Right? This is just like like another engineering problem where you have to think about how quickly you want something. What's the cost going to be? And instead of accuracy here, I'm using problem complexity. And if you can't have that serious discussion with your users and know what the trade-offs are, it's going to be hard to actually build a useful solution. So have that upfront conversation. Set your expectations of users.

![Slide 10: RAG Considerations Matrix](images/slide_10.png)
*Mapping generation types from simple facts to reasoning based on query complexity.*

[00:04:57](https://youtu.be/AS_HlJbJjH8?t=297s) One thing that often comes up in Gen AI is the cost of a mistake. Often where you're going to get implemented in today's generative AI because they are mistakrone is in places where it's easy to make mistakes. So this is why you see codebased tools, codebased assistant tools happening all the time because developers can quickly check the mistake while building a rag system that might be a life and death something for patients in a healthcare medical might be a little bit harder because of the cost of the mistakes. But that should be a rough proxy for telling you like how what you're going to have to do to get this into production.

![Slide 11: Increasing Query Complexity](images/slide_11.png)
*Examples ranging from simple keyword searches to multi-hop and agentic scenarios.*

[00:05:33](https://youtu.be/AS_HlJbJjH8?t=333s) Now, to give you a sense of kind of some of the trade-offs that we have, this is something I made I made this like probably a year ago for our sales team. Like my day job is helping to kind of work with customers on building kind of rag solutions. I've been doing this for years all the way back to when I was at HuggingFace. And so I built this for the sales guy. This this chart on the right just I use chatbt to build this. But the idea here is to have that conversation about what type of queries, what type of things people are going to use this rag system for. And that way you can figure out what is the complexity, what are the nuances that you're going to have to consider.

[00:06:10](https://youtu.be/AS_HlJbJjH8?t=370s) Understanding this upfront before you start getting into the details of of designing your rag system is very important and could save you a lot of heartache. Like one thing I like to do is just know what kind of queries do we expect from people because as we talk about queries, they have a lot of different complexity where you could have very simple keyword queries, right? This will work very great. But on the other hand, maybe your users don't know the exact keywords and you're going to have some type of semantic variation where they're going to say how much bank instead of just the total revenue. Or maybe your users have queries where they expect a little bit of complexity of hopping from get solving one part of the question going to the next part. Or maybe the questions answers are in multiple documents. Or and this is the one that often happens a lot of times the answers aren't in the documents that they give you that they're all of a sudden they're asking for knowledge that's outside. I see this happening all the time and it's something again to get ahead of to figure out how you want to solve it. And then finally nowadays we are used to these thinking LLMs. People are asking much more broader questions that call for agentic scenarios. Each of these things will come with consequences for how we design our systems like that.

## Deep Dive: Retrieval Approaches

![Slide 12: Focusing on Retrieval](images/slide_12.png)
*Zooming in on the "Retrieval" stage of the RAG diagram.*

[00:07:32](https://youtu.be/AS_HlJbJjH8?t=452s) Now today I'm going to focus on the retrieval part of this diagram. And I do this because this is where I see a lot of confusion, uncertainty. I people don't know exactly what type of models to pick out. They're a little bit overwhelmed at all the different architectures and different choices. And I see a lot of stuff out on the internets, on the LinkedIn, the X's where there's a lot of different philosophies, developers, companies putting out kind of ideas like that. And I want to give people a good solid practical way to start with retrieval before jumping into all types of alternative approaches like that. So this is where we're going to focus on retrieval. We're going to stick to the basics here.

[00:08:16](https://youtu.be/AS_HlJbJjH8?t=496s) And retrieval again is about I have a document. I've broken it down into pieces, right? We need to break these things down into pieces. You're not going to have one model that can hold them all. If you just think about the extreme case, imagine you had one model that had like a 10 million context length that could hold everything. Would it really make sense to run that for every query? the amount of compute to do that. No, no, no. We want to be compute efficient. It makes sense to break our documents into pieces using a chunking approach like that. This is why retrieval rag is always going to be around.

![Slide 13: Three Main Retrieval Approaches](images/slide_13.png)
*The three pillars: BM25 (keyword), Language Models (semantic), and Agentic Search.*

[00:08:52](https://youtu.be/AS_HlJbJjH8?t=532s) We're going to talk about BM25. We're going to talk about language models and agentic search. And since this is a video where you can skip ahead, I'm going to just keep going.

![Slide 14: Code Snippet - Retrieval Focus](images/slide_14.png)
*Highlighting the specific lines of code involving embeddings and vector databases.*

[00:09:01](https://youtu.be/AS_HlJbJjH8?t=541s) Now, if you think about it in terms of code, this is kind of the area of the steps that we're working in where we've chunked down the data. The next step is figuring out what the relevant chunk is to pass into our generator model. A lot of approaches here. I want to start with BM25.

### BM25: The Strong Baseline

![Slide 15: BM25 Explanation](images/slide_15.png)
*BM25 is a probabilistic lexical ranking function based on keyword indexing.*

[00:09:20](https://youtu.be/AS_HlJbJjH8?t=560s) BM25 stands for best match 25. So, it's a lexical type of search. And it took a couple iterations for them to get there. This is the 25th, right? This is a crafted formula that takes a look at all the words that are in a document and creates this inverted index. And so you can see it right here in the middle where like for every word we know which documents it goes to. So then right if I have a search and I need to f figure out I have a query that has about butterfly now I can figure out what is the relevant document that has butterfly right like this is a very nice way of doing this and to give you a sense of like how quick and how fast it is I kind of use chatbt to get a quick benchmark so all of these numbers were just generated using the models which is why I don't have a ton of code for you because you can easily get the models like this so I had to create a synthetic set of a,000 3,000 9,000 documents.

![Slide 16: BM25 vs Linear Search Scaling](images/slide_16.png)
*BM25 scales efficiently with document count, unlike linear search.*

[00:10:19](https://youtu.be/AS_HlJbJjH8?t=619s) The first thing I did was I ran a linear search. So a linear search is just like when you use Ctrl+F find and you look for one after another after another after another. So imagine looking for that word butterfly right through each document one time after time. And you can see right that scales as you import documents. It's going to scale and go much slower. And it's pretty slow. As soon as you get to right a thousand documents, you can see it already takes 3,000 seconds to do that. On the other hand, if we use this idea of created this inverted index and then use the BM25 algorithm which works off that inverted index, you can see it's much much faster, right? Several orders of speed, much faster, which is why this is a widely used approach like that.

![Slide 17: BM25 Failure Cases](images/slide_17.png)
*Lexical search fails when synonyms or aliases are used (e.g., "Physician" vs "Doctor").*

[00:11:08](https://youtu.be/AS_HlJbJjH8?t=668s) So, what's the rub? Why aren't we using this all the time? Well, this is great at keywords, but here's the thing is sometimes the queries, the things we look for don't exactly match up in a lexical one-on-one overlapping way. Somebody asks, in this case, for a physician, but all the documents have the word doctor or somebody asked for international business machines, but the documents use IBM. So these are the failure words of this kind of strict lexical approach. Now nevertheless this is a very strong baseline. In fact when we talk about these neural network methods many of these methods the BM25 can beat on lots of different types of corpus. So depending on the type of documents and the type of queries you have this can be a good fit. Can give you a pretty good baseline like that. especially if you have users that already kind of know the words that they're looking for like that. And as we'll talk about later in a gentic search, it might be sufficient for a lot of cases.

![Slide 18: BM25 Python Implementation](images/slide_18.png)
*Resources for a high-performance Python implementation of BM25.*

[00:12:14](https://youtu.be/AS_HlJbJjH8?t=734s) For those of you who want to play around with this, there's an implementation of BM25 in Python that you can go and grab and play around with.

### Language Models & Embeddings

![Slide 19: Text to Embeddings](images/slide_19.png)
*Language models convert text into dense embedding vectors via a neural encoder.*

[00:12:24](https://youtu.be/AS_HlJbJjH8?t=744s) Now I want to enter language models. So the idea of language models is what we can do is we can take our text that we have, we pass it through an encoder, right? It's an encoder because it's encoding all of our text into into into numbers. And with that encoding, then we're going to be able to use that as a way to search.

![Slide 20: Semantic Similarity in 2D](images/slide_20.png)
*Visualizing how embeddings group related concepts (like Doctor and Physician).*

[00:12:47](https://youtu.be/AS_HlJbJjH8?t=767s) And the great way is because the language models are trained on lots and lots of data, they've seen a lot of the world, they have an idea of these similar concepts. So when for example I search for physician what I can do is in that same latenc number that we've created from the embedding the word doctor is very close by right international business machines is very close to IBM this is basic semantic search stuff it works really well which is why it was a big deal for Google when they added it they had great results with it.

![Slide 21: Widespread Use of Semantic Search](images/slide_21.png)
*Semantic search is now standard, with many models available on Hugging Face.*

[00:13:22](https://youtu.be/AS_HlJbJjH8?t=802s) It's also very popular. If you go over to hugging face, you'll see these models are widely deployed. So this is all kind of baseline knowledge that you should have. Now the question though a lot of people have is like okay Raj you told me this but like which one of these should I use.

![Slide 22: NanoBEIR Benchmark Scatter Plot](images/slide_22.png)
*Comparing inference speed vs. accuracy (NDCG@10) across various models.*

[00:13:38](https://youtu.be/AS_HlJbJjH8?t=818s) So now let's look at the data here. If we look at this graph we'll see there's two axes. One is CPU inference speed and this is just basically how fast it goes right faster to the right slower to the left and could have been GPU. I just used CPU implementation here for this this what is this NCDG thing all this so NCDG is a retrieval metric it's the quality of how good the results come back nano is a small version of BEI B beer BIR which is a benchmark for information retrieval so this is basically a quality score on a benchmark for testing out information retrieval so the higher you get the better your job you're doing at retrieval so I've given you the big map. So, I started helping you here by putting where BM25 is, right? You can see it's over to the right, right? It's one of the faster approaches as we talked about, but right in terms of retrieval quality, it's not necessarily the best.

![Slide 23: Static Embeddings (Model2Vec)](images/slide_23.png)
*Static embeddings are fast and lightweight but lack contextual awareness.*

[00:14:40](https://youtu.be/AS_HlJbJjH8?t=880s) But look, is it is it the fastest? No. There's even a faster way that I want to show you, which is using static embeddings. What a static embedding is is is for every word is going to have a unique num numerical embedding. So this is very similar to older approaches like word tovec that you might have seen. So here for example the word happy the word joy has a kind of a meaning. You can run this really quickly. It's super fast. You can even run this on kind of CPUs. Now the downside of kind of using the static embeddings is many words have multiple meanings right like you have to look at the context to understand that and so this approach is going to lose out in some of those cases where that context matters for understanding the meaning here right so model for example can mean right a statistical model that most of us are used to in kind of AI and data science but if you're in fashion Right? Model has a very different meaning like that.

![Slide 24: Word2Vec vs Transformers Cartoon](images/slide_24.png)
*A humorous look at how Transformers capture sentence-level context better than Word2Vec.*

[00:15:48](https://youtu.be/AS_HlJbJjH8?t=948s) So this is where the context matters and where our retrieval quality can suffer is because people ask questions that have different ways.

![Slide 25: Embedding Model Landscape](images/slide_25.png)
*Revisiting the scatter plot: a vast array of models with different performance trade-offs.*

[00:15:59](https://youtu.be/AS_HlJbJjH8?t=959s) And this is where there's a lot more models that are available way over here to the left. And you can see some of the names out here. And they differ of course in retrieval quality. They differ in speed. Right? If you think about this, and we'll talk about why is this one way over here that's super super super slow. Well, and it's a bigger model takes a lot more compute to run. So now you're going to ask me, all right, so you got me a ton more models here. How am I going to figure out kind of which model to run?

![Slide 26: MTEB/RTEB Leaderboard](images/slide_26.png)
*The Massive Text Embedding Benchmark (MTEB) on Hugging Face tracks performance.*

[00:16:35](https://youtu.be/AS_HlJbJjH8?t=995s) Well, the folks over at HuggingSpace hosts a couple of leaderboards. So this is the multi-ext embedding leaderboard. And now the retrieval embedding leaderboard that has hundreds of models out there. And I want to take a minute here and show you. I'm going to flip over on my web browser. This is what the front page of the leaderboard looks like. So here, for example, I'm looking at the multi-lingual part of the leaderboard. Um, you'll see there's many many models here. I think on the there's the order of like 300 models. And the great thing is is is not only do you get the basic characteristics what are the embedding dimensions what are the tokens of that but you get all this look over to the right you get all these scores here as well. So these are how this model performs on some public data sets that are out there and it gives us a rough gauge for being able to compare different models. And so this is where you can now pick the model that best kind of fits your use case. And as you would kind of explore this, you'll see that there's many different kinds of ways to kind of break up these these embedding models and look and find the right one.

![Slide 27: Embedding Model Selection Chart](images/slide_27.png)
*A bubble chart helping select models based on accuracy, latency, and compute.*

[00:17:49](https://youtu.be/AS_HlJbJjH8?t=1069s) Recently, what what's happened is is we've they've introduced a new one here, the the retrieval embedding leaderboard. And I'm going to click on this one here. And with the retrieval embedding leaderboard, there it goes. The retrieval embedding leaderboard's a little bit different and it's going to have a subset. It doesn't have all the models yet, but it has one important difference. And the multi-ext embedding leaderboard all showed public data sets performance. What the retrieval embedding leaderboard is going to show is it shows performance on a private held out data set. And this is important because this keeps us from keeps people from kind of gaming the system and maybe training on the exact same data that's there. Unfortunately, this thing is taking forever to load today. Um, like that. So, let me stop and wait for it to load. And there you can see that you can see the private scores right here for that leaderboard as well.

![Slide 28: Additional Model Considerations](images/slide_28.png)
*Factors beyond score: model size, dimensions, and training data.*

[00:18:58](https://youtu.be/AS_HlJbJjH8?t=1138s) Now there's a ton of tools here that you can use to help kind of look at the leaderboards to figure out kind of what's important like that. One of the things that often comes into mind for as you're picking these is the size of the model of the size of the model because the size of the model will directly have to do with compute. Now, when I when I do this in in in a classroom setting or a workshop, I have a little more fun. But what I want to point out here is take a look here. You'll see that there's a bunch of models here that are all the same size, right? So, it takes the same amount of compute to run these models, but the performance over here on the mean differs. And the reason why and I'll give you one second if you want to pause and come up with your own explanation is the models have improved for the same size models people have evolved better training strategies for example improved architectures and so we have kind of a newer generation of models where we have a slight improvement um like that. So this is one of the great things we'll talk about here is these things are moving along as well.

[00:20:08](https://youtu.be/AS_HlJbJjH8?t=1208s) Now, as you start thinking about them, there's of course the accuracy of the models, how well they perform on the task, the latency and compute. All of these things are tied together. You'll want to think about, hey, is this an open source model? Can I go and quantize it maybe to get a little bit of extra speed? I'll think about the embedding dimension. Is this a small kind of embedding of 128 or is this kind of a gargantuan one? Because I'm going to have to manage and store all that stuff as well. When you're starting to look deeper into these models, you can look at, for example, some of them have trained differently, multilingual, for example, or maybe there's a specific domain. Maybe you're going to go and fine-tune the model. A lot of kind of different considerations that come into place like that.

![Slide 29: Matryoshka Embedding Models](images/slide_29.png)
*Matryoshka models allow truncating embeddings to smaller dimensions without losing quality.*

[00:20:53](https://youtu.be/AS_HlJbJjH8?t=1253s) One kind of neat kind of innovation that I want to highlight here is these the matriosia embedding models where a lot of embedding models initially came with one dimension. So when you passed in your information out came one token one embedding um output of a fixed length. What the match should let us do is let us pick we can pick smaller lengths like that. So this can be more convenient for storage or for compute that we're doing but the models have been trained. So even if you go down to let's say 64 the retrieval quality is still high. I believe the open AI models also support this capability as well. So it's kind of an interesting thing I like to kind of highlight for folks um with these models.

![Slide 30: Sentence Transformers](images/slide_30.png)
*Models optimized for sentence-level meaning and semantic search.*

[00:21:42](https://youtu.be/AS_HlJbJjH8?t=1302s) Now as you start using these models, one of the most dominant models you will see are sentence transformers for retrieval tasks. And these work great because if you think about most of the documents you write you you read that you're using for retrieval, they're probably all like written in sentences. Well, the sentence transformer has been drained to work with documents, not at like the individual token level, but in terms of sentences. So, it works a lot better kind of for retrieval. And you'll see these widely used inside of RAG systems like that.

### Improving Precision: Rerankers

![Slide 31: Cross-Encoder Architecture](images/slide_31.png)
*A two-stage process: fast retrieval followed by precise reranking.*

[00:22:16](https://youtu.be/AS_HlJbJjH8?t=1336s) A second model you'll see is the cross encoder or often as we use it in rag, we often call it a reranker because that's the function it has inside there. And what the cross encoder does is it crosses two things. It crosses the incoming embedding that we have with the query that's coming in. So maybe your retriever found a bunch of chunks. We cross that chunk with the query.

![Slide 32: Reranker Architecture (Detail)](images/slide_32.png)
*Emphasizing the interaction between query and document in the cross-encoder.*

[00:22:41](https://youtu.be/AS_HlJbJjH8?t=1361s) And what that does is you can use that cross encoder to get a score to see how similar they are. And what we do is we'll then use that to check each one of those embeddings. And that will often lead to a reranking stage where we find out the relationship of that query is a little bit better to some chunks.

![Slide 33: Reranker Accuracy Boost](images/slide_33.png)
*Adding a reranker significantly improves accuracy in large models like Llama 3.1.*

[00:23:00](https://youtu.be/AS_HlJbJjH8?t=1380s) And what we can do is we can get a slight improvement in performance like that. So this is widely used um in that. And you'll see you typically get a little bit of a bump by using a reranker but like everything right it doesn't come for free.

![Slide 34: RAG Latency Flow](images/slide_34.png)
*Reranking is computationally expensive, adding nearly 30% to total latency.*

[00:23:15](https://youtu.be/AS_HlJbJjH8?t=1395s) There's often kind of some type of latency gain. And again the numbers here I'm just to give you the ideas. You can of course pick re-rankers of different um that of different sizes and different kind of latency effects like that.

![Slide 35: Colab Notebook for Retrieve & Re-Rank](images/slide_35.png)
*A hands-on example of implementing retrieve and rerank on Wikipedia data.*

[00:23:28](https://youtu.be/AS_HlJbJjH8?t=1408s) Now I have a an example kind of collab demo that I taken from somebody else but it's a nice walkthrough to kind of give you a sense of like what the value is of a reranker how to kind of use one just all runs inside Google collab um for those who want to kind of play around with the code a little bit.

![Slide 36: Instruction Following Reranker](images/slide_36.png)
*Rerankers that accept natural language instructions to bias results.*

[00:23:47](https://youtu.be/AS_HlJbJjH8?t=1427s) Couple of other things. I work at Contextual. We launched an instruction following reranker. It is out there on hugging face. You can use it for free if you're in a company um that's for research, but if you want to actually use it, you got to pay for it. Um but the key thing here is it allows you to send an instruction or a prompt for how you want that ranking to happen. So you can prioritize different types of information. This gives you another kind of knob when you're thinking about these reranking models.

### Advanced Retrieval Strategies

![Slide 37: Combining Multiple Retrievers](images/slide_37.png)
*Using multiple retrievers (BM25 + Semantic) improves recall.*

[00:24:20](https://youtu.be/AS_HlJbJjH8?t=1460s) Now, a lot of retrievers, I showed you a lot of methods before. Well, you know what? You don't have to use them by themselves. You can combine them. So, here, for example, you can see here some combinations of maybe I use BM25 with something else. Maybe I used E5 with the re-ranker. Or maybe, right, like you go crazy and I'm like, shove them. You put them all together, right? They did a fusion here and re-rank all the way, right? You can do that, but just remember, right, like you got to engineer this. You're going to have to pay for the compute. You're going to have to keep track of everything if you want to use multiples. But you have a lot of flexibility when it comes to these retrievers depending on your needs, right?

![Slide 38: Cascading Rerankers (Kaggle)](images/slide_38.png)
*A Kaggle competition example using cascading rerankers to refine results.*

[00:24:56](https://youtu.be/AS_HlJbJjH8?t=1496s) Like if you look over at the folks at Kaggle, they'll do some crazy stuff like this. In a recent Kaggle competition, this person used three different rerankers to get to the final kind of list where they went from 64 to eight to five to rank the top five like that. So depending on what you need, there's a lot you can do against it.

![Slide 39: Best Practices: Hybrid Search](images/slide_39.png)
*The gold standard: Semantic + Lexical Search + Fusion + Reranking.*

[00:25:16](https://youtu.be/AS_HlJbJjH8?t=1516s) But my best practice always is use a hybrid search. So semantic and lexical, fuse those together, right? Reciprocal rank fusions easily out there. Pass it through a reranker. That's going to give you pretty good standard performance out of the box. And this is a great place as a baseline to set before you kind of jump into lots of alternative approaches um like that.

![Slide 40: Taxonomy of Embedding Models](images/slide_40.png)
*Categorizing models by speed, accuracy, and use case.*

[00:25:42](https://youtu.be/AS_HlJbJjH8?t=1542s) So a lot of different families of models tried to cover all these. If not kind of send your questions and comments like that.

![Slide 41: New Embedding Models](images/slide_41.png)
*Recent innovations from IBM, Google, and others.*

[00:25:50](https://youtu.be/AS_HlJbJjH8?t=1550s) And this is an area of course with embedding models where you see kind of newer embedding models coming out just in the last couple weeks. The folks over at John Hopkins, IBM, Google all released models. I would tell you though as a practitioner it there is a slight improvement enough where you want to use the latest models but like it's not a gamecher. I wouldn't like go rip up something you have to install kind of a newer model as well. So the improvements are very incremental at this point.

![Slide 42: Other Retrieval Methods (SPLADE, ColBERT, GraphRAG)](images/slide_42.png)
*Acknowledging other advanced flavors of RAG.*

[00:26:18](https://youtu.be/AS_HlJbJjH8?t=1578s) Now there's a lot of other retrieval methods like I'm only taking like maybe an hour of time. We could easily do a six-hour workshop on everything in rag. So, splade for example is a very popular way for kind of sparse um sparse retrieval methods where what you do is you add a few other kind of related synonyms inside your inside your lexical search area at as a way to improve it. There's other things like coar which is named after the late night talk show host late interaction approach. There's graph rag where you spend a lot of time upfront like creating this whole graph network and all the entities relationships like there were some funny kind of tweets on X about like the fact that everybody talks about graph rag but nobody actually implements it or uses it. There's tons of other rag flavors out there. Will they work for your use case? Absolutely they may. But again like I'm giving you a good baseline. Use that as a starting point to decide like hey where are we lacking? Where are we failing? Will one of these methods kind of fit where the gaps are that we have like that before just start before just start following kind of the flavor of the week that you see out there.

### Operational Concerns

![Slide 43: Vector Storage Systems](images/slide_43.png)
*Comparing FAISS, Pinecone, and ChromaDB for performance and latency.*

[00:27:30](https://youtu.be/AS_HlJbJjH8?t=1650s) In terms of operational concerns, a couple of things I want to mention is there are optimized libraries for doing some of this stuff. So face for example from Facebook is widely used for kind of computing embeddings. The other thing is depending on the amount of embeddings you have, the amount of documents, you might be able to just store them in memory. For a lot of use cases, you can just buy a big processor, store them in memory, load them up, run what you need to like that.

![Slide 44: Layered Vector Storage Architecture](images/slide_44.png)
*Optimizing storage with hot, warm, and cold data tiers.*

[00:27:55](https://youtu.be/AS_HlJbJjH8?t=1675s) On the other hand, other use cases, you're like, I want a database. I want someplace I can manage that, be able to keep updates and do all of that. Sure, absolutely. And there's a ton of vector database options and I do not pretend to tell you kind of where to go in terms of that. I've linked one of the an article that I found in here. A big part of when you pick out vector databases is thinking about what is your latency requirements for that, right? Because that's going to govern the the kind of a choice of it. But a lot of the standard databases out there, the snowflakes of the world for example, now give you some way to kind of store your embeddings and vectors there as well.

![Slide 45: Datastore Size vs Performance](images/slide_45.png)
*As data size grows, simple retrieval performance degrades.*

[00:28:40](https://youtu.be/AS_HlJbJjH8?t=1720s) All right. Um, one other thing is is as you kind of when we talk about these retrieval methods, what we typically find is that as your information grows, your those retrieval methods, you're going to have to lean on much heavier for you. And this is one of the techniques I like to recommend to people to use as metadata. when you go from a thousand documents to a million documents, if you're not using something like metadata, so when you have a search, you can narrow down the scope, it's going to be very tough to be able to find and get your high accuracy like that. So yes, retrieval will go down as your data source goes up, but you can use strategies to help fight that back.

## Agentic RAG: The Next Frontier

![Slide 46: Traditional vs Agentic RAG](images/slide_46.png)
*Contrasting static retrieval with dynamic, exploratory agentic search.*

[00:29:20](https://youtu.be/AS_HlJbJjH8?t=1760s) All right, so now let's move into the exciting part. We've talked about traditional rag kind of oneshot approaches to be able to search. There's also now agentic rag where we use multiple ways multiple kind of calls to be able to do this. This all stemmed in just basically the last year really came to a head because now we have LM reasoning models that are capable of effectively using tools where they can use a tool to make a query look at the results that come back and go oh you know what maybe we should do it a different way like that. So that's been the radical change which to me has really brought this about.

![Slide 47: Agentic Reasoning Code](images/slide_47.png)
*Code example of a model continually querying until a task is satisfied.*

[00:30:04](https://youtu.be/AS_HlJbJjH8?t=1804s) So I have a code snippet here. Agno for example is an open source library. They have examples of kind of reasoning agents like that. Um the basic kind of approach here is your query comes in, you're going to generate an answer and then you ask your LM did it answer the question or not? If not, it can rewrite the query, word it a little bit different, try to find that missing information, feed that back into the loop as well.

![Slide 48: Agentic RAG Flowchart](images/slide_48.png)
*Iterative steps: Retrieve -> Grade -> Rewrite -> Repeat.*

[00:30:32](https://youtu.be/AS_HlJbJjH8?t=1832s) And what ends up looking like something like this where it your model's thinking through the steps of what it needs to be able to do for each of those steps it will be like oh this is the query I need to make this is what this is the search information I need to based on those results it'll come back and that gives you to a nice response that takes a little bit longer but now is much more kind of searched across to be able to do this

![Slide 49: Detailed Agent Reasoning Example](images/slide_49.png)
*An agent performing complex tool-use to answer a question about published changes.*

[00:31:02](https://youtu.be/AS_HlJbJjH8?t=1862s) one of The big early categories of this was deep research. So the folks over at Langchain have an open source repo with their open deep research approach which again takes a similar approach.

![Slide 50: Open Deep Research Pipeline](images/slide_50.png)
*A multi-agent framework for scope clarification, research, and reporting.*

[00:31:13](https://youtu.be/AS_HlJbJjH8?t=1873s) I mean they do some things like use a bunch of research sub agents to go out there and be able to kind of do get that do those retrievalss and then bring it all back together to write a report. You can check it out. They have they've made all the prompts all that stuff available. So it's good to see out.

![Slide 51: DeepResearch Bench Leaderboard](images/slide_51.png)
*Performance on 100 PhD-level research tasks.*

[00:31:30](https://youtu.be/AS_HlJbJjH8?t=1890s) There's a whole school around this like actually doing this deep research where there's deep research bench which is a leaderboard in this space. Um it can get very expensive if you start running a lot of a lot of tasks on it. It's got a 100 PhD level research tasks. So it can cost a little bit of money for each of the queries to run. But if you're interested in this kind of deep research area and I already see companies out there um making out making solutions for this.

![Slide 52: Westlaw AI Deep Research UI](images/slide_52.png)
*Commercial application: Westlaw AI generating cited legal research.*

[00:31:58](https://youtu.be/AS_HlJbJjH8?t=1918s) I think the interesting thing on this one here is you pick the time that you want to think and that's often as we'll talk about here a crucial element when it comes to using this agentic search approaches.

### Benchmarking Agentic Search

![Slide 56: BRIGHT Benchmark (Reasoning-based Retrieval)](images/slide_56.png)
*Analyzing queries across keyword, semantic, and reasoning levels.*

[00:32:11](https://youtu.be/AS_HlJbJjH8?t=1931s) A widely used benchmark that I find interesting in this area is called bright and it's a benchmark that's built around retrieval reasoning. So you can see at the top here there's two examples of keyword and semantic. This isn't a benchmark that does that. There's other ones that does that. Instead, look at the examples that it's giving you. These are the types of questions that it wants to do where you have to do a little bit deeper kind of thinking through things to be able to solve the problems like this. So, it's an excellent benchmark out there.

![Slide 57: DIVER Framework](images/slide_57.png)
*DIVER: Chunking, expansion, and multi-stage reranking for reasoning tasks.*

[00:32:46](https://youtu.be/AS_HlJbJjH8?t=1966s) If we look and see what is the number one approach right now on this, its name is diver. And if you take a look at the diver diagram, it probably doesn't look that crazy to you if you're used to rag like right you see, oh wait a minute, right? There's a there's a chunking mechanism here. There's a retrieving mechanism here. Oh, there's a re-ranking mechanism here. And in fact, the number one I also looked at the number two approaches both use those same type of methodologies that we talked about for a baseline in this. Now, they've tweaked this, of course, around kind of the the reasoning pieces, but again, the elements that we've talked about of going out, finding information, chunking, finding information, re-ranking, but then just putting this into a loop is what's going on here.

![Slide 58: DIVER Prompts](images/slide_58.png)
*Specific LLM prompts used for query expansion in DIVER.*

[00:33:31](https://youtu.be/AS_HlJbJjH8?t=2011s) Um, and you can see here some of the examples of queries where, right, in the first round they have, hey, given a query, go look for this stuff. And now, right, based on what we've learned, now what do you think would be possibly helpful to do like that? And so this is hopefully gives you the schematic of how we can think about kind of a gentic rag where we're going to ask, hey, can we find a better answer?

![Slide 53: Self RAG Process](images/slide_53.png)
*Self RAG grades relevance and checks for hallucinations before answering.*

[00:33:54](https://youtu.be/AS_HlJbJjH8?t=2034s) And look, there's been people doing this. This isn't brand new. There's things like self-rag where people have asked and had the models kind of reflect on the answers like that.

![Slide 54: Self-Reflection RAG (Reddit)](images/slide_54.png)
*Community discussion on self-evaluating retrieved documents.*

[00:34:04](https://youtu.be/AS_HlJbJjH8?t=2044s) I saw this on Reddit where somebody kind of shared out um hey how they built this system to do that.

![Slide 55: Inefficiency of Agentic RAG](images/slide_55.png)
*The downside: full pipeline restarts can be slow.*

[00:34:11](https://youtu.be/AS_HlJbJjH8?t=2051s) But one of the things you quickly find out is that these systems can be super inefficient. Right? They're asking the models to go back and retrieve rer and maybe it could have been done just a lot quicker. So this is right there's always a rub. This is the rub with these approaches is that long latency and the long agentic time.

### Latency vs Accuracy

![Slide 59: One Shot vs Agentic RAG on WixQA](images/slide_59.png)
*Comparing factuality and latency: Agentic RAG wins on accuracy but loses on speed.*

[00:34:34](https://youtu.be/AS_HlJbJjH8?t=2074s) And in fact, this is uh kind of I ran this myself, right? I work at Contextual. We have kind of a RAD platform, lots of little settings. So I could kind of tweak it and play around with this. And I took Wix QA, which is publicly available. It's on HuggingFace. It's a technical support um technical support database uh technical support knowledge base. So that's the kind of question it has like a help desk questions and you can see when I had my kind of the one one one shot rag and I think this is like E5 with maybe a reanker I can't remember I could get answers really quick right 5 seconds or so it boom it pulls it back but in terms of factuality which is the benchmark they use on Wix QA like it's 76 like yeah it's pretty good but but it's missing a lot well then I wired in diagentic rag system where all I did was just asked it to reflect you know maybe do more retrieval calls if the answer wasn't complete and it would do more retrieval calls and you can see here it took a little bit longer in terms of thinking the numbers here don't fixate on the exact numbers there's a lot of wiggle room I just want to give you a sense of like a gentic rag takes a little bit longer to do that but on the other hand take a look at that accuracy that's crazy that's a look at that improvement there that has a ton of implications for that.

[00:35:58](https://youtu.be/AS_HlJbJjH8?t=2158s) I mean, one thing right away for me when I ran this is look now now anything that I'm missing that I'm not getting in this 007. I kind of wonder like even my smart system that took a while couldn't figure it out. Like what is going on with the last little bit here? But beyond that, look at the difference between the 0.93 and 76. So these were answers that I was able to figure out if I did multiple calls. On the other hand, right, these are all the the bottom ones here were all the ones I did the first time. So, there's a gap here of answers that took a couple of calls to do. Well, why don't I take a look at those? Why don't I take a look at those types of queries, that type of material, and figure out why do they take multiple queries? Is there something about the way my documents are stored? Is there a way of how I've chunked the documents retrieval that I can modify so I could actually improve this oneshot rag and bring it up closer? Right? You can think of this now as like this is our new kind of baseline for what's possible. Right? This shows what's possible in the system. I can now up that up. So this really is is mind-blowing for me in a couple of different ways.

![Slide 60: BM25 vs SBERT with LLM Querying](images/slide_60.png)
*Surprise finding: BM25 can outperform embedding models when used in an agentic loop.*

[00:37:10](https://youtu.be/AS_HlJbJjH8?t=2230s) Now it's I'm not going to stop you there. So one of the things in the bright paper is they had this graph and I want to walk you through it. So over here they have Quen. So this is the Quen embedding models. So they're using the Quen embedding models with GPT4. So doing that same kind of retrieval loop that we've talked about to be able to find kind of answers. And you can see here's the quality. The higher the bar you get the better answer. So you can see right the Quinn model does okay. Right? It's much better than this espert model bottle over here or right the instant model does. But it gives you a sense of like the quality of what we're getting. But wait a minute, what's this other crazy model over here? This BM25. Take a look. It does better than the Quen. This is crazy, right? Like our good old keyword baseline.

[00:38:02](https://youtu.be/AS_HlJbJjH8?t=2282s) There's just the language model because it can rewrite the queries, right? like it doesn't need an embedding model to figure out the semantic variation because it can just rewrite that into different semantic ones and re-query re-query like that and it actually does better than the quen embedding model like I saw this in the graph and immediately I was like research team like like this is this is something we need to dive into

![Slide 61: Factual Equivalence in Agentic RAG](images/slide_61.png)
*Agentic RAG with BM25 maintains high factual accuracy across datasets.*

[00:38:26](https://youtu.be/AS_HlJbJjH8?t=2306s) and I even ran my own benchmarks like this on a couple of the data sets we have the Wix QA and then I we have an internal financial data set of 10ks and you know what like When I ran this with just BM25, it still did a lot better than one shot and it still got pretty close to kind of the Aentic rag. And this is all just out of the box. I've not tuned or tried to make this improve this thing in any way. This is just the raw performance. But this blows me away, right? Like now this tells me I don't need to use that neural network model, the the semantic model, all that stuff, those embeddings, vector databases. is I could throw all that away. I could just stick this in a textonly database and use BM25 and get a do a pretty good job of being able to find the right answers consistently, right? These are in across different domains. So for me, this is a real gamecher.

[00:39:20](https://youtu.be/AS_HlJbJjH8?t=2360s) Now there is the downside, right? There's that latency cost, right? Like you're lots of times you're going to need one shot. People are going to need an answer in three or five seconds or they're going to leave your website or they're going to be unhappy. There's plenty of room, many use cases for singleshot rag. It's not going away in any way like that. But, you know, if the accuracy matters, if people can wait, this aentic rag is really going to change things.

![Slide 62: Agentic RAG for Code Search](images/slide_62.png)
*Claude Code uses lexical/iterative search instead of vectors for code.*

[00:39:46](https://youtu.be/AS_HlJbJjH8?t=2386s) And you already see it being used in terms of like things like clawed code for example uses a lexical approach, an iterative approach for its um for its approach. And part of that is it's doing code search, which is a little bit different. code doesn't have the same kind of semantic properties that conventional documents do. So, it's always been a little weird for using it for search, but still it's another sign that, you know, hey, maybe we can use these agentic approaches um to be able to do stuff.

## Practical Implementation & Conclusion

![Slide 63: Response Guardrail System](images/slide_63.png)
*A two-tier guardrail system: simple embedding checks first, LLM second.*

[00:40:15](https://youtu.be/AS_HlJbJjH8?t=2415s) Now, as we're doing this, I like to keep you all practically minded. This is where we talk about tradeoffs, but you know what? These things can work together, too. So, I saw this um paper by Door Dash where they talked about their guardrail system. And what I liked is it showed a two-tier system where it showed two different methods working together. It uses a very simple text similarity as an initial guardrail. If that guardrail works great, that's great. If not, they can always kick it over to an LLM, but they use the LM as a backup, right? It's not the primary. It's it's more of like a difficult cases. And I like this type of thinking because it better takes advantage of the relevant kind of advances ad trade-offs of these different types of approaches.

![Slide 64: Hands-on Agentic RAG Resource](images/slide_64.png)
*Comparing `smolagents` vs vanilla RAG.*

[00:41:05](https://youtu.be/AS_HlJbJjH8?t=2465s) Um there's an here's an example if you want to play around with agents. There's lots of agent um ones out there, but just wanted to give people um a little sense of that.

![Slide 65: Solutions for RAG Challenges](images/slide_65.png)
*Matching solutions to problems: Rerankers for accuracy, BM25 for speed, Agents for complexity.*

[00:41:18](https://youtu.be/AS_HlJbJjH8?t=2478s) All right. Thank you all. I going through this. Hopefully, I've given you some sense of like thinking about these trade-offs, you know, right based on kind of these trade-offs. Maybe if you have like a high cost of mistakes or really, right, you don't want to make mistakes. You have the budget for it, maybe a reranker could make sense. On the other hand, right, maybe maybe you're like, "Hey, Raj, you know, I need sub 5 seconds, sub 1 second latency." So, maybe you're like, "Hey, I'm going to try out that BM25 or static embeddings." Maybe your users are doing complex multihop queries. So, a gentic rag is a better better fit like that.

![Slide 66: Retriever Selection Checklist](images/slide_66.png)
*A decision checklist for choosing between Keyword, Semantic, and Agentic retrieval.*

[00:41:52](https://youtu.be/AS_HlJbJjH8?t=2512s) Um, but hopefully I've gone through given you a little bit of a cert checklist here for kind of good starting points for kind of building out your rag systems like that. I'm going to end it here. When I do this in person, I ask a lot of questions. We walk through other parts of the rag platform as well. But thank you all.

### Additional Slides: RAG System & Generation

*The following slides were included in the presentation deck but were not covered in detail during the video recording due to time constraints. They offer a complete view of the RAG system and generation phase.*

![Slide 67: Full RAG System with Reranker](images/slide_67.png)
*The complete system view, now integrating the "Instruction Following Reranker."*

![Slide 68: The Generation Phase](images/slide_68.png)
*Moving from retrieval to generation: producing coherent answers.*

![Slide 69: Generation Model Considerations](images/slide_69.png)
*Selecting the right LLM: Cost, latency, hallucinations, and context window.*

![Slide 70: Contextual Chunking](images/slide_70.png)
*Adding context to chunks to improve retrieval accuracy.*

![Slide 71: Conclusion](images/slide_71.png)
*Final slide with speaker contact information.*