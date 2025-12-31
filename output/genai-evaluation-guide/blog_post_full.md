Here is a comprehensive, annotated blog post based on the technical talk by Rajiv Shah, PhD. It includes the complete transcript, annotated with all 106 slides at the appropriate moments.

***

# Best Practices for Evaluating Large Language Models

**Speaker:** Rajiv Shah, PhD
**Video Source:** [Watch the full talk here](https://youtu.be/qPHsWTZP58U)

This post contains the complete transcript of the workshop, annotated with the accompanying slides to provide a visual guide to the concepts discussed.

---

### Introduction: The Need for Evaluation

![Slide 1: Title slide for a workshop on best practices for evaluating Large Language Models (LLMs) by Rajiv Shah, PhD.](images/slide_1.png)

[[00:00:00](https://youtu.be/qPHsWTZP58U?t=0s)] evaluation for your generative AI applications. This was a recent talk I did for ODSC. Wanted to make a version for the rest of you.

![Slide 2: The presentation introduces the topic of evaluating Generative AI and provides a GitHub repository link for further resources.](images/slide_2.png)

[[00:00:09](https://youtu.be/qPHsWTZP58U?t=9s)] Now, three big things I want you to take away. One is Genai is a little bit different in terms of the technical nuances that's important to know if you're building applications. Second, I wanted to give everybody a basic intro workflow for how you can build an evaluation data set, how you can do evaluation with generative AI. And finally, I'm hoping I can inspire all of you to go out and actually start doing evaluation because in the world that's how you actually learn this stuff is by doing, not reading papers or watching videos like that.

![Slide 3: The workshop begins by illustrating a customer support use case where Gen AI can help agents compose emails more efficiently.](images/slide_3.png)

[[00:00:41](https://youtu.be/qPHsWTZP58U?t=41s)] Now, in the beginning, I always like to kind of motivate these talks with a funny anecdote. And the idea here is one of the biggest use cases for Genai is helping to write those customer support um tickets, emails out there.

![Slide 4: It highlights the common misconception that generating useful Gen AI outputs is simple and can be achieved with basic "vibe coding" of prompts.](images/slide_4.png)

[[00:00:57](https://youtu.be/qPHsWTZP58U?t=57s)] Anybody can go grab a little bit of a prompt, do a little vibe coding, have have a model write out a Genai uh output so you can get a customized response like this.

![Slide 5: An example of a well-crafted, personalized support email acknowledging a delayed shipment is shown.](images/slide_5.png)

[[00:01:12](https://youtu.be/qPHsWTZP58U?t=72s)] This stuff works really good out of the box. And you're probably thinking, "Hey, I'm done." If you're building that quick demo app, you're good. But if you're in this game long enough, you'll see that wait a minute, those things don't always work, right?

![Slide 6: Another example demonstrates an effective support email for a damaged product, indicating successful AI application.](images/slide_6.png)

![Slide 7: A problematic LLM response is presented, where the AI completely misunderstands an "Order Delay Inquiry" and offers product promotions instead.](images/slide_7.png)

[[00:01:26](https://youtu.be/qPHsWTZP58U?t=86s)] like I asked about a order delay, but my email tells me about a new product line, right? It doesn't match at all.

![Slide 8: A positive LLM response is shown, where the AI appropriately apologizes and dispatches a replacement for a defective product.](images/slide_8.png)

[[00:01:34](https://youtu.be/qPHsWTZP58U?t=94s)] Or I somebody asks about a specific order and we tell them that that they're they're sorry that their espresso machine arrived effective. Well, wait a minute. We don't actually sell espresso machines. There was an hallucination here that happened.

![Slide 9: The slide outlines the significant "Risk of Mistakes" associated with Gen AI, categorizing them as reputational, legal, and financial.](images/slide_9.png)

[[00:01:48](https://youtu.be/qPHsWTZP58U?t=108s)] And this is not isolated incidents. Cursor, the folks that build you that wonderful IDE, well, they were using a customer support bot. And guess what? It created a policy that said you're only allowed one device per subscription. And the reality is that wasn't right at all. You could use multiple ones. And this led people to like mistake cursors policy and actually cancel their subscriptions like that. Besides that, Genai has always been problematic around the inputs and outputs and whether they're copyright issues. We also know if you're using these Genai bots and having them out there that courts might be held that it's no different than an employee. If your Genai bot does something or creates a promise, well, you got to back that just like if your customer, your employee did that. So, there is a huge set of mistakes that you have to be worried about which is should cause you pause as somebody that's going in and building these systems.

![Slide 10: An image depicts an individual in distress, visually representing the negative consequences and anxieties related to AI failures.](images/slide_10.png)

![Slide 11: A Fortune article headline reveals that "95% of generative AI pilots at companies are failing," underscoring the challenges in Gen AI adoption.](images/slide_11.png)

[[00:02:46](https://youtu.be/qPHsWTZP58U?t=166s)] Now, what's happened and what's different in 2025 is it's not just you that's thinking about this. It's the executives because they've seen the numbers. They've seen how many Gen AI projects that they've invested into that haven't had huge returns. The 95% is way overstated, but still Gen AI can be useful, can have some good results, but it's not always a sure thing that it's going to be massive like that.

![Slide 12: The presentation asserts that effective "Evaluation helps improve your Gen AI Applications" and links to a relevant video workshop.](images/slide_12.png)

[[00:03:14](https://youtu.be/qPHsWTZP58U?t=194s)] So where evaluation comes in is it helps you build better Genai applications. I've been in the space for a long time. About two years ago I did this video been widely seen around doing evaluation. It's still a good video. A lot of good points here. But this is a little bit more condensed version of that video with a little fresher content for all of you all like that.

![Slide 13: Evaluation is crucial for Gen AI applications to prevent errors, ensure human staff buy-in, and meet regulatory requirements.](images/slide_13.png)

[[00:03:37](https://youtu.be/qPHsWTZP58U?t=217s)] And I always like to start with why evaluation is important. It's important if you're for yourself to build a better application to understand what's working and what isn't. But then you need to also convince your team, your managers. So you need to be able to show them like, hey, I ran this data set on things that hadn't seen before and look, it's holding up okay, as well as maybe you need to go convince regulators or a third-party um model evaluation team. Well, you're going to have to have eval data sets. You're going to have methodologies that you need to be able to show them that your app is going to do what you want it to and you have confidence and trust that it's going to perform in this and evaluation covers a lot of stuff.

![Slide 14: Evaluation for production applications should consider Technical (F1), Business ($$), and Operational (TCO) metrics.](images/slide_14.png)

[[00:04:21](https://youtu.be/qPHsWTZP58U?t=261s)] I know as data scientists we end up often talking about this technical piece. One thing I like to stress is you also have to think about the value of your applications. What's the ROI that's going to do it? At the same time, keep in mind the operational costs as well. What is the cost of ownership? This is one of the issues with, for example, GPUs and enterprises where it costs a lot to have a locally hosted open-source model that you're running 24/7 inside an enterprise, which is often why people go to APIs. But these types of considerations of what is it going to cost to actually run your solution on a day-to-day is an important thing that you need to think about at the outset of your of your application.

![Slide 15: Public benchmarks offer a preliminary understanding of new LLMs' performance, with links to evaluation harnesses provided.](images/slide_15.png)

[[00:05:05](https://youtu.be/qPHsWTZP58U?t=305s)] Now, I think at this point we're all mature enough and we realize that companies out there promote their LMS with these public benchmarks. We know these public benchmarks, they're great for like giving you a rough performance of the LMS, but you're not going to use them to figure out is this a good fit for your application.

![Slide 16: To effectively evaluate LLMs, custom benchmarks reflecting specific use cases, combining a task, dataset, and evaluation metric, are essential.](images/slide_16.png)

[[00:05:19](https://youtu.be/qPHsWTZP58U?t=319s)] Instead, you want to build benchmarks, data sets that reflect your case like that.

![Slide 17: This slide serves as a motivational transition, inviting the audience to learn how to manage and "tame Gen AI."](images/slide_17.png)

[[00:05:28](https://youtu.be/qPHsWTZP58U?t=328s)] So, let's jump in. Let me help you kind of tame generative AI.

![Slide 18: The roadmap outlines a progression from understanding Gen AI basics to building evaluation workflows, adding complexity, and considering agents' impact.](images/slide_18.png)

[[00:05:34](https://youtu.be/qPHsWTZP58U?t=334s)] Now, we're going to start with the basics of how generative AI works. We're going to build an evaluation workflow and then add more complexity. And finally, we'll get to the more agentic stuff. When I gave this talk at ODSC, we ended up with so many questions. That's the advantage of you catch me in person that we didn't get to the later parts. I get to cover the later parts here in the video since none of you can. I'm not going to stop for any of your questions right now.

### Why Evaluating Gen AI Is So Hard

![Slide 19: Two slightly different LLM responses to nearly identical prompts illustrate "Why Evaluating Gen AI Is So Hard" due to output variability.](images/slide_19.png)

[[00:05:58](https://youtu.be/qPHsWTZP58U?t=358s)] So, the reason why Genai is so hard is is if you write a prompt like this, you're going to go through and you're going to get an output. But here's the same thing. If you just wait a minute or two, your system's going to give you a different output. Now, in this case, the outputs are substantively the same, right? They're covering the same types of materials around investigations and help. But you see there are slight differences. And when we get to evaluation, this becomes an important consideration for us.

![Slide 20: The slide explains that even identical prompts can lead to divergent outputs from an LLM.](images/slide_20.png)

[[00:06:30](https://youtu.be/qPHsWTZP58U?t=390s)] And I want to break this up because there's a lot of places where this happens. And we're going to just systematically go through it. We'll talk about inputs, the model, and then output.

![Slide 21: Screenshots of social media posts highlight "Inconsistent Scores Across Benchmarks" for LLMs, indicating evaluation variability.](images/slide_21.png)

[[00:06:41](https://youtu.be/qPHsWTZP58U?t=401s)] So the first thing is is we see some inconsistent scores around benchmarks. And this is a story I told many times. I still like to tell it. I worked at Hugging Face. Tom Wolf, one of the co-founders, loves to talk about new great open source models. Tweet it out. Let everybody know, look how good it is. Look at the performance that we see across all of these benchmarks. Well, in this case, when he tweeted it out, somebody else tweeted back, "Wait a minute. How come the numbers you're tweeting out differ from the ones that are actually in the llama paper?" Now, in both of these cases, you're using the same data set, as we'll talk about MMLU, but why are we showing two different numbers?

![Slide 22: An overview of MMLU (Massive Multitask Language Understanding) is provided, describing it as a benchmark with 57 tasks across various academic domains.](images/slide_22.png)

[[00:07:25](https://youtu.be/qPHsWTZP58U?t=445s)] Now, MMLU is a multiplechoice benchmark. It covers like history, economics, biology, like questions that like high schoolish kind of colleges questions around knowledge in these areas. So, it's often used to measure like how kind of smart a model is um like that.

![Slide 23: The concept of "Prompt Sensitivity" is introduced, showing that minor formatting changes in prompts can lead to a >~5% change in MMLU accuracy.](images/slide_23.png)

[[00:07:42](https://youtu.be/qPHsWTZP58U?t=462s)] But why would two different models get different scores on a multiple choice test? Like it doesn't make any sense if you think about it. [gasps] Well, it turns out if we dig into it that if we look at the three evaluation harnesses that were used, three different approaches, they each wrote their prompts slightly different. If you take a look here, you'll see that there's slight differences in the prompt where one of the the how they phrased it. Some use the word question. Wait, you see the word choices here. All of this ends up affecting the overall accuracy of the how we evaluate the model because it leads to changes in the output.

![Slide 24: Further research on prompt sensitivity details specific formatting alterations that can cause a ~5% accuracy change in MMLU evaluation.](images/slide_24.png)

[[00:08:22](https://youtu.be/qPHsWTZP58U?t=502s)] And look, this isn't crazy stuff like Anthropic wrote about this too, how just changing the options from parenthesis a to parenthesis one or going from round parenthesis to square parenthesis had an effect on the output.

![Slide 25: A bar chart visually demonstrates that simple word changes in prompts can result in a 5–10% drop in LLM performance.](images/slide_25.png)

[[00:08:34](https://youtu.be/qPHsWTZP58U?t=514s)] Now, this hasn't changed recently. If we look at, for example, GPT40, [snorts] still very sensitive to the prompts that are there. We've seen this in a number of recent studies where how you change the just the tone of what you're doing can affect the overall accuracy.

![Slide 26: Beyond prompt content, the "Prompt Tone Also Affects Accuracy," as shown by performance differences in a chatbot arena based on style and sentiment control.](images/slide_26.png)

[[00:08:50](https://youtu.be/qPHsWTZP58U?t=530s)] So, how you ask something can do that, right? Like, I guess this is why mom always had to be polite, right?

![Slide 27: A tweet reinforces that "Prompt Sensitivity Still a Problem," with different prompt phrasing still significantly impacting LLM performance.](images/slide_27.png)

[[00:09:00](https://youtu.be/qPHsWTZP58U?t=540s)] Um, and it's still a huge piece. you still see um posts like this that tell you, hey, use specific phrases, do this because these models still even years later are still kind of sensitive like that. Hopefully, you know, two years from now this won't be an issue, but for now it is.

![Slide 28: The slide questions if the "Falcon LLM - Biased??" by showing a tweet where the model provides positive sentiment about a city but avoids human rights issues.](images/slide_28.png)

[[00:09:16](https://youtu.be/qPHsWTZP58U?t=556s)] So a second story I like to tell and this is about the Falconella model is when it was first released people were trying out different things and part of it is right it came out from the Middle East and some people were concerned like hey wait a minute like could this be biased in some ways and they tried different um different queries and one of them said you know recommend me a technological city and why did it recommend Abu Dhabi like did they train it themselves they can change the input data into this Did they alter the weights or something?

![Slide 29: Another tweet illustrates the "Falcon LLM" avoiding human rights discussions, further highlighting potential bias.](images/slide_29.png)

[[00:09:49](https://youtu.be/qPHsWTZP58U?t=589s)] People were a little confused and there was even concerns like that maybe this is covering up human rights issues because it gives different answers for different cities like that. Well, someone on the team kind of dug into this and like anything when you start digging into this do you jump right into like looking at model weights or no anything? No. You look at what's the inputs into the model? Well, besides your query, a system prompt.

![Slide 30: The slide emphasizes the importance of understanding the "system prompt" as it significantly influences an LLM's responses and potential biases.](images/slide_30.png)

[[00:10:14](https://youtu.be/qPHsWTZP58U?t=614s)] And it turns out that the system prompt here gave the location. It said, "Hey, you're a model that was built in Abu Dhabi." And so that was leading these queries to kind of use Abu Dhabi in a different way than other cities. And it's just a reminder that you need to think about the system prompt whenever you're working with these models.

![Slide 31: Users are prompted to consider if they have read their model's "System Prompt," noting Claude's is a substantial 1700 words.](images/slide_31.png)

[[00:10:33](https://youtu.be/qPHsWTZP58U?t=633s)] [snorts] And I can guarantee you most of you have not. Right? If you go look at the cloud system prompt, it'll take you like eight or nine minutes if you just want to read that straight through. And I'm sure very few people have done that. But those 1700 words in the prompt can have an effect and it could be a different effect depending on the query that you're asking that could affect that response of the model. So as you start using these models more, you need to spend time looking at those system prompts as well.

![Slide 32: The evaluation of a single LLM response is complex due to factors like tokenization, prompt styles, prompt engineering, and system prompts.](images/slide_32.png)

[[00:11:03](https://youtu.be/qPHsWTZP58U?t=663s)] So these are just some of the things just on the input side that can affect it. Now, when we get over to the model side, you got to remember these models are all very different.

![Slide 33: A heatmap illustrates that "LLMs are very different" from each other, showing varying inter-text similarity between model outputs.](images/slide_33.png)

[[00:11:15](https://youtu.be/qPHsWTZP58U?t=675s)] Even if you take two models that are very similar. So, if we take a look here, and I don't think I can show it with my mouse properly. I'll hover it, but we'll see if it shows up. But take a look at two models that are very similar to each other. The Llama 70B and the Llama 3B or 8B model. Very high tech similarity, but they're not perfect. even though they've probably been trained with very similar if not exactly the same data right the AB just had a little bit less of it and so I hope this gets the red light that these models when they give their outputs just the nature of the design of them even if they're the same family is going to lead to different types of outputs and this is always a consideration when you're moving from one model to another you always have to run your eval to make sure that everything holds up I can tell you on our team we've seen sometimes times going from two to 2.5 actually we can see a regression in lots of behaviors where we have to go back and change the prompts that we're using.

![Slide 34: The slide discusses "Sycophantic Models and Bias," demonstrating how AI assistants can generate feedback that aligns with perceived user preferences.](images/slide_34.png)

[[00:12:14](https://youtu.be/qPHsWTZP58U?t=734s)] These models have a lot of their own nuances. Some of these models for example can be very syo sickopantic. I love using that word. Right? They can be overly nice. They can love you too much. We saw this when when OpenAI released GPT41 and then they pulled that back because it was just way over the top like that. This is a consideration is when with your prompts besides that when you're using commercial APIs and you don't have control of that model and the weights well things can change over time they can update those models without telling you and people have been measuring this and seen this type of drift like that and there's lots of reasons for it but um Anthropic recently released a post where they showed that you know some of the things they had some very technical reasons for why things were going wrong like context windows output corruption, but these lasted for days and degraded and changed the outputs of your models.

![Slide 35: The "Reliability of Commercial APIs – Model Drift" is highlighted, showing that LLM performance can change over time, even for the same model version.](images/slide_35.png)

![Slide 36: A timeline from Anthropic illustrates "Degraded Responses" and performance issues in LLMs due to various operational errors over time.](images/slide_36.png)

[[00:13:09](https://youtu.be/qPHsWTZP58U?t=789s)] So things you need to be aware of when you do this. And I'll tell you if you think you're just using open source and you can control it kind of, but the VLM the the inference endpoint that you use, somebody could have updated that and changed that. So even with the weights the same, you have to think about the entire infrastructure stack when you want to make sure things are the same.

![Slide 37: The slide stresses that "Hyperparameters Matter," and understanding settings like temperature and maximum length is crucial for controlling LLM outputs.](images/slide_37.png)

[[00:13:31](https://youtu.be/qPHsWTZP58U?t=811s)] And of course there's always things like hyperparameters that you can go and modify. You can modify right your top P, your temperature. You can set temperature one for the models to be very creative. You can set it all the way down zero because you don't want the model creative. You want it to take the biggest thing out of its probability like that. These are all things that you can control, but they can affect the output.

![Slide 38: Multiple social media posts and articles explain "Non-Deterministic Inference in Practice," where LLMs can produce varied outputs even with identical inputs due to underlying computational factors.](images/slide_38.png)

[[00:13:58](https://youtu.be/qPHsWTZP58U?t=838s)] Now, one recent thing, and if you're not used to GPUs, this is a little bit new, is often the way we implement these these LM models. They're non-deterministic inference in practice. So with a traditional XG boost model, I can set my seed and then my inputs, I should always get the exact same outputs. It's deterministic here. Even if you set the seed, even if you give the same inputs, you can have differences. Then there's a number of different reasons for this and this is why I give lots of people. It it can be the floating point error can accumulate because often it's not just your your floating point. It's combining with others that can cause slight rounding differences can can do that. There's also things with mixture of experts models where you'll have different batches, different activations for that. And so the reality is is it's very prevalent to have non-deterministic inference around this. And you'll look if you look carefully at many of the providers, they'll have a page in there. They're saying, "Hey, you we're not being able to guarantee determinism."

![Slide 39: The challenge of defeating "Non-deterministic inference" in LLMs is acknowledged as a difficult ongoing research area.](images/slide_39.png)

[[00:15:11](https://youtu.be/qPHsWTZP58U?t=911s)] Now, and this is why we always watch these videos. We've had a recent update. The folks over at Thinking Machines spent a little bit of time and figured out, hey, if you correctly batched things, you can try to defeat this non-determinism and have have it deterministic. There was, I believe, a slight latency hit for this approach, but I just saw in the last week or two that it's been introduced in VLM. So, there may be a chance, but you'll have to check with your folks to see if you're able to get deterministic inference um with that. But for the most part, I think you all of you should be aware of the non-determinism problem with GPUs.

![Slide 40: The complexity of evaluating one LLM response is further elaborated by including model selection, hyperparameters, nondeterministic inference, and forced updates as influential factors.](images/slide_40.png)

[[00:15:49](https://youtu.be/qPHsWTZP58U?t=949s)] So, that's that's it. We've covered the model. There's still one more interesting thing. Even if all those are the same, changes in the outputs can change that.

![Slide 41: Challenges in "Generating a Multiple Choice Output" are shown, where LLMs might not adhere to strict formatting requirements, leading to incorrect parsing of answers.](images/slide_41.png)

[[00:16:01](https://youtu.be/qPHsWTZP58U?t=961s)] And here what I like to do is go back to MMOU because there we were trying to get a multiplechoice output. And you're probably like, Raj, multiple choice output, four choices. How tricky could this be? Well, let me tell you, how are you going to tell your model to select a choice? Are you going to tell it select the first letter? when you think about it or are you gonna tell it to look at the entire answer and be able to come up with a determinant there's more than one way to kind of do this or you can limit it to one of the existing choices and in fact we see this with different implementations for the MMLU where we saw that these models were doing different ways right gu just fix it to those four letters and that's it have it generate the text for the and use the first better compare the full answers like that.

![Slide 42: Different evaluation approaches (Original, HELM, AI Harness) for MMLU can yield "different outputs," complicating comparisons.](images/slide_42.png)

[[00:16:56](https://youtu.be/qPHsWTZP58U?t=1016s)] And this has a meaningful effect on the overall performance about which approach you use. And so this again shows you the value of understanding this and recognizing this.

![Slide 43: A table comparing MMLU scores across various LLMs and evaluation methods demonstrates that achieving "Consistency is hard!" in benchmarking.](images/slide_43.png)

[[00:17:07](https://youtu.be/qPHsWTZP58U?t=1027s)] And I shared a spreadsheet which this is a little bit dated but had a bunch of open source LMS where they use the exact same prompt and you can see just a humongous variety in the output of these models like that.

![Slide 44: The slide presents a table showing that "Evaluating Outputs Across Models" for tasks like sentiment analysis can result in different classifications from different LLMs.](images/slide_44.png)

![Slide 45: "Tool Use Adds Another Layer of Variance" to LLM performance, as different models exhibit varying effectiveness across categories like email or terminal tasks.](images/slide_45.png)

[[00:17:23](https://youtu.be/qPHsWTZP58U?t=1043s)] And recently now we don't just look at outputs with reasoning models are making decisions. For example, deciding what tool to use under what conditions. And this is another area where we're going to see a lot of non-determinism where different models at different times you're going to pick different tools. And I've seen it internally in our own things is sometimes it uses the tools, sometimes it doesn't. That can be a little bit tricky when you're building these workflows as we'll talk about um like that.

![Slide 46: This comprehensive slide summarizes "Why LLM Responses Differ," detailing various factors from input tokenization to infrastructure variability.](images/slide_46.png)

[[00:17:49](https://youtu.be/qPHsWTZP58U?t=1069s)] So I tried to shove all this stuff into one slide. I hopefully by walking through it you this is a little bit more palatable and understandable but this is one big takeaway I want all of you to understand if you're not familiar with everything that I talked about. These are all pieces that you should understand how these stacks work because that way you can make sure you're going to get consistent outputs and none of these little things are going to trick up when you're working on your applications like that.

![Slide 47: The slide concludes that the chaotic nature of LLM evaluation is "Okay" and presents a matrix of generative AI evaluation methods based on flexibility and cost.](images/slide_47.png)

[[00:18:17](https://youtu.be/qPHsWTZP58U?t=1097s)] So, I know it feels chaotic. I've showed you a lot of stuff. Haven't made you feel better. And don't worry, we got a lot of tools up our sleeve that we're going to be able to do this. And let's walk through.

### Building an Evaluation Workflow

![Slide 48: This slide marks a transition towards gaining "control" over evaluation, suggesting a starting point for systematic assessment.](images/slide_48.png)

[[00:18:29](https://youtu.be/qPHsWTZP58U?t=1109s)] Now, we're going to spend a big chunk of time. How do we do a simp how do we do how do we evaluate a Genai app?

![Slide 49: The initial step in evaluation involves building a diverse "evaluation dataset" with prompts for various tasks like summarization and extraction.](images/slide_49.png)

[[00:18:37](https://youtu.be/qPHsWTZP58U?t=1117s)] Now, as a starting point, you're going to have some type of prompt. You're asking the model to do something, right? A summarization, extract a city.

![Slide 50: The next step is to obtain "Labeled Outputs," which are the correct, "gold" answers for each prompt in the evaluation dataset.](images/slide_50.png)

[[00:18:46](https://youtu.be/qPHsWTZP58U?t=1126s)] Then what you're going to need to do is get some labeled output. We call it labels. We call it output. Called a reference. Called it gold. A lot of different words for this. But you need this ground truth, another word for it to to help doing that because you use that ground truth to compare to your model output.

![Slide 51: The evaluation process then involves comparing the LLM's "Model Output" against the established "Gold Output" for each prompt.](images/slide_51.png)

[[00:19:05](https://youtu.be/qPHsWTZP58U?t=1145s)] And that tells us are they consistent? Are they lined up? Now, ideally, if you have enough humans, you would just have humans check all of these all the time. But usually humans are too expensive and too tired to work all the time.

![Slide 52: It is crucial to "Measure Equivalence, Not Exact Matches," using an LLM judge to determine if the model's output is semantically similar to the gold standard.](images/slide_52.png)

[[00:19:20](https://youtu.be/qPHsWTZP58U?t=1160s)] So a common technique is we use an LM that reads your prompt that reads the outputs and says are these things the same or not. As we'll talk about this works pretty well. Now I'm not asking for an exact lexical string match. I'm just saying hey do these things say the same? And you can control the prompt for the LM judge with a little bit. So for example, these two in this case we're going to treat as equal. This makes it a lot easier to run your evaluation by leveraging that the strength and the [clears throat] power of kind of an automated judge to do that.

![Slide 53: The "Equivalence" metric serves as the primary optimization goal for LLM evaluation, similar to classic ML evaluation, allowing comparison between configurations.](images/slide_53.png)

[[00:19:57](https://youtu.be/qPHsWTZP58U?t=1197s)] Now, if you use that equivalence that I was talking about as your metric, you can almost just treat it like traditional machine learning where you have a hyperparameter where now all you're trying to do is change the knobs in your in um in your application to maximize that equivalence. And you'll go through and you'll be like, okay, I'll change this prompt. Did my equivalence go up? Oh, I changed this model. Did my equivalence go up? That's how you can then try to help improve your model. That's [laughter] it. That's a very simplified way of how to do all of this. And this is the good part. It's a lot like classic ML evaluation.

![Slide 54: The slide explains "Why Global Metrics Don’t Tell the Whole Story," noting their utility for overall measurement but limitations in generating gold answers or capturing nuanced response aspects.](images/slide_54.png)

[[00:20:33](https://youtu.be/qPHsWTZP58U?t=1233s)] Now, the bad part about this is like you can see like you can't stuff the entire dragon in the box because there's things we're missing here. Okay? There's other aspects of the answer that we're not catching when we just focus on this equivalence thing. The other part is sometimes it's really hard to generate that gold answer. And so I want to kind of touch upon that as well.

![Slide 55: To maximize performance, "From Global to Targeted Evaluation" is necessary, requiring a deep understanding of the data to identify and address specific errors.](images/slide_55.png)

[[00:20:55](https://youtu.be/qPHsWTZP58U?t=1255s)] And so here what we want to do is go into a more targeted evaluation where I've shown you the stuff you can get quickly out of the box. But if we spend more time with the data, spend more time understanding, we can up the accuracy of our models. And what this involves is taking time to build tests.

### Building Tests and Targeting Errors

![Slide 56: This slide acts as a segway to the section on "Building Tests" for LLM evaluation.](images/slide_56.png)

[[00:21:17](https://youtu.be/qPHsWTZP58U?t=1277s)] Now to building tests, what we need to do is dig deeper into the problem set. So here I have an example. Look, it looks good right away, right? It's got a nice answer for that.

![Slide 57: It is recommended to "Start with Examples" by defining clear "Good Example" and "Bad Example" responses to set expectations for LLM behavior.](images/slide_57.png)

[[00:21:32](https://youtu.be/qPHsWTZP58U?t=1292s)] While this response here, we're going to call the bad example. Now, I'm going to ask you, why are we calling this the bad example? What is it about it that's bad? H, and maybe some of you can think about it, but this is the one of the biggest things I want you to learn and take away is to understand what's bad about this.

![Slide 58: The slide encourages cultivating an "Evaluation Mindset" by considering the complexity and nuance of real-world problems that LLMs might address.](images/slide_58.png)

![Slide 59: "Collaborate with Domain Experts and Users" is advised for generating user testing examples and bootstrapping evaluation processes.](images/slide_59.png)

[[00:21:53](https://youtu.be/qPHsWTZP58U?t=1313s)] to understand what's wrong with one of your evaluation sets, you need to go talk to those experts. One of the biggest problems I see and especially I know as data scientists, AI developers, we want to go find an optimal solution. We want to just look for an archive paper. We want to look for an algorithm. We don't want to leave our chair. We just want to find an answer by ourselves. But evaluation is all about solving problems. And we need to go out and talk to others. And having this collaboration with the users, with the domain experts is a must. And this is where if you want to succeed in this field, if you want to build successful applications that people are happy with, you got to go out there, talk to the domain experts, talk to the users, pretend you're a naive user, and kind of bootstrap your up. But this is a big part of doing this. You're not going to just solve this with formulas and listening to videos like me.

![Slide 60: The process of "Identify and Categorize Failure Types" involves reviewing data and classifying common errors to understand LLM shortcomings.](images/slide_60.png)

[[00:22:52](https://youtu.be/qPHsWTZP58U?t=1372s)] Because once you have this knowledge then you can go through all those examples that we showed earlier and you can be like oh yeah these things are related to each other. These this is this is a group a a a cluster a type of behavior we see and the light bulbs start going off and you start to see patterns in your data.

![Slide 61: The slide demonstrates how to "Define What Good Looks Like for Your Use Case" by comparing good and bad examples and then outlining specific evaluation focus areas.](images/slide_61.png)

[[00:23:11](https://youtu.be/qPHsWTZP58U?t=1391s)] And then when I say what's that bad example is you can be like oh yeah well you know what it's too short right the tone it lacks professional you can explicitly kind of start to tell me what's wrong and you need this because once you have that explicit knowledge once you know exactly why then what we can do is start to build tests so what I want you to do is when you have those prompts the models has their responses have your humans evaluate those model responses.

![Slide 62: A table illustrates how to "Document Every Issue and Failure" with LLM responses and corresponding human evaluations of their quality.](images/slide_62.png)

[[00:23:40](https://youtu.be/qPHsWTZP58U?t=1420s)] Have them go through. Now, you're not going to do everything, but even a small subset, have them write down what they think is good about that response and what is bad because you can then use that to start to build tests.

![Slide 63: "Good Evaluation Tooling Can Help" by providing custom viewers for reviewing chatbot conversations and logging user feedback.](images/slide_63.png)

[[00:23:53](https://youtu.be/qPHsWTZP58U?t=1433s)] Now, sometimes you can do this in Excel. You can build custom evaluation tool. Don't go overboard with building custom evaluation tool, but you can make it easier to work with your experts like that.

![Slide 64: The "First Test – Length Check" involves identifying examples with improper length and using a simple function to evaluate if output text length is acceptable.](images/slide_64.png)

[[00:24:05](https://youtu.be/qPHsWTZP58U?t=1445s)] But here, for example, we talked about, oh, it's too long. Well, you know what? We can build a simple test in Python, right? We don't need a fancy model. This is just basic Python that says, hey, you know, is this something over under eight words or under over 200? Let's flag that.

![Slide 65: The "Second Test – Tone and Style" is built by identifying desired tones and using an LLM itself as a judge to evaluate the tone of responses.](images/slide_65.png)

[[00:24:22](https://youtu.be/qPHsWTZP58U?t=1462s)] I could build another test which looks at the tone and style. And here I'm going to use an open AI model. I'm going to use that LM as a judge to see what was the style and tone because these models can effectively do that.

![Slide 66: The slide shows how to "Document Issues and Failures" by adding automated checks for length and tone to the evaluation table.](images/slide_66.png)

[[00:24:38](https://youtu.be/qPHsWTZP58U?t=1478s)] And when I do that now, when I run my when I run my prompts through, I can look at the response that was given and then I could have this automated test which tells me which answers passed the length test, which ones didn't, which ones passed the tone test like that. So now these give are my new automated tests that help me I figure out where my failures are. [snorts]

![Slide 67: It's crucial to "Check LLM Judges Against Humans" by verifying the alignment between LLM-based equivalence scores and human evaluations.](images/slide_67.png)

[[00:25:09](https://youtu.be/qPHsWTZP58U?t=1509s)] Now, as I'm working on this, one step further I can always do is as I'm building tests, we still want to use equivalence, but let's make sure that equivalence is lined up with our human evaluation because the whole idea of that equivalence is we just want to take the burden off our humans to check every one of these. So, it might involve slightly changing the prompt, changing changing that equivalence judge so it aligns, right? aligns with that human. And if they're looking at the world differently, it's not very helpful. You need them to be aligned to do that.

![Slide 68: The slide illustrates "Self-Evaluation Bias in LLMs," showing how models tend to rate their own outputs or those from similar models more favorably.](images/slide_68.png)

[[00:25:54](https://youtu.be/qPHsWTZP58U?t=1554s)] Now when you're doing this, one of the things to be careful about is you're going to use you're using different judges for different pieces here. As we talked about, you're have that equivalence judge that we talked about. You might use other judges. These models, they love themselves. If you give a GPT4 model text, it likes its GPT4 text better than text from other models. So, just be aware if you're using models together that are the same, they're going to like themselves better better. It if to be to get them a little more critical, you want to mix it up. You want to use Cloud for one, GPT4 for another, Gemini for another. So, this is just a little trick. It's not going to make a huge different, but it can make enough of a subtle difference that you want to think about kind of making sure you don't limit yourself to this self-evaluation bias.

![Slide 69: "LLM Judges - Check Alignment" is critical, as human and LLM judges can achieve high agreement on correctness and readability if properly aligned.](images/slide_69.png)

[[00:26:48](https://youtu.be/qPHsWTZP58U?t=1608s)] We talked about the alignment piece. You always want to make sure that the humans that are checking your things, and you should be having humans spot check at the beginning and all the way through that they're lined up with what your LLM judges are doing.

![Slide 70: This slide details various "Biases in LLM Judges," including position, verbosity, compassion, bandwagon, and authority biases, among others.](images/slide_70.png)

[[00:27:02](https://youtu.be/qPHsWTZP58U?t=1622s)] Now, these LM judges, we talked about the self-evaluation bias. They have lots of other biases. So, as if you're somebody getting into this field, you should take a look at these biases. You should slowly learn this because this is going to affect your evaluation results over time. If you don't, for example, know that LM for example favor the early answers over the later answers. So really, you need to scramble up your answers every once in a while or otherwise that bias is going to carry through towards your evaluation like that.

![Slide 71: "Best Practices for LLM Judges" include calibration with human data, using ensembles, avoiding them for relevance, human spot-checks, discrete ratings, and awareness of concept drift.](images/slide_71.png)

### Error Analysis and Refinement

![Slide 72: "Error Analysis Using Test Cases" helps investigate and improve LLM performance by plotting failed cases categorized by different error types for various models.](images/slide_72.png)

[[00:27:32](https://youtu.be/qPHsWTZP58U?t=1652s)] All right, we're making good progress here. So now that you've done this, what we can do is start to collect the results that you have and figure out what are the patterns that we're seeing. And this is error analysis. I can go through and see, oh look, when I did GPT4 or when I did GPT3, how many failures did I get in tone? How many did I get with GPT4? Right? This helps me figure out like, oh, I can compare these two to see what's going on.

![Slide 73: Another example of "Error Analysis Using Test Cases" compares the performance of two different prompts across various failure categories.](images/slide_73.png)

[[00:28:00](https://youtu.be/qPHsWTZP58U?t=1680s)] Right? Or I could compare two different prompts. This is the value of having all these test cases. Now I have a better understanding of where my failures are and how to fix them like that.

![Slide 74: The slide suggests using "Explanations to Guide Improvement" by providing metadata from equivalence checks that detail why an LLM's response was considered accurate or not.](images/slide_74.png)

[[00:28:11](https://youtu.be/qPHsWTZP58U?t=1691s)] One of the other tips you can do is when I use equivalence, I always like to ask for an explanation for equivalence. I just ask it to give me one sentence to explain explain its decision. That helps me a ton. Like these models are really useful if you have them explained. It just kind of helps you focus your thinking about what are the relevant pieces of information for why it made its decision.

![Slide 75: It warns about "Limits to Model Explanations," reminding that LLM explanations might not accurately reflect the model's true reasoning process.](images/slide_75.png)

[[00:28:35](https://youtu.be/qPHsWTZP58U?t=1715s)] Now, the explanations aren't exactly what the model's doing. Like don't don't go too far with that. It's just a huristic to help you understand what's going on and make quicker sense of this.

![Slide 76: The "Evaluation Flywheel" model outlines a continuous process of analyzing failures, improving the system, and measuring outcomes to refine LLM applications.](images/slide_76.png)

[[00:28:43](https://youtu.be/qPHsWTZP58U?t=1723s)] So all of this is really this kind of evaluation flywheel. My buddy Hamill, he's done a course. If you find him on X or Twitter, he's he talks about this stuff all day long. But this is the idea for what you're going to do. You're going to go build that evaluation. You're going to analyze things. But then you're gonna build these tests, see how they are, [clears throat] figure out where your weaknesses are, improve it, build that evaluation, spend some time with the data. Meet this is a flywheel cycle that you're going to continually do to do that. [snorts]

![Slide 77: An example illustrates "Building Even More Tests" for a financial analyst agent, including a complex question and a detailed LLM response.](images/slide_77.png)

[[00:29:17](https://youtu.be/qPHsWTZP58U?t=1757s)] So, let me show you one more example of how we even go crazier with this. Um, suppose you're building a financial analyst agent and you care about the style. And this is a real world use case. This is happens all the time. people are very particular how their their responses should be like that. Now, when you assess the response here, and you can see the response here, it's it's kind of long. It's not like a one-s sentence kind of thing.

![Slide 78: A "Global Test" for the financial analyst use case asks if the LLM's explanation is appropriate for a regulated firm.](images/slide_78.png)

[[00:29:43](https://youtu.be/qPHsWTZP58U?t=1783s)] You could write a global LM test that says, "Hey, was this explained as I would expect for like a financial analyst at a regulated firm?" It's one approach you could do.

![Slide 79: The slide contrasts "Global versus Unit Tests," breaking down the financial analyst agent evaluation into specific unit tests for context, clarity, precision, compliance, actionability, and risks.](images/slide_79.png)

[[00:29:54](https://youtu.be/qPHsWTZP58U?t=1794s)] What I want to introduce you to, we've talked about tests, we can build unit tests. So suppose I think of style as composed of six elements. The context, the clarity, precision, compliance, actionability, and risks. I can build a unit test for each one of those.

![Slide 80: "Scoring Global and Unit Tests" is demonstrated, showing a radar chart for unit test scores alongside a detailed global evaluation summary.](images/slide_80.png)

[[00:30:11](https://youtu.be/qPHsWTZP58U?t=1811s)] And so what this allows me to do is now when I want to check a query, I can go and just look at the results of the unit tests. And that gives me an idea of where where the answer is working well and where it isn't. versus if I just use that global test, like there's a lot of stuff for me to read through to figure out exactly like where the model is.

![Slide 81: "Analyzing Failures with Clustered Patterns" involves using K-means to group LLM responses into categories like synthesis, context, hallucination, and incomplete retrieval failures.](images/slide_81.png)

[[00:30:33](https://youtu.be/qPHsWTZP58U?t=1833s)] And the great thing with the unit test is you can even combine them, cluster them together, and find patterns in them. And I have a whole notebook and a whole worksheet kind of showing you how to do this. But hopefully the light bulbs are going off here. As you look for errors, you can group them, look for larger clusters of errors along the ways like that.

![Slide 82: Guidelines for "How to Design Good Unit Tests" include keeping them focused, avoiding compound criteria, using unambiguous language, assessing desirable qualities, and employing binary or small-range scales.](images/slide_82.png)

[[00:30:52](https://youtu.be/qPHsWTZP58U?t=1852s)] All right, a little bit on unit tests, but what I want to do is keep moving on. Lots of good things you can do with unit tests.

![Slide 83: "Examples of Global to Unit Tests" are provided, categorized into Legal, Retrieval, and Bias/Fairness aspects.](images/slide_83.png)

![Slide 84: Unit tests are shown to be effective "to Evaluate New Prompts," especially when built from a strong system prompt, helping to judge new prompt iterations.](images/slide_84.png)

![Slide 85: The slide cautions that "Evaluation Tools – No Silver Bullet" exists, advising users to learn evaluation basics before adopting tools and to implement logging and dataset versioning.](images/slide_85.png)

![Slide 86: Error analysis is conceptualized as understanding both the "Forest: Global / Integration" (overall system) and the "Trees: Test Case / Unit Tests" (specific components).](images/slide_86.png)

[[00:31:04](https://youtu.be/qPHsWTZP58U?t=1864s)] So, all of this so far kind of comes under the bundle of air analysis of of what we want to do.

![Slide 87: A key "Error Analysis Tip" is to "Compare performance one setting at a time" to isolate the impact of individual changes.](images/slide_87.png)

[[00:31:12](https://youtu.be/qPHsWTZP58U?t=1872s)] Now, you guys don't get all my fun jokes. What I want you to do is make sure that when you're thinking about error analysis, you change one thing at a time. If you try to change too many things and it's very very tempting, right? There's like four or five, right? There's so many settings. Change one thing at a time. See how what the effect is as you're going through, as I've shown you before already.

![Slide 88: Additional "Error Analysis Tips" include using an ablation style, categorizing failures, leveraging examples, and monitoring logs and traces.](images/slide_88.png)

[[00:31:36](https://youtu.be/qPHsWTZP58U?t=1896s)] We categorize the failures. We keep track of it. As you find examples that are outliers, edge cases, or really good examples, like heart them, save them, favorite them, find a way to keep track of them because you're going to want to come back in them in a few days. And if you haven't done that, it's a pain in the butt to try to go find it. Finally, use some type of tool that gives you logs, traces, so that way you can go back and do that investigation as well. There's a ton of them, as we'll talk about, on the market.

![Slide 89: "The Evaluation Story We Tell" often portrays a linear progression of accuracy improvement over time for Gen AI applications.](images/slide_89.png)

[[00:32:04](https://youtu.be/qPHsWTZP58U?t=1924s)] Now, as you go through this, if you haven't done this stuff before, you often see people tell a story like this, like, "Hey, we started off, the performance wasn't that great, but then we started tweaking some things. We're able to get to a really good performance where we did it." And this is this nice like linear history of the natural progression of what happens.

![Slide 90: This slide contrasts with "The Reality of Progress," showing a non-linear, iterative optimization flow for LLMs involving various techniques like RAG, prompt engineering, and fine-tuning.](images/slide_90.png)

[[00:32:24](https://youtu.be/qPHsWTZP58U?t=1944s)] Let me tell you, they that's not actually how it happens. The reality is is it's often you do a couple steps forward, you fall back, you do a couple steps forward, you fall back. Like it's not in like that. So as you're working through this, if you get frustrated at times, no, just keep sticking with it. It will get better. And I think that's the difference between people who've done this for a while versus new people is people who've done this for a while know if you keep sticking with the approach that I told you will slowly improve the application and it will get better even though you might not see it at your current state like that

![Slide 91: "Evaluation is a Continual Process," depicted as a cyclical workflow involving data collection, optimization, user acceptance testing, and iterative updates.](images/slide_91.png)

[[00:33:01](https://youtu.be/qPHsWTZP58U?t=1981s)] when you're working with use cases in Gen AI an important consideration is to do user acceptance testing and this is because unlike traditional machine learning where you had a hold out data set that you could use to see if it generalizes. We don't really have that in Gen AI. Your hold out data set is your users. You have to involve them early on because otherwise your application won't work very well. So what I tell people is build that initial evaluation data set, spend some time trying to optimize on it, but then go test it with your users. Has to be that production settings because they're going to give you invaluable feedback that you didn't catch the first time. And then you're using that to update your eval data set, do some more hill climbing, and figure out what you improve. And then the cycle keeps going until you're happy enough where we want to go ahead and move it into production like that.

![Slide 92: The rhetorical question "How do you eat an elephant?" sets up the idea of breaking down a large evaluation task into manageable parts.](images/slide_92.png)

[[00:33:56](https://youtu.be/qPHsWTZP58U?t=2036s)] Relatedly, as we get to these Genai applications, they're big. There's a lot to it. And so, one of my favorite quotes is when we're dealing with like these huge overwhelming tasks is, how do you eat an elephant? Right? You eat it one bite at a time.

![Slide 93: The slide illustrates "Adding Tests Over Time" by metaphorically showing how to evaluate the "GenAI Evaluation Elephant One Bite at a Time," gradually widening the scope of testing.](images/slide_93.png)

[[00:34:10](https://youtu.be/qPHsWTZP58U?t=2050s)] Same thing for Gen AI. Like the first time through, you're just basically seeing does my app work or not? Like not trying to catch every edge case. Over time, you'll continue to add tests as you notice, oh really, we need to focus on this point or oh, this point isn't. And so your initial app might just have a handful of tests, but six months later, if this app is useful, you've kept building on it, you might have 80, 90, 100 tests for that same application as well. So that's the normal flow. Don't try to do too much all at once like that.

![Slide 94: "Doing Evaluation the Right Way" involves starting with annotated examples, systematically documenting issues, continuous error analysis, collaborating with experts, and considering generalization.](images/slide_94.png)

[[00:34:45](https://youtu.be/qPHsWTZP58U?t=2085s)] All right, we're making good progress here. Hopefully I've been going not too fast for you.

### Agentic Use Cases

![Slide 95: This slide transitions to the topic of "Agentic use cases" for LLMs.](images/slide_95.png)

[[00:34:50](https://youtu.be/qPHsWTZP58U?t=2090s)] Last thing I want to touch a gentic, right? It's the way the world is going. We know um we see so many of this and the the trouble with this is the the idea of the agentic is now the model's making decisions. it's making it's using its reasoning its tool calls to decide you know should I fly should I swim you know what other approach should I take in doing this and this giving the model this agency makes it much harder for us to track what's going on

![Slide 96: A simple decision point, "How should it cross the river?", is presented for an agent, hinting at the need to evaluate agent choices.](images/slide_96.png)

![Slide 97: A complex flowchart titled "Under the Hood: Chat-to-purchase Router" illustrates an agentic workflow involving LLM calls, internal APIs, and application code.](images/slide_97.png)

[[00:35:22](https://youtu.be/qPHsWTZP58U?t=2122s)] so here was a simple example I saw for kind of imagine a model that's going to look at the the input and then based on that input it's going to make a decision for what the customer wants do they need to search for a product do they need customer port? Do they want to track a package? Now once it decides which of these things the customer wants to do, this is that router function. The second step is to actually execute and do that complete workflow. So I want you to break down these tasks when you have it like this. Like what is that initial decision that's going on around which of these workflows we're going to follow and then we can look at the efficacy of each of those workflows and how well the model does upon that. This is the kind of breaking down that you have to do when you work with this stuff. You have to find ways to bite that elephant and make it easier.

![Slide 98: A workflow diagram for a "Text to SQL Agent from Snowflake" details how a user question is processed through multiple stages and agents to generate a SQL query.](images/slide_98.png)

[[00:36:17](https://youtu.be/qPHsWTZP58U?t=2177s)] Similarly like Snowflake has this text to SQL agent seems really fancy but again you can kind of break this down into pieces where for example they have an initial piece that says hey should this is this a good question for us to take as a SQL agent and so they have this quick classification at the front end. We can build a test we can build and evaluate just this portion of it before we go in and look at the rest of the text to SQL like this.

![Slide 99: "Evaluating Office-Style Agent Workflows (OdysseyBench)" demonstrates typical failure cases when LLM agents attempt complex multi-step office tasks.](images/slide_99.png)

[[00:36:44](https://youtu.be/qPHsWTZP58U?t=2204s)] And one of the things you'll see is as you go into more of these agentic things is all of these LLM agents are doing different kinds of tasks here. They're finding files, finding actions, failing find failing to use tools.

![Slide 100: "Error Analysis for Agentic Workflows" focuses on assessing overall performance, routing decisions, and individual agent steps to identify and fix issues.](images/slide_100.png)

[[00:36:57](https://youtu.be/qPHsWTZP58U?t=2217s)] We can build and test and evaluate each one of these. And it's the same process we talked about where you're going to assess how well it's doing the routing, assess the individual age steps, see where it's working, where it isn't, categorize all of that. It's just a lot more but it's the same kind of basic action error analysis action

![Slide 101: The slide emphasizes "Evaluating a Workflow Instead of a Response" by showing a detailed flowchart of a conversational refund process, illustrating the complexity of agentic behavior.](images/slide_101.png)

[[00:37:19](https://youtu.be/qPHsWTZP58U?t=2239s)] and let me tell you I know it gets complicated right like this is a huge workflow which has lots of steps to do this and I think we're still figuring out our way for h what's the best approach as you build these more complicated workflows where you're you're not going to go in from the start and be able to evaluate every step of the process where maybe you look end to end for some maybe for some of them you actually break it down into micros and I think we're all just learning and trying to figure out how we do all of that.

![Slide 102: The warning that "Agentic Frameworks Help – Until They Don’t" highlights their benefits and limitations, particularly when they break, become outdated, or require customization.](images/slide_102.png)

[[00:37:46](https://youtu.be/qPHsWTZP58U?t=2266s)] As you're doing this, one caution I have for people is there's a lot of agentic frameworks out there. They're great for demos, great to kind of get you started, but a lot of times they can abstract away the technical details, which is nice again for a demo, but then if it breaks, if it fails on you, then it's like uh like you have to end up going in looking at the code and trying to do it. So yes, you know, you can use them for demos, but I tell a lot of people for many times as you move these to productions, it's best to not really rely on those agentic frameworks unless you have to um to do that because it's a dependency that the world is changing so fast. I haven't seen any of them stay up in a reliable way versus just going with straight Python.

![Slide 103: The slide presents conceptual "Abstraction for Agentic Workflows," showing trade-offs between cost efficiency and intelligence, and the iterative nature of an agent's internal workflow.](images/slide_103.png)

[[00:38:30](https://youtu.be/qPHsWTZP58U?t=2310s)] >> [snorts]
>> It's a similar thing that we see with with agentic pieces where you can build these workflows of I have certain actions that I want to do. You can orchestrate it yourself where you have control over every step like that. For some applications where you want control, you want to make sure everything works perfectly, it makes sense to do that.

![Slide 104: "When Agent Abstractions Break Down," declarative frameworks become cumbersome for dynamic workflows, suggesting code-first SDKs for adaptive agent orchestration.](images/slide_104.png)

[[00:38:53](https://youtu.be/qPHsWTZP58U?t=2333s)] Now, the model providers are busy training their models to follow these types of workflows. And so they're saying, "Don't don't create these workflows. Don't create these separate steps. Instead, our agents are smart enough. We'll dynamically do it. You can just trust us to do that." And my guess is is for different applications, we'll do different things. But I'm just want you to be aware of sometimes you want to break everything down into specific pieces. Sometimes eh, let's just see if the LM can handle it by itself without anything else um like that.

![Slide 105: "Lessons from Reproducing Agent Benchmarks" include standardizing evaluation, measuring efficiency alongside accuracy, detecting agents gaming tests, and logging real behavior.](images/slide_105.png)

![Slide 106: The final slide, "We did it!", provides the GitHub link and QR code for the presentation's code and slides.](images/slide_106.png)

[[00:39:25](https://youtu.be/qPHsWTZP58U?t=2365s)] All right. Thank you all. I went through this quickly, but hopefully it gives everybody a sense of like where are the issues with Genai that you should be thinking of. Hopefully the confidence to be like, okay, I saw how Raj did this with this application. Let me try to build my own and this is what you should do, my own Genai application where I build a simple evaluation data. I can test whether my model is meeting it or not like that. And just do that to give yourself the experience and the confidence to do this kind of work. All right. Thank you all.