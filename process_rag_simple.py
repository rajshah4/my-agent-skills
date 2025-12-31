#!/usr/bin/env python3
"""
Simpler workflow: Process RAG talk video and slides into a blog post
Using individual tools instead of the complex generate_annotated_talk_post
"""

from dotenv import load_dotenv
from hamel.writing import pdf2imgs, outline_slides
from hamel.yt import transcribe, yt_chapters
from pathlib import Path
import os

# Load environment variables
load_dotenv()

print("🎬 Processing RAG Talk Video → Blog Post (Simple Workflow)\n")
print("=" * 60)

# Configuration
video_url = "https://youtu.be/AS_HlJbJjH8"
slides_pdf = Path.home() / "Downloads" / "RAG_Oct2025.pdf"
output_dir = Path.home() / "Code" / "my-agent-skills" / "output" / "rag-talk"
image_dir = output_dir / "images"

print(f"\n📹 Video: {video_url}")
print(f"📄 Slides: {slides_pdf}")
print(f"📁 Output: {output_dir}")
print(f"🖼️  Images: {image_dir}\n")

# Step 1: Convert PDF to images
print("🔄 Step 1: Converting PDF slides to images...")
try:
    pdf2imgs(str(slides_pdf), str(image_dir))
    num_images = len(list(image_dir.glob("*.png")))
    print(f"   ✅ Created {num_images} slide images\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")

# Step 2: Get transcript
print("🔄 Step 2: Fetching video transcript...")
try:
    transcript = transcribe(video_url)
    transcript_file = output_dir / "transcript.txt"
    with open(transcript_file, 'w') as f:
        f.write(transcript)
    print(f"   ✅ Transcript saved ({len(transcript):,} characters)\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")
    transcript = None

# Step 3: Get chapters
print("🔄 Step 3: Extracting video chapters...")
try:
    chapters = yt_chapters(video_url)
    if chapters and isinstance(chapters, (list, tuple)) and len(chapters) > 0:
        chapters_file = output_dir / "chapters.txt"
        with open(chapters_file, 'w') as f:
            for i, chapter in enumerate(chapters[:20], 1):  # Limit to first 20
                f.write(f"{i}. {chapter}\n")
        print(f"   ✅ Saved {min(len(chapters), 20)} chapters\n")
    else:
        print(f"   ⚠️  No chapters found or format unexpected\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")

# Step 4: Create slide outline
print("🔄 Step 4: Generating slide outline...")
try:
    outline = outline_slides(str(slides_pdf))
    outline_file = output_dir / "slide_outline.md"
    with open(outline_file, 'w') as f:
        f.write(outline)
    print(f"   ✅ Slide outline saved\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")
    outline = None

# Step 5: Create a simple blog post template
print("🔄 Step 5: Creating blog post template...")
try:
    blog_template = f"""---
title: "RAG Talk - October 2025"
date: {Path(slides_pdf).stat().st_mtime}
video: {video_url}
---

# RAG Talk - October 2025

## Video

Watch the full talk here: [{video_url}]({video_url})

## Slide Outline

{outline if outline else "See slide_outline.md"}

## Transcript

{transcript[:1000] if transcript else "See transcript.txt"}...

[Full transcript available in transcript.txt]

## Slides

The slides have been extracted to the `images/` directory.

"""

    blog_file = output_dir / "blog_post_template.md"
    with open(blog_file, 'w') as f:
        f.write(blog_template)

    print(f"   ✅ Blog post template created\n")
except Exception as e:
    print(f"   ❌ Error: {e}\n")

print("=" * 60)
print(f"✅ Processing complete!")
print(f"\n📂 Output files:")
print(f"   - Images: {image_dir}/")
print(f"   - Transcript: {output_dir}/transcript.txt")
print(f"   - Chapters: {output_dir}/chapters.txt")
print(f"   - Slide outline: {output_dir}/slide_outline.md")
print(f"   - Blog template: {output_dir}/blog_post_template.md")
print(f"\n💡 Next: You can now manually edit the blog post or use Gemini to enhance it!")
