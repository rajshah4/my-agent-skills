#!/usr/bin/env python3
"""
Quick test of the video-to-blog workflow tools
"""

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

print("🔧 Testing Video-to-Blog Workflow Tools\n")
print("=" * 60)

# Test 1: Check environment variables
print("\n1️⃣ Testing Environment Variables...")
gemini_key = os.getenv('GEMINI_API_KEY')
if gemini_key:
    print(f"   ✅ GEMINI_API_KEY loaded: {gemini_key[:10]}...")
else:
    print("   ❌ GEMINI_API_KEY not found")

# Test 2: Import modules
print("\n2️⃣ Testing Module Imports...")
try:
    from hamel.yt import transcribe, yt_chapters
    from hamel.writing import gather_urls, jina_get
    print("   ✅ All modules imported successfully")
except ImportError as e:
    print(f"   ❌ Import error: {e}")
    exit(1)

# Test 3: Get YouTube transcript
print("\n3️⃣ Testing YouTube Transcript...")
# Using a short video about Python (Fireship's 100 seconds of Python)
test_video = "https://youtu.be/x7X9w_GIm1s"
print(f"   Video: {test_video}")
try:
    transcript = transcribe(test_video)
    if transcript:
        print(f"   ✅ Transcript retrieved: {len(transcript)} characters")
        print(f"   First 200 chars: {transcript[:200]}...")
    else:
        print("   ⚠️  Transcript is empty")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 4: Get YouTube chapters
print("\n4️⃣ Testing YouTube Chapters...")
try:
    chapters = yt_chapters(test_video)
    if chapters:
        print(f"   ✅ Chapters retrieved: {len(chapters)} chapters")
        for i, chapter in enumerate(chapters[:3], 1):  # Show first 3
            print(f"      {i}. {chapter}")
    else:
        print("   ⚠️  No chapters found (video may not have chapters)")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 5: Test jina_get (web content extraction)
print("\n5️⃣ Testing Web Content Extraction...")
test_url = "https://www.example.com"
print(f"   URL: {test_url}")
try:
    content = jina_get(test_url)
    if content:
        print(f"   ✅ Content retrieved: {len(content)} characters")
        print(f"   First 100 chars: {content[:100]}...")
    else:
        print("   ⚠️  Content is empty")
except Exception as e:
    print(f"   ❌ Error: {e}")

print("\n" + "=" * 60)
print("✨ Testing complete!\n")
