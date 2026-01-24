# GitHub Pages Setup

This document explains how the Hanuman Chalisa website is structured and how GitHub Pages generates the live site from this repository.

## Live Website

**🌐 View the live site:** [https://arun-gupta.github.io/hanuman-chalisa/](https://arun-gupta.github.io/hanuman-chalisa/)

## How It Works

This repository uses **Jekyll** (a static site generator) with **GitHub Pages** to automatically convert markdown files into a beautiful, navigable website.

### The Magic of Jekyll + GitHub Pages

1. **You write in Markdown** - The verse files in `/verses/` are plain markdown
2. **Push to GitHub** - When you commit and push changes
3. **GitHub builds automatically** - Jekyll runs on GitHub's servers
4. **Site is live** - Changes appear at the URL above within 1-2 minutes

No manual HTML generation needed! GitHub does it all automatically.

## Directory Structure

```
hanuman-chalisa/
├── _config.yml              # Jekyll configuration
│
├── _layouts/                # HTML templates
│   ├── default.html        # Base template (header, footer)
│   └── verse.html          # Template for verse pages
│
├── assets/                  # Static assets
│   ├── css/
│   │   └── style.css       # All styling
│   └── js/
│       └── navigation.js   # Arrow key navigation
│
├── verses/                  # Verse content (markdown)
│   ├── doha_01.md          # Opening doha 1
│   ├── doha_02.md          # Opening doha 2
│   ├── verse_01.md         # Verse 1
│   ├── verse_02.md         # Verse 2
│   ├── ...                 # Verses 3-40
│   └── doha_closing.md     # Closing doha
│
├── images/                  # Verse images
│   ├── doha_01.jpg
│   ├── verse_01.jpg
│   └── ...                 # One image per verse
│
├── audio/                   # Audio recitations
│   ├── doha_01_full.mp3
│   ├── doha_01_slow.mp3
│   └── ...                 # 2 audio files per verse
│
├── docs/                    # Documentation
│   ├── background.md
│   ├── guide.md
│   └── github-pages-setup.md (this file)
│
├── index.html              # Home page
└── README.md               # Repository documentation
```

## Jekyll Front Matter

Each verse markdown file includes "front matter" at the top:

```yaml
---
layout: verse
title: "Verse 1: Ocean of Knowledge and Virtues"
previous_verse: "/verses/doha_02"
next_verse: "/verses/verse_02"
---
```

This tells Jekyll:
- Which layout template to use
- The page title
- Navigation links for arrow key navigation

## Key Features

### 1. Arrow Key Navigation
- **Left Arrow (←)** - Previous verse
- **Right Arrow (→)** - Next verse
- **H or Home** - Return to verse list
- Works seamlessly across all 43 verses

### 2. Responsive Design
- Mobile-friendly layout
- Adapts to all screen sizes
- Touch-friendly navigation buttons

### 3. Audio Integration
- Full speed recitation for each verse
- Slow speed for learning pronunciation
- Direct playback in browser

### 4. Visual Content
- One image per verse
- Supports iconographic depictions
- Responsive image sizing

## How to Update Content

### Adding or Editing Verses

1. Edit the markdown file in `/verses/`
2. Keep the front matter intact
3. Commit and push to GitHub
4. Site updates automatically in 1-2 minutes

### Adding Images

1. Place image in `/images/` with correct filename
   - Example: `verse_01.jpg` for Verse 1
2. Commit and push
3. Image appears automatically on the verse page

### Adding Audio

1. Place audio files in `/audio/` with correct filenames
   - Example: `verse_01_full.mp3` and `verse_01_slow.mp3`
2. Commit and push
3. Audio players appear automatically

### Updating Styles

1. Edit `/assets/css/style.css`
2. Commit and push
3. New styles apply site-wide

## Enabling GitHub Pages

If GitHub Pages is not yet enabled:

1. Go to repository Settings
2. Navigate to "Pages" in the left sidebar
3. Under "Source", select:
   - Branch: `main`
   - Folder: `/ (root)`
4. Click "Save"
5. Wait 1-2 minutes for the first build
6. Site will be live at: `https://arun-gupta.github.io/hanuman-chalisa/`

## Local Development (Optional)

To preview the site locally before pushing:

### Install Jekyll

```bash
# On macOS
brew install ruby
gem install jekyll bundler

# On Linux
sudo apt-get install ruby-full build-essential
gem install jekyll bundler
```

### Run Local Server

```bash
cd hanuman-chalisa
jekyll serve
```

Then visit: `http://localhost:4000/hanuman-chalisa/`

**Note:** Local development is optional. You can edit and push directly to GitHub and let it build for you.

## File Requirements

### Images (43 files needed)
- Format: JPG or PNG
- Recommended size: 800×600px
- Naming: `doha_01.jpg`, `verse_01.jpg`, etc.

### Audio (86 files needed)
- Format: MP3
- Quality: 128kbps minimum
- Two files per verse: `*_full.mp3` and `*_slow.mp3`

### Verses (43 files - already created ✓)
- Format: Markdown (.md)
- Must include front matter
- Content follows template structure

## Troubleshooting

### Site not updating?
- Wait 2-3 minutes after push
- Check repository "Actions" tab for build status
- Look for any error messages

### 404 errors?
- Verify GitHub Pages is enabled
- Check that `_config.yml` has correct `baseurl`
- Ensure file paths match exactly

### Styling issues?
- Clear browser cache
- Check CSS file is committed
- Verify no syntax errors in CSS

## Technology Stack

- **Jekyll** - Static site generator (Ruby-based)
- **Liquid** - Template language
- **Markdown** - Content format
- **GitHub Pages** - Free hosting
- **HTML/CSS/JavaScript** - Frontend

## Benefits of This Approach

✅ **No manual HTML** - Write in simple Markdown
✅ **Automatic deployment** - Push and it's live
✅ **Version controlled** - Full history of changes
✅ **Free hosting** - GitHub Pages is free
✅ **Fast and secure** - Static site = no server vulnerabilities
✅ **Easy maintenance** - Update markdown files, not HTML

## Questions or Issues?

See [GitHub Pages Documentation](https://docs.github.com/en/pages) or [Jekyll Documentation](https://jekyllrb.com/docs/) for more details.
