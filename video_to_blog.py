#!/usr/bin/env python3
"""
Complete Video-to-Blog Pipeline
Converts technical talks (video + slides) into blog posts

Usage:
    1. Edit the CONFIG section below
    2. Run: python video_to_blog.py
    3. Get summary + full annotated versions
"""

from dotenv import load_dotenv
from pathlib import Path
import os
from google import genai
from google.genai import types
from hamel.writing import pdf2imgs, outline_slides
from hamel.yt import transcribe, yt_chapters

# Load environment
load_dotenv()

# ============================================
# CONFIGURATION - Edit these for each new talk
# ============================================

CONFIG = {
    # Talk details
    "video_url": "https://youtu.be/AS_HlJbJjH8",
    "slides_pdf": Path.home() / "Downloads" / "RAG_Oct2025.pdf",
    "talk_name": "rag-talk",  # Used for output directory

    # Quarto metadata (for final blog post)
    "title": "From Vectors to Agents: Managing RAG in an Agentic World",
    "date": "2025-01-15",
    "categories": ["RAG", "AI", "Retrieval", "Agentic"],
    "author": "Rajiv Shah",

    # Optional: Custom output location
    "output_base": Path.home() / "Code" / "my-agent-skills" / "output",
}

# ============================================
# PIPELINE - No need to edit below
# ============================================

