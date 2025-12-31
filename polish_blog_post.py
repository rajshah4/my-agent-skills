#!/usr/bin/env python3
"""
Polish the RAG blog post using Gemini API
"""

from dotenv import load_dotenv
from pathlib import Path
import os
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()

print("✨ Polishing RAG Blog Post with Gemini\n")
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
print(f"   ✅ Slide outline: {len(slide_outline):,} characters")

# Get Gemini config
model_name = os.getenv('GEMINI_MODEL', 'gemini-2.0-flash-exp')
api_key = os.getenv('GEMINI_API_KEY')
temperature = float(os.getenv('TEMPERATURE', '0.7'))

print(f"\n🤖 Using model: {model_name}")
print(f"   Temperature: {temperature}")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Create the prompt
prompt = f"""You are an expert technical writer specializing in AI/ML content.

I have a technical talk about RAG (Retrieval Augmented Generation) that I want to turn into a comprehensive blog post.

VIDEO URL: {video_url}

SLIDE OUTLINE (71 slides):
{slide_outline}

FULL TRANSCRIPT (with timestamps):
{transcript[:30000]}... [transcript continues]

Please create a polished, engaging blog post that:

1. **Structure**:
   - Start with a compelling introduction explaining why RAG is important
   - Use clear section headings based on the slide topics
   - Include relevant quotes from the transcript
   - Add timestamps as links (e.g., [00:15:30]({video_url}&t=930s))
   - Reference specific slides where relevant (e.g., "As shown in slide 13...")

2. **Style**:
   - Write in an engaging, accessible tone
   - Explain technical concepts clearly
   - Use markdown formatting (headers, lists, code blocks, emphasis)
   - Include key insights and takeaways

3. **Content**:
   - Cover the main topics: BM25, Language Models, Agentic Search
   - Highlight the RAG design framework and tradeoffs
   - Explain why 95% of Gen AI projects fail
   - Include practical implementation details
   - Add a conclusion with key takeaways

4. **Format**:
   - Use proper markdown with front matter (title, date, author)
   - Include image placeholders like: `![Slide 5](images/slide_5.png)`
   - Make it ready to publish

Generate the complete blog post now:"""

print("\n🔄 Generating polished blog post...\n")

try:
    # Generate the content
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=8192,
        )
    )

    blog_post = response.text

    # Save the polished blog post
    output_file = output_dir / "blog_post_polished.md"
    with open(output_file, 'w') as f:
        f.write(blog_post)

    print("=" * 60)
    print(f"✅ Blog post polished successfully!")
    print(f"📝 Saved to: {output_file}")
    print(f"\n📊 Stats:")
    print(f"   - Length: {len(blog_post):,} characters")
    print(f"   - Words: ~{len(blog_post.split()):,}")
    print(f"   - Lines: {len(blog_post.splitlines()):,}")

    # Show first 800 characters
    print(f"\n📖 Preview:")
    print("-" * 60)
    print(blog_post[:800])
    print("...")
    print("-" * 60)

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
