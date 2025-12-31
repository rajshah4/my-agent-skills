#!/bin/bash
###############################################################################
# Deploy Quarto Blog to rajivshah.com via Git
#
# NOTE: This script is deprecated. The blog now deploys via GitHub.
#
# New deployment process:
# 1. Copy images to ~/Code/rajiv-shah-website/public/blog/images/[talk-name]/
# 2. Re-render index: cd ~/Code/rajistics_blog && quarto render index.qmd
# 3. Git commit and push from ~/Code/rajiv-shah-website
# 4. Vercel automatically deploys to rajivshah.com/blog
###############################################################################

set -e  # Exit on error

# ============================================
# CONFIGURATION - Edit these paths
# ============================================

BLOG_DIR="$HOME/Code/rajistics_blog"
SERVER="rajivshah.com"
USER="root"
REMOTE_BLOG_PATH="/var/www/html/blog"  # Update with actual path
REMOTE_IMAGES_PATH="/var/www/html/images"  # Update with actual path

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# ============================================
# FUNCTIONS
# ============================================

print_section() {
    echo ""
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}📝 $1${NC}"
}

# ============================================
# MAIN DEPLOYMENT
# ============================================

print_section "Starting Blog Deployment"

# Check if blog directory exists
if [ ! -d "$BLOG_DIR" ]; then
    echo "❌ Error: Blog directory not found: $BLOG_DIR"
    exit 1
fi

cd "$BLOG_DIR"

# Render the blog (optional - comment out if already rendered)
print_section "Step 1: Rendering Quarto Blog"
if command -v quarto &> /dev/null; then
    print_info "Running quarto render..."
    quarto render
    print_success "Blog rendered"
else
    print_info "Quarto not found, skipping render (assuming already rendered)"
fi

# Check if web directory exists
if [ ! -d "$BLOG_DIR/web" ]; then
    echo "❌ Error: web/ directory not found. Run 'quarto render' first."
    exit 1
fi

# Deploy using rsync over SSH (most efficient)
print_section "Step 2: Deploying to Server"

print_info "Syncing blog content to $SERVER..."

# Using rsync (more efficient than SFTP for directories)
# -a: archive mode (preserves permissions, timestamps, etc.)
# -v: verbose
# -z: compress during transfer
# --delete: remove files on server that don't exist locally
# --exclude: don't delete these files on server

rsync -avz --delete \
    --exclude='.DS_Store' \
    --exclude='*.Rproj' \
    "$BLOG_DIR/web/" \
    "$USER@$SERVER:$REMOTE_BLOG_PATH/"

if [ $? -eq 0 ]; then
    print_success "Blog content deployed"
else
    echo "❌ Error deploying blog content"
    exit 1
fi

# Deploy images if they exist
print_section "Step 3: Deploying Images"

# Find all *-images directories
IMAGE_DIRS=$(find "$BLOG_DIR" -maxdepth 1 -type d -name "*-images" 2>/dev/null)

if [ -n "$IMAGE_DIRS" ]; then
    print_info "Found image directories, syncing to server..."

    for dir in $IMAGE_DIRS; then
        dirname=$(basename "$dir")
        print_info "Syncing $dirname..."

        rsync -avz \
            "$dir/" \
            "$USER@$SERVER:$REMOTE_IMAGES_PATH/$dirname/"
    done

    print_success "Images deployed"
else
    print_info "No image directories found (skip)"
fi

# Summary
print_section "Deployment Complete!"

echo ""
echo "🎉 Your blog has been deployed!"
echo ""
echo "📊 Deployed:"
echo "   - Blog HTML: $SERVER:$REMOTE_BLOG_PATH/"
echo "   - Images: $SERVER:$REMOTE_IMAGES_PATH/"
echo ""
echo "🌐 Live at: https://rajivshah.com/blog"
echo ""
