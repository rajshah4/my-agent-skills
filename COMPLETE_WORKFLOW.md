# Complete Video-to-Blog Workflow
## From YouTube Video to Published Blog Post

**Total time:** ~10 minutes (mostly automated)

---

## Quick Start (For Future Talks)

```bash
# 1. Activate environment
cd ~/Code/my-agent-skills
source .venv/bin/activate

# 2. Edit video_to_blog.py - Update CONFIG section (lines 21-32)
nano video_to_blog.py

# 3. Run pipeline (extracts, generates summary + full)
python video_to_blog.py

# 4. Create Quarto post - Edit create_quarto_post.py CONFIG
nano create_quarto_post.py
python create_quarto_post.py

# 5. Deploy to server
cd ~/Code/rajistics_blog
python deploy_blog.py

# Done! 🎉
```

---

## Detailed Workflow

### Step 1: Generate Content from Video + Slides

**Script:** `video_to_blog.py`

**Edit CONFIG section:**
```python
CONFIG = {
    "video_url": "https://youtu.be/YOUR_VIDEO_ID",
    "slides_pdf": Path.home() / "Downloads" / "YOUR_SLIDES.pdf",
    "talk_name": "your-talk-name",  # Used for directories
    "title": "Your Talk Title",
    "date": "2025-01-15",
    "categories": ["Category1", "Category2"],
}
```

**Run:**
```bash
python video_to_blog.py
```

**Output:**
```
output/your-talk-name/
├── images/ (slide PNGs)
├── transcript.txt
├── slide_outline.md
├── blog_post_summary.md      (~1,200 words)
└── blog_post_full.md         (~9,000 words)
```

**Time:** ~5 minutes

---

### Step 2: Create Quarto Blog Post

**Script:** `create_quarto_post.py`

**Edit CONFIG section:**
```python
CONFIG = {
    "talk_name": "your-talk-name",  # Match Step 1
    "post_filename": "descriptive-name.qmd",
    "title": "Your Talk Title",
    "date": "2025-01-15",
    "categories": ["Category1", "Category2"],
    "video_url": "https://youtu.be/YOUR_VIDEO_ID",
}
```

**Run:**
```bash
python create_quarto_post.py
```

**What it does:**
- Creates .qmd file with Summary/Full tabs
- Updates image URLs to https://rajivshah.com/images/talk-name/...
- Renders with Quarto automatically
- Ready for deployment

**Output:**
```
~/Code/rajistics_blog/
├── your-post.qmd  (source)
└── web/
    └── your-post.html  (rendered)
```

**Time:** ~1 minute

---

### Step 3: Deploy to Website

**Method:** Git-based deployment via Vercel

**Run:**
```bash
# 1. Copy images to website
mkdir -p ~/Code/rajiv-shah-website/public/blog/images/[talk-name]
cp ~/Code/my-agent-skills/output/[talk-name]/images/* \
   ~/Code/rajiv-shah-website/public/blog/images/[talk-name]/

# 2. Re-render blog index (IMPORTANT!)
cd ~/Code/rajistics_blog
quarto render index.qmd

# 3. Commit and push to GitHub
cd ~/Code/rajiv-shah-website
git add public/blog/
git commit -m "Add new blog post: [title]"
git push
```

**What it does:**
1. Copies slide images to website public directory
2. Updates blog index with new post metadata
3. Deploys to rajivshah.com/blog via GitHub → Vercel

**Time:** ~1-2 minutes

---

## File Structure

```
~/Code/
├── my-agent-skills/
│   ├── .env                       (API keys)
│   ├── .venv/                    (Python environment)
│   ├── video_to_blog.py          (Step 1: Generate content)
│   ├── create_quarto_post.py     (Step 2: Create Quarto post)
│   ├── WORKFLOW.md               (Documentation)
│   ├── COMPLETE_WORKFLOW.md      (This file)
│   └── output/
│       └── talk-name/
│           ├── images/           (Uploaded to server)
│           ├── blog_post_summary.md
│           └── blog_post_full.md
│
└── rajistics_blog/
    ├── .env                      (SFTP credentials)
    ├── deploy_blog.py            (Step 3: Deploy)
    ├── your-talk.qmd             (Quarto source)
    └── web/                      (Rendered HTML, uploaded to server)
```

