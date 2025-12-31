# Using the Writing Tools

This repo contains both AI skills (for Claude Code) and Python utilities (from Hamel's package) for converting videos/talks into blog posts.

## Setup

The Python utilities are installed in a virtual environment:

```bash
cd ~/Code/my-agent-skills

# Activate the virtual environment
source .venv/bin/activate

# Now you can use the writing tools
```

## Available Tools

### 1. Video → Blog Post (Main Workflow)

```python
from hamel.writing import generate_annotated_talk_post

# Convert a talk with slides + video into an annotated blog post
generate_annotated_talk_post(
    slide_path="path/to/slides.pdf",           # PDF of your slides
    video_source="https://youtu.be/VIDEO_ID",  # YouTube URL or local MP4 path
    image_dir="output/images",                 # Where to save slide images
    transcript_path=None,                      # Optional: path to transcript file
    example_urls=[...]                         # Optional: URLs of example posts for style
)
```

This will:
- Extract slides from PDF and convert to images
- Get video chapters and transcript
- Generate annotated markdown with embedded images
- Include timestamps linked to video
- Create Q&A sections for content not on slides

### 2. Individual Utilities

```python
from hamel.writing import (
    pdf2imgs,        # Convert PDF slides to images
    jina_get,        # Fetch website as markdown
    gather_urls,     # Aggregate markdown from multiple URLs
    outline_slides,  # Generate numbered slide summaries
)
from hamel.yt import yt_chapters  # Extract YouTube chapters
from hamel.yt import transcribe   # Get video transcript

# Convert PDF to images
pdf2imgs(pdf_path="slides.pdf", output_dir="images/")

# Get website as markdown
content = jina_get("https://example.com")

# Gather style examples from URLs
examples = gather_urls(["url1", "url2", "url3"])

# Get YouTube chapters
chapters = yt_chapters("https://youtu.be/VIDEO_ID")

# Get transcript
transcript = transcribe(video_source)
```

### 3. Using Skills in Claude Code

After restarting Claude Code, these skills are automatically available:

- `/youtube-transcribe` - Transcribe YouTube videos
- `/youtube-chapters` - Extract chapter markers
- `/annotate-talk` - Annotate talks with timestamps
- `/gem` - Generate educational materials
- `/zoom` - Process Zoom recordings
- `/kit` - Starter kit for projects

Just mention your task naturally and Claude will invoke the relevant skill when appropriate.

## Environment Variables

Make sure you have the required API keys in your environment:

```bash
# .env file
GEMINI_API_KEY=your_key_here  # For Gemini AI
```

## Examples

### Convert a conference talk to blog post:

```python
from hamel.writing import generate_annotated_talk_post

# Your talk slides and video
post = generate_annotated_talk_post(
    slide_path="~/Downloads/my-talk-slides.pdf",
    video_source="https://youtu.be/abc123",
    image_dir="~/blog/images/my-talk"
)

print(post)  # Markdown content ready for your blog
```

### Just get a YouTube transcript:

```python
from hamel.yt import transcribe

transcript = transcribe("https://youtu.be/abc123")
print(transcript)
```

## Updating

To update to the latest version of Hamel's utilities:

```bash
cd ~/Code/my-agent-skills
source .venv/bin/activate
uv pip install --upgrade git+https://github.com/hamelsmu/hamel.git
```

## Architecture

```
my-agent-skills/
├── skills/              # AI Skills for Claude Code (symlinked to ~/.claude/skills/)
│   ├── annotate-talk/
│   ├── youtube-transcribe/
│   └── ...
├── .venv/              # Virtual environment with hamel package
├── README.md           # General documentation
└── USAGE.md            # This file
```

**Two separate concerns:**
1. **Skills** - Guide Claude's behavior (what you're editing/customizing)
2. **Python utilities** - Command-line tools for video processing (installed via uv)

This separation keeps skills clean and makes the utilities easy to update.
