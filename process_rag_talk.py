#!/usr/bin/env python3
"""
Process RAG talk video and slides into a blog post
"""

from dotenv import load_dotenv
from hamel.writing import generate_annotated_talk_post
from pathlib import Path
import httpx

# Load environment variables
load_dotenv()

def fetch_example_urls_directly():
    """Fetch example blog posts directly without Jina"""
    example_urls = [
        'https://raw.githubusercontent.com/hamelsmu/hamel-site/refs/heads/master/notes/llm/evals/inspect.qmd',
        'https://raw.githubusercontent.com/hamelsmu/hamel-site/refs/heads/master/notes/llm/rag/p1-intro.md',
        'https://raw.githubusercontent.com/hamelsmu/hamel-site/refs/heads/master/notes/llm/rag/p2-evals.md',
    ]

    print("📚 Fetching example blog posts for style reference...")
    contents = []
    for url in example_urls:
        try:
            response = httpx.get(url, timeout=10.0)
            if response.status_code == 200:
                contents.append(response.text)
                print(f"   ✅ Fetched: {url.split('/')[-1]}")
        except Exception as e:
            print(f"   ⚠️  Failed to fetch {url.split('/')[-1]}: {e}")

    return '\n\n'.join(contents) if contents else None

print("🎬 Processing RAG Talk Video → Blog Post\n")
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

# Run the workflow
print("🔄 Running generate_annotated_talk_post...\n")

try:
    blog_post = generate_annotated_talk_post(
        slide_path=str(slides_pdf),
        video_source=video_url,
        image_dir=str(image_dir),
        transcript_path=None,  # Will auto-fetch from YouTube
        example_urls=[]  # Skip style examples to avoid needing JINA_READER_KEY
    )

    # Save the blog post
    output_file = output_dir / "blog_post.md"
    with open(output_file, 'w') as f:
        f.write(blog_post)

    print("=" * 60)
    print(f"✅ Blog post generated successfully!")
    print(f"📝 Saved to: {output_file}")
    print(f"🖼️  Images saved to: {image_dir}")
    print(f"\n📊 Stats:")
    print(f"   - Blog post length: {len(blog_post):,} characters")
    print(f"   - Word count: ~{len(blog_post.split()):,} words")

    # Show first 500 characters
    print(f"\n📖 Preview (first 500 chars):")
    print("-" * 60)
    print(blog_post[:500])
    print("-" * 60)

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
