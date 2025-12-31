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
    "date": "2025-10-27",
    "categories": ["RAG", "AI", "Retrieval", "Agentic", "Annotated Talk"],
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
    # STEP 2: Generate Slide-by-Slide Annotation
    # ========================================
    print("=" * 60)
    print("STEP 2: Generating Slide-by-Slide Annotations")
    print("=" * 60 + "\n")

    prompt_annotated = f"""You are creating a slide-by-slide annotated presentation from a technical talk.

VIDEO URL: {video_url}

SLIDE SUMMARIES ({num_images} slides):
{outline}

FULL TRANSCRIPT WITH TIMESTAMPS:
{transcript}

Create an annotated presentation that goes through EACH slide sequentially. For each slide:

1. **Slide Header**: Format as "### N. [Slide Title]" where N is the slide number
2. **Image**: Embed the slide image: `![Slide N](images/slide_N.png)`
3. **Timestamp**: Add a timestamp link in format: `([Timestamp: MM:SS]({video_url}&t=XXXs))`
4. **Explanation**: Write 2-3 paragraphs explaining:
   - What the slide shows
   - Key concepts introduced
   - Important details from the transcript
   - Why this matters or how it connects to other concepts

REQUIREMENTS:

- Go through ALL {num_images} slides in sequential order (1, 2, 3...)
- Match each slide to the relevant part of the transcript using timestamps
- Use the slide outline to understand what each slide is about
- Keep explanations clear and technical but accessible
- Bold key terms and concepts
- Include relevant quotes from the transcript
- Maintain a progressive flow from basic to advanced concepts

FORMAT EXAMPLE:
### 1. Introduction to Topic

![Slide 1](images/slide_1.png)

([Timestamp: 01:23]({video_url}&t=83s))

First paragraph explaining what this slide introduces...

Second paragraph with key details and context...

Third paragraph connecting to next concepts...

Generate the complete slide-by-slide annotation now:"""

    print("🔄 Generating slide-by-slide annotations with Gemini...")
    print("   (This processes all slides and transcript)\n")

    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt_annotated,
            config=types.GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=30000,
            )
        )

        annotated = response.text
        annotated_file = output_dir / "blog_post_annotated.md"
        with open(annotated_file, 'w') as f:
            f.write(annotated)

        slide_count = annotated.count('![Slide')
        print(f"   ✅ Annotated presentation generated ({len(annotated):,} characters, {slide_count} slides)\n")
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
    print(f"   - blog_post_annotated.md (slide-by-slide format)")
    print(f"\n💡 Next: Create Quarto post with annotated presentation")

if __name__ == "__main__":
    main()