---

## Configuration Files

### my-agent-skills/.env
```bash
GEMINI_API_KEY=your_key
GEMINI_MODEL=gemini-3-pro-preview
TEMPERATURE=0.7

OPENAI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key
```

### rajistics_blog/.env
```bash
login=root
password=your_password
```

---

## Image Handling

**Local (during generation):**
```
output/talk-name/images/slide_1.png
```

**In markdown (after create_quarto_post.py):**
```markdown
![](https://rajivshah.com/images/talk-name/slide_1.png)
```

**On server (after deploy):**
```
/var/www/html/images/talk-name/slide_1.png
```

**Live URL:**
```
https://rajivshah.com/images/talk-name/slide_1.png
```

---

## Troubleshooting

### "sshpass not found"
```bash
brew install hudochenkov/sshpass/sshpass
```

### "Quarto not found"
```bash
# Install Quarto
brew install quarto

# Or render manually
cd ~/Code/rajistics_blog
quarto render your-post.qmd
```

### "API quota exceeded"
- Wait a few minutes
- Check Gemini console for quota

### Images not showing
- Check image URLs in .qmd file (should be https://rajivshah.com/images/...)
- Verify images uploaded: ls /var/www/html/images/talk-name/ on server
- Check deploy_blog.py ran successfully

---

## Tips & Best Practices

### Naming Convention
Use descriptive, URL-friendly names:
```python
"talk_name": "rag-agentic-world"      # Good
"talk_name": "rag talk"               # Bad (spaces)
"talk_name": "talk1"                  # Bad (not descriptive)
```

### Categories
Use consistent categories across posts:
```python
"categories": ["RAG", "AI", "Retrieval"]  # Good
"categories": ["rag", "AI stuff"]         # Bad (inconsistent)
```

### Dates
Use ISO format:
```python
"date": "2025-01-15"  # Good
"date": "Jan 15"      # Bad
```

### Video Length
- < 30 mins: Works perfectly
- 30-60 mins: Works well (tested)
- > 60 mins: May hit token limits, consider splitting

---

## Success Checklist

After completing the workflow, verify:
- ✅ Blog post has both Summary and Full tabs
- ✅ Images load correctly in browser
- ✅ Video link works
- ✅ Timestamps link to correct moments in video
- ✅ Post appears on blog listing page
- ✅ Mobile view looks good

---

## Future Enhancements

### Potential Improvements:
1. **Single unified script** - One command for everything
2. **Interactive prompts** - Ask for video URL, title, etc.
3. **Automatic title generation** - Extract from video metadata
4. **Image optimization** - Convert to WebP, compress
5. **Social media preview cards** - Auto-generate
6. **Error recovery** - Resume from failed steps

### Next Steps:
- Consider creating a Claude Code skill
- Add automated testing
- Set up CI/CD for blog deployment

---

## Example: RAG Talk

This workflow was used to create the RAG talk blog post:

1. **Input:**
   - Video: https://youtu.be/AS_HlJbJjH8
   - Slides: RAG_Oct2025.pdf (71 slides)

2. **Output:**
   - Summary: 1,166 words
   - Full: 9,167 words with all 71 slides
   - Processing time: ~8 minutes

3. **Result:**
   - Live at: https://rajivshah.com/blog/rag-agentic-world.html
   - Both versions accessible via tabs
   - All images loading correctly

---

## Support

- **Documentation:** See WORKFLOW.md for detailed docs
- **Scripts:** All scripts have inline comments
- **Issues:** Check troubleshooting section first

---

**Last Updated:** 2025-01-01
**Version:** 1.0
