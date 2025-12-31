#!/usr/bin/env python3
"""
Create Quarto blog post with Summary/Full tabs
Handles content, images, and optionally renders with Quarto
"""

from pathlib import Path
import shutil
import subprocess
import re

# ============================================
# CONFIGURATION
# ============================================

CONFIG = {
    # Source (from video_to_blog.py output)
    "talk_name": "rag-talk",
    "source_dir": Path.home() / "Code" / "my-agent-skills" / "output" / "rag-talk",

    # Destination (Quarto blog)
    "blog_dir": Path.home() / "Code" / "rajistics_blog",

    # Quarto post filename
    "post_filename": "rag-agentic-world.qmd",

    # Quarto front matter
    "title": "From Vectors to Agents: Managing RAG in an Agentic World",
    "date": "2025-01-15",
    "categories": ["RAG", "AI", "Retrieval", "Agentic"],

    # Video URL
    "video_url": "https://youtu.be/AS_HlJbJjH8",

    # Options
    "auto_render": True,  # Run quarto render after creating
}

# ============================================
# HELPER FUNCTIONS
# ============================================

def strip_front_matter(content: str) -> str:
    """
    Remove YAML front matter from content if present.
    Front matter is detected as content between --- markers at the start.
    """
    # Pattern: starts with ---, has content, ends with ---
    pattern = r'^---\s*\n.*?\n---\s*\n'
    cleaned = re.sub(pattern, '', content, count=1, flags=re.DOTALL)
    return cleaned.strip()

# ============================================
# MAIN SCRIPT
# ============================================

def main():
    print("📝 Creating Quarto Blog Post\n")
    print("=" * 60)

    source_dir = CONFIG["source_dir"]
    blog_dir = CONFIG["blog_dir"]
    post_file = blog_dir / CONFIG["post_filename"]

    # Read the generated content
    print("\n📚 Reading generated content...")

    # Try different filename patterns (from different scripts)
    summary_file = source_dir / "blog_post_summary.md"
    if not summary_file.exists():
        summary_file = source_dir / "blog_post_polished.md"

    full_file = source_dir / "blog_post_full.md"
    if not full_file.exists():
        full_file = source_dir / "blog_post_annotated_full.md"

    if not summary_file.exists() or not full_file.exists():
        print(f"❌ Error: Content files not found in {source_dir}")
        print(f"   Looking for: {summary_file.name} and {full_file.name}")
        print("   Run video_to_blog.py first!")
        return

    with open(summary_file, 'r') as f:
        summary_content = f.read()

    with open(full_file, 'r') as f:
        full_content = f.read()

    print(f"   ✅ Summary: {len(summary_content):,} characters")
    print(f"   ✅ Full: {len(full_content):,} characters\n")

    # Strip any embedded front matter from AI-generated content
    print("🧹 Cleaning content...")
    summary_content = strip_front_matter(summary_content)
    full_content = strip_front_matter(full_content)
    print("   ✅ Removed any embedded front matter\n")

    # Update image paths to use full URLs (as in existing posts)
    print("🖼️  Updating image paths...")

    # Images will be at https://projects.rajivshah.com/images/talk-name/slide_X.png
    # Match the pattern from existing posts like running-code-failing-models.md
    image_base_url = f"https://projects.rajivshah.com/images/{CONFIG['talk_name']}"

    summary_content = summary_content.replace("images/", f"{image_base_url}/")
    full_content = full_content.replace("images/", f"{image_base_url}/")

    # Set cover image (first slide)
    cover_image = f"{image_base_url}/slide_1.png"

    print(f"   ✅ Image URLs updated to: {image_base_url}/...\n")

    # Create Quarto post with tabs
    print("📄 Creating Quarto post...")

    quarto_content = f"""---
title: "{CONFIG['title']}"
date: "{CONFIG['date']}"
categories: {CONFIG['categories']}
image: {cover_image}
---
![{CONFIG['title']}]({cover_image})

Watch the [full video]({CONFIG['video_url']}) (50 mins)

::: {{.panel-tabset}}

## Summary (5 min read)

{summary_content}

## Full Annotated Walkthrough (45 min read)

{full_content}

:::

---

*This post was generated from the talk using automated tools. Summary and full transcript available above.*
"""

    # Write the Quarto file
    with open(post_file, 'w') as f:
        f.write(quarto_content)

    print(f"   ✅ Created: {post_file.name}\n")

    # Optionally render with Quarto
    if CONFIG["auto_render"]:
        print("🔄 Rendering with Quarto...")
        try:
            result = subprocess.run(
                ["quarto", "render", str(post_file)],
                cwd=str(blog_dir),
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode == 0:
                print(f"   ✅ Rendered successfully\n")
            else:
                print(f"   ⚠️  Render had issues:\n{result.stderr}\n")
        except subprocess.TimeoutExpired:
            print(f"   ⚠️  Render timed out\n")
        except FileNotFoundError:
            print(f"   ⚠️  Quarto not found in PATH\n")
            print(f"      Run manually: cd ~/Code/rajistics_blog && quarto render {CONFIG['post_filename']}\n")

    # Summary
    print("=" * 60)
    print("✅ Quarto Post Created!")
    print("=" * 60)
    print(f"\n📂 Files:")
    print(f"   - Post: {post_file}")
    print(f"   - Rendered HTML: {blog_dir / 'web' / post_file.stem}.html")
    print(f"   - Source images: {source_dir / 'images'}/")

    print(f"\n🎯 Next Steps:")
    print(f"   1. Review: open {post_file}")
    if not CONFIG["auto_render"]:
        print(f"   2. Render: cd ~/Code/rajistics_blog && quarto render {CONFIG['post_filename']}")
    print(f"   3. Deploy: python deploy_blog.py")
    print(f"      (Uploads web/ and images/ to projects.rajivshah.com)")

if __name__ == "__main__":
    main()
