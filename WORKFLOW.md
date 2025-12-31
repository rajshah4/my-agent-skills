# Video-to-Blog Post Workflow

Complete workflow for converting technical talks (video + slides) into blog posts.

## Overview

**Input:**
- YouTube video URL
- PDF slides
- Optional: transcript file

**Output:**
- Summary blog post (~1,200 words)
- Full annotated walkthrough (~9,000 words)
- 71 slide images
- Transcript, chapters, slide outline
- Quarto-ready markdown with tabs

**Time:** ~5-10 minutes (mostly AI generation)

---

## Prerequisites

### 1. Environment Setup

```bash
cd ~/Code/my-agent-skills
source .venv/bin/activate
```

### 2. Required API Keys (.env)

```bash
GEMINI_API_KEY=your_key      # Required
GEMINI_MODEL=gemini-3-pro-preview
```

### 3. Input Files

- Video URL (YouTube)
- Slides PDF (in ~/Downloads or specify path)

---

## Step-by-Step Workflow

### Step 1: Extract Raw Materials

**Script:** `process_rag_simple.py` (or customize for your talk)

**What it does:**
1. Converts PDF slides → PNG images (one per slide)
2. Fetches video transcript from YouTube
3. Extracts video chapters (if available)
4. Generates AI slide outline/summaries

**Run it:**
```bash
python process_rag_simple.py
```

**Customize for new talks:**
```python
# Edit these lines:
video_url = "https://youtu.be/YOUR_VIDEO_ID"
slides_pdf = Path.home() / "Downloads" / "YOUR_SLIDES.pdf"
output_dir = Path.home() / "Code" / "my-agent-skills" / "output" / "YOUR_TALK_NAME"
```

**Output:**
```
output/your-talk-name/
├── images/
│   ├── slide_1.png
│   ├── slide_2.png
│   └── ... (all slides)
├── transcript.txt
├── chapters.txt
├── slide_outline.md
└── blog_post_template.md
```

---

### Step 2: Generate Summary Version

**Script:** `polish_blog_post.py`

**What it does:**
- Takes transcript + slide outline
- Uses Gemini to create polished summary (~1,200 words)
- Includes key insights, quotes, selected slides
- Professional blog post format

**Customize:**
```python
# Update paths to match your talk
output_dir = Path.home() / "Code" / "my-agent-skills" / "output" / "YOUR_TALK_NAME"
video_url = "https://youtu.be/YOUR_VIDEO_ID"
```

**Run it:**
```bash
python polish_blog_post.py
```

**Output:** `output/your-talk-name/blog_post_polished.md`

---

### Step 3: Generate Full Annotated Version

**Script:** `generate_annotated_post.py`

**What it does:**
- Integrates COMPLETE transcript with ALL slides
- Embeds slides at exact moments discussed
- Adds timestamps linking to video
- Creates walkthrough experience (~9,000 words)

**Customize:**
```python
# Update paths
output_dir = Path.home() / "Code" / "my-agent-skills" / "output" / "YOUR_TALK_NAME"
video_url = "https://youtu.be/YOUR_VIDEO_ID"
```

**Run it:**
```bash
python generate_annotated_post.py
```

**Output:** `output/your-talk-name/blog_post_annotated_full.md`

---

### Step 4: Create Quarto Blog Post

**Script:** `create_quarto_post.py` (to be created)

**What it does:**
- Combines both versions into Quarto tabbed format
- Adds proper front matter
- Copies to your blog directory
- Handles image paths

**Output:** Ready-to-publish Quarto .qmd file

---

## Quick Reference: Full Workflow

```bash
# 1. Activate environment
cd ~/Code/my-agent-skills
source .venv/bin/activate

# 2. Edit scripts with your video URL and slide path
# - process_rag_simple.py
# - polish_blog_post.py
# - generate_annotated_post.py

# 3. Run the pipeline
python process_rag_simple.py       # Extract materials (~2 min)
python polish_blog_post.py         # Generate summary (~1 min)
python generate_annotated_post.py  # Generate full version (~2 min)

# 4. Create Quarto post
python create_quarto_post.py       # Combine into Quarto format

# 5. Build and publish
cd ~/Code/rajistics_blog
quarto render your-talk.qmd
# Copy web/ contents to rajivshah.com/blog
```

---

## File Structure

```
my-agent-skills/
├── .env                              # API keys
├── .venv/                           # Python environment
├── output/
│   └── talk-name/
│       ├── images/                  # Slide PNGs
│       ├── transcript.txt
│       ├── slide_outline.md
│       ├── blog_post_polished.md    # Summary version
│       └── blog_post_annotated_full.md  # Full version
├── process_rag_simple.py            # Step 1: Extract
├── polish_blog_post.py              # Step 2: Summary
├── generate_annotated_post.py       # Step 3: Full
└── create_quarto_post.py            # Step 4: Quarto (TBD)
```

---

## Customization Points

### For Each New Talk:

1. **Output directory name** - Use descriptive name:
   ```python
   output_dir = .../output/rag-talk-oct2025/
   ```

2. **Video URL**:
   ```python
   video_url = "https://youtu.be/NEW_VIDEO_ID"
   ```

3. **Slides PDF path**:
   ```python
   slides_pdf = Path.home() / "Downloads" / "NEW_SLIDES.pdf"
   ```

4. **Quarto metadata**:
   ```yaml
   title: "Your Talk Title"
   date: "2025-01-15"
   categories: [Category1, Category2]
   ```

---

## Tips & Best Practices

### Image Handling
- Slides are converted to PNG (high quality)
- Average ~260KB per slide
- Consider optimizing for web (WebP format)

### Gemini Model Selection
- `gemini-3-pro-preview` - Best quality (current default)
- `gemini-2.0-flash-exp` - Faster, good quality
- Adjust in `.env`: `GEMINI_MODEL=your_choice`

### Token Limits
- Summary generation: 8,192 tokens (sufficient)
- Full annotation: 30,000 tokens (handles long transcripts)
- If video > 60 mins, may need to split

### Error Handling
- Missing chapters: OK, script continues
- JINA_READER_KEY: Optional, not needed
- Gemini errors: Check API key and model availability

---

## Future Improvements

### Potential Enhancements:
1. **Single unified script** - Run entire pipeline with one command
2. **Config file** - YAML config instead of editing Python
3. **Claude Code skill** - Invoke from Claude Code chat
4. **Image optimization** - Auto-convert to WebP
5. **Auto-publish** - Direct push to blog

### Next Steps:
- Create wrapper script that runs all steps
- Build Quarto template generator
- Consider MCP server for repeatable workflows

---

## Troubleshooting

### Common Issues:

**"JINA_READER_KEY not set"**
- Not needed! Scripts updated to skip example URLs
- Can safely ignore this error

**"API quota exceeded"**
- Wait a few minutes
- Check Gemini API quota in console

**"Model not found"**
- Check model name in `.env`
- Try `gemini-2.0-flash-exp` as fallback

**Images not loading**
- Check image paths in markdown
- Ensure images copied to correct directory
- Verify relative paths work in Quarto

---

## Success Metrics

After running the workflow, you should have:
- ✅ 71+ slide images (or however many in your PDF)
- ✅ Complete transcript with timestamps
- ✅ AI-generated slide summaries
- ✅ Professional summary blog post (~1,200 words)
- ✅ Full annotated walkthrough (~9,000 words)
- ✅ Quarto-ready markdown file
- ✅ Total time: 5-10 minutes

---

## Examples

See `output/rag-talk/` for a complete example of all outputs from the RAG talk.