def main():
    print("🎬 Video-to-Blog Pipeline\n")
    print("=" * 60)

    # Setup paths
    output_dir = CONFIG["output_base"] / CONFIG["talk_name"]
    image_dir = output_dir / "images"
    output_dir.mkdir(parents=True, exist_ok=True)
    image_dir.mkdir(exist_ok=True)

    video_url = CONFIG["video_url"]
    slides_pdf = CONFIG["slides_pdf"]

    print(f"\n📹 Video: {video_url}")
    print(f"📄 Slides: {slides_pdf}")
    print(f"📁 Output: {output_dir}\n")

    # Get Gemini config
    model_name = os.getenv('GEMINI_MODEL', 'gemini-2.0-flash-exp')
    api_key = os.getenv('GEMINI_API_KEY')
    temperature = float(os.getenv('TEMPERATURE', '0.7'))

    print(f"🤖 Using Gemini: {model_name}")
    print(f"   Temperature: {temperature}\n")

    # Initialize Gemini
    client = genai.Client(api_key=api_key)

    # ========================================
    # STEP 1: Extract Raw Materials
    # ========================================
    print("=" * 60)
    print("STEP 1: Extracting Raw Materials")
    print("=" * 60 + "\n")

    # Convert PDF to images
    print("🔄 Converting PDF slides to images...")
    try:
        pdf2imgs(str(slides_pdf), str(image_dir))
        num_images = len(list(image_dir.glob("*.png")))
        print(f"   ✅ Created {num_images} slide images\n")
    except Exception as e:
        print(f"   ❌ Error: {e}\n")
        return

    # Get transcript
    print("🔄 Fetching video transcript...")
    try:
        transcript = transcribe(video_url)
        transcript_file = output_dir / "transcript.txt"
        with open(transcript_file, 'w') as f:
            f.write(transcript)
        print(f"   ✅ Transcript saved ({len(transcript):,} characters)\n")
    except Exception as e:
        print(f"   ❌ Error: {e}\n")
        return

    # Get chapters (optional, can fail)
    print("🔄 Extracting video chapters...")
    try:
        chapters = yt_chapters(video_url)
        if chapters and len(chapters) > 0:
            chapters_file = output_dir / "chapters.txt"
            with open(chapters_file, 'w') as f:
                for i, chapter in enumerate(chapters[:20], 1):
                    f.write(f"{i}. {chapter}\n")
            print(f"   ✅ Chapters saved\n")
        else:
            print(f"   ⚠️  No chapters found\n")
    except Exception as e:
        print(f"   ⚠️  Could not extract chapters: {e}\n")

    # Generate slide outline
    print("🔄 Generating slide outline...")
    try:
        outline = outline_slides(str(slides_pdf))
        outline_file = output_dir / "slide_outline.md"
        with open(outline_file, 'w') as f:
            f.write(outline)
        print(f"   ✅ Slide outline saved\n")
    except Exception as e:
        print(f"   ❌ Error: {e}\n")
        return

    # ========================================
    # STEP 2: Generate Summary Version
    # ========================================
    print("=" * 60)
    print("STEP 2: Generating Summary Version")
    print("=" * 60 + "\n")

    prompt_summary = f"""You are an expert technical writer specializing in AI/ML content.

I have a technical talk that I want to turn into a comprehensive blog post summary.

VIDEO URL: {video_url}

SLIDE OUTLINE:
{outline}

FULL TRANSCRIPT (with timestamps):
{transcript[:30000]}... [transcript continues]

Please create a polished, engaging blog post that:

1. **Structure**:
   - Start with a compelling introduction
   - Use clear section headings
   - Include relevant quotes from the transcript
   - Add timestamps as links (e.g., [00:15:30]({video_url}&t=930s))
   - Reference specific slides (e.g., "As shown in slide 13...")

2. **Style**:
   - Write in an engaging, accessible tone
   - Explain technical concepts clearly
   - Use markdown formatting
   - Include key insights and takeaways

3. **Content** (Cover main topics):
   - Problem overview and why it matters
   - Key technical approaches discussed
   - Practical insights and recommendations
   - Conclusion with takeaways

4. **Format**:
   - Use proper markdown
   - Include image placeholders like: `![Slide 5](images/slide_5.png)`
   - Target length: ~1,200 words

Generate the blog post now:"""

    print("🔄 Generating summary with Gemini...\n")
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt_summary,
            config=types.GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=8192,
            )
        )

        summary = response.text
        summary_file = output_dir / "blog_post_summary.md"
        with open(summary_file, 'w') as f:
            f.write(summary)

        print(f"   ✅ Summary generated ({len(summary):,} characters)\n")
    except Exception as e:
        print(f"   ❌ Error: {e}\n")
        return

    # ========================================
    # STEP 3: Generate Full Annotated Version
    # ========================================
    print("=" * 60)
    print("STEP 3: Generating Full Annotated Version")
    print("=" * 60 + "\n")

    prompt_full = f"""You are creating a comprehensive, annotated blog post from a technical talk.

VIDEO URL: {video_url}

SLIDE SUMMARIES ({num_images} slides):
{outline}

FULL TRANSCRIPT WITH TIMESTAMPS:
{transcript}

Create a blog post that integrates the COMPLETE transcript with ALL slides at the appropriate moments.

REQUIREMENTS:

1. **Main Content - Annotated Transcript**:
   - Include the COMPLETE transcript, organized into logical sections
   - Embed slide images at the exact moment they're discussed
   - Format: `![Slide X: Brief description](images/slide_X.png)`
   - Add section headers to break up the content
   - Keep ALL the original spoken words - don't summarize
   - Add timestamp links: `[MM:SS](video_url&t=XXs)`

2. **Slide Placement**:
   - Use the slide summaries to determine WHEN each slide appears
   - Match slide topics to transcript content
   - Embed ALL slides in order

3. **Structure**: Break the content into logical sections based on the talk flow

4. **Important**:
   - DO NOT summarize - include the full transcript
   - DO NOT skip slides - embed all of them
   - DO maintain chronological order

Generate the complete annotated blog post now:"""

    print("🔄 Generating full annotated version with Gemini...")
    print("   (This takes longer - processing full transcript)\n")

    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt_full,
            config=types.GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=30000,
            )
        )

        full = response.text
        full_file = output_dir / "blog_post_full.md"
        with open(full_file, 'w') as f:
            f.write(full)

        slide_count = full.count('![Slide')
        print(f"   ✅ Full version generated ({len(full):,} characters, {slide_count} slides)\n")
    except Exception as e:
        print(f"   ❌ Error: {e}\n")
        return

    # ========================================
    # COMPLETE!
    # ========================================
    print("=" * 60)
    print("✅ Pipeline Complete!")
    print("=" * 60)
    print(f"\n📂 Output files in: {output_dir}")
    print(f"   - images/ ({num_images} slides)")
    print(f"   - transcript.txt")
    print(f"   - slide_outline.md")
    print(f"   - blog_post_summary.md (~1,200 words)")
    print(f"   - blog_post_full.md (~9,000 words)")
    print(f"\n💡 Next: Create Quarto post with both versions in tabs")

if __name__ == "__main__":
    main()
