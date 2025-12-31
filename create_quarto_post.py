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
    "talk_name": "model-interpretability-explainability",
    "source_dir": Path.home() / "Code" / "my-agent-skills" / "output" / "model-interpretability-explainability",

    # Destination (Quarto blog)
    "blog_dir": Path.home() / "Code" / "rajistics_blog",

    # Quarto post filename
    "post_filename": "model-interpretability-explainability.qmd",

    # Quarto front matter
    "title": "Model Interpretability and Explainability for Machine Learning Models",
    "date": "2020-04-15",
    "categories": ["Interpretability", "Explainability", "Machine Learning", "XAI", "Annotated Talk"],

    # Video URL
    "video_url": "https://youtu.be/ZRckw_fE56Q",

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

    # Look for the annotated presentation file
    annotated_file = source_dir / "blog_post_annotated.md"
    if not annotated_file.exists():
        print(f"❌ Error: Content file not found in {source_dir}")
        print(f"   Looking for: {annotated_file.name}")
        print("   Run video_to_blog.py first!")
        return

    with open(annotated_file, 'r') as f:
        annotated_content = f.read()

    print(f"   ✅ Annotated content: {len(annotated_content):,} characters\n")

    # Strip any embedded front matter from AI-generated content
    print("🧹 Cleaning content...")
    annotated_content = strip_front_matter(annotated_content)
    print("   ✅ Removed embedded front matter\n")

    # Update image paths to use full URLs (as in existing posts)
    print("🖼️  Updating image paths...")

    # Images will be at https://rajivshah.com/blog/images/talk-name/slide_X.png
    image_base_url = f"https://rajivshah.com/blog/images/{CONFIG['talk_name']}"

    annotated_content = annotated_content.replace("images/", f"{image_base_url}/")

    # Set cover image (first slide)
    cover_image = f"{image_base_url}/slide_1.png"

    print(f"   ✅ Image URLs updated to: {image_base_url}/...\n")

    # Create Quarto post
    print("📄 Creating Quarto post...")

    quarto_content = f"""---
title: "{CONFIG['title']}"
date: "{CONFIG['date']}"
categories: {CONFIG['categories']}
image: {cover_image}
toc: true
toc-depth: 2
---

## Video

{{{{< video {CONFIG['video_url']} >}}}}

Watch the [full video]({CONFIG['video_url']})

---

## Annotated Presentation

Below is an annotated version of the presentation, with timestamped links to the relevant parts of the video for each slide.

{annotated_content}

---

*This annotated presentation was generated from the talk using AI-assisted tools. Each slide includes timestamps and detailed explanations.*
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
    print(f"   3. Copy images to website:")
    print(f"      mkdir -p ~/Code/rajiv-shah-website/public/blog/images/{CONFIG['talk_name']}")
    print(f"      cp {source_dir / 'images'}/* ~/Code/rajiv-shah-website/public/blog/images/{CONFIG['talk_name']}/")
    print(f"   4. Re-render index: cd ~/Code/rajistics_blog && quarto render index.qmd")
    print(f"   5. Deploy: cd ~/Code/rajiv-shah-website && git add . && git commit && git push")
    print(f"      (Deploys to rajivshah.com/blog via GitHub)")

if __name__ == "__main__":
    main()
