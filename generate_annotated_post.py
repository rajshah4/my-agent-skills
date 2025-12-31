#!/usr/bin/env python3
"""
Generate a fully annotated blog post with complete transcript + all slides embedded
This creates a "walk through the talk" experience, not a summary
"""

from dotenv import load_dotenv
from pathlib import Path
import os
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()

print("📝 Generating Fully Annotated Blog Post\n")
print("=" * 60)

# Configuration
output_dir = Path.home() / "Code" / "my-agent-skills" / "output" / "rag-talk"
transcript_file = output_dir / "transcript.txt"
outline_file = output_dir / "slide_outline.md"
video_url = "https://youtu.be/AS_HlJbJjH8"

# Read the content
print("\n📚 Reading source materials...")
with open(transcript_file, 'r') as f:
    transcript = f.read()
with open(outline_file, 'r') as f:
    slide_outline = f.read()

print(f"   ✅ Transcript: {len(transcript):,} characters")
print(f"   ✅ Slide outline: 71 slides")

# Get Gemini config
model_name = os.getenv('GEMINI_MODEL', 'gemini-2.0-flash-exp')
api_key = os.getenv('GEMINI_API_KEY')
temperature = float(os.getenv('TEMPERATURE', '0.7'))

print(f"\n🤖 Using model: {model_name}")
print(f"   Temperature: {temperature}\n")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Create the prompt for annotated transcript
prompt = f"""You are creating a comprehensive, annotated blog post from a technical talk about RAG (Retrieval Augmented Generation).

VIDEO URL: {video_url}

SLIDE SUMMARIES (71 slides):
{slide_outline}

FULL TRANSCRIPT WITH TIMESTAMPS:
{transcript}

YOUR TASK:
Create a blog post that integrates the COMPLETE transcript with ALL 71 slides at the appropriate moments. This should be like "walking through the talk" - readers follow along with every word spoken, with slides appearing exactly when they're discussed.

REQUIREMENTS:

1. **Format**: Start with markdown front matter:
---
title: "From Vectors to Agents: Managing RAG in an Agentic World - Full Talk"
date: 2025-10-27
video: {video_url}
author: Rajiv Shah
type: annotated-transcript
---

2. **Introduction**: Brief intro (2-3 paragraphs) setting context

3. **Main Content - Annotated Transcript**:
   - Include the COMPLETE transcript, organized into logical sections
   - Embed slide images at the exact moment they're discussed
   - Format: `![Slide X: Brief description](images/slide_X.png)`
   - Add section headers to break up the content
   - Keep ALL the original spoken words - don't summarize
   - Add timestamp links: `[MM:SS](video_url&t=XXs)`

4. **Slide Placement**:
   - Use the slide summaries to determine WHEN each slide appears
   - Match slide topics to transcript content
   - Embed ALL 71 slides in order
   - Add a brief caption under each slide (1 line)

5. **Structure Example**:
```markdown
## Introduction to RAG

[00:00:00](link) Are you ready for a deep dive into rag, especially around retrieval? What I want to do today is talk to you about what the problems are with rag...

![Slide 1: Title - From Vectors to Agents](images/slide_1.png)
*Rajiv Shah presents an overview of managing RAG in production.*

[00:00:20](link) Now, to start out with, I like to focus on where we are with Rag today...

![Slide 2: ACME GPT Logo](images/slide_2.png)
*A hypothetical RAG system example.*

[continuing with full transcript...]
```

6. **Sections**: Break the content into these major sections based on the talk flow:
   - Introduction & Context
   - The RAG Problem Space
   - RAG as a System
   - Retrieval Approach 1: BM25
   - Retrieval Approach 2: Language Models & Embeddings
   - Retrieval Approach 3: Agentic Search
   - Conclusion & Key Takeaways

7. **Important**:
   - DO NOT summarize - include the full transcript
   - DO NOT skip slides - embed all 71
   - DO maintain chronological order
   - DO add helpful section breaks
   - DO keep the conversational tone from the talk

Generate the complete annotated blog post now. This will be long (expect 40,000+ characters) - that's expected and desired.
"""

print("🔄 Generating fully annotated blog post...")
print("   (This will take a minute - processing full transcript + 71 slides)\n")

try:
    # Generate the content with higher token limit
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=30000,  # Much higher for full transcript
        )
    )

    blog_post = response.text

    # Save the annotated blog post
    output_file = output_dir / "blog_post_annotated_full.md"
    with open(output_file, 'w') as f:
        f.write(blog_post)

    print("=" * 60)
    print(f"✅ Full annotated blog post generated!")
    print(f"📝 Saved to: {output_file}")
    print(f"\n📊 Stats:")
    print(f"   - Length: {len(blog_post):,} characters")
    print(f"   - Words: ~{len(blog_post.split()):,}")
    print(f"   - Lines: {len(blog_post.splitlines()):,}")

    # Count slide references
    slide_count = blog_post.count('![Slide')
    print(f"   - Slides embedded: {slide_count}")

    # Show first 1000 characters
    print(f"\n📖 Preview (first 1000 chars):")
    print("-" * 60)
    print(blog_post[:1000])
    print("...")
    print("-" * 60)

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
