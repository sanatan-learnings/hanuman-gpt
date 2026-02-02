---
layout: default
title: "Developer Guide"
---

# Developer Guide

Technical documentation for developers contributing to the Hanuman Chalisa project.

## Quick Start

```bash
# Clone the repository
git clone https://github.com/sanatan-learnings/hanuman-gpt.git
cd hanuman-chalisa

# Install dependencies
gem install bundler
bundle install

# Start local server
bundle exec jekyll serve

# Visit http://localhost:4000/hanuman-gpt/
```

## Project Structure

```
hanuman-chalisa/
├── _data/                    # Site data files
│   ├── translations/         # Language files (en.yml, hi.yml)
│   └── themes.yml            # Image theme definitions
├── _layouts/                 # Page templates
│   ├── default.html          # Main site layout
│   └── verse.html            # Individual verse layout
├── _verses/                  # 43 verse markdown files
│   ├── doha_01.md
│   ├── verse_01.md
│   └── doha_closing.md
├── assets/                   # Static assets
│   ├── css/                  # Stylesheets
│   ├── js/                   # JavaScript files
│   └── images/               # Static images
├── audio/                    # AI-generated audio files
│   ├── doha_01_full.mp3      # Full speed recitations
│   └── doha_01_slow.mp3      # Slow speed (75%) for learning
├── docs/                     # Documentation
├── images/                   # AI-generated verse images
│   └── modern-minimalist/    # Default theme (47 images)
├── scripts/                  # Legacy scripts (use verse-content-sdk instead)
│   └── legacy/               # Old bash/python scripts (deprecated)
├── book.html                 # Book generator page
├── index.html                # Home page
├── full-chalisa.html         # Complete chalisa view
└── search.html               # Search page
```

## Local Development

### Prerequisites

- Ruby 3.0+ (check: `ruby --version`)
- Bundler (`gem install bundler`)
- Git

### Setup

```bash
# Install dependencies
bundle install

# Start development server
bundle exec jekyll serve

# Build only (no server)
bundle exec jekyll build

# Clean build artifacts
bundle exec jekyll clean
```

### Development Workflow

1. **Make changes** to files
2. **Jekyll auto-rebuilds** (watch mode)
3. **Refresh browser** to see changes
4. **Check console** for errors (F12)

### Common Issues

**Port already in use:**
```bash
bundle exec jekyll serve --port 4001
```

**YAML syntax error:**
- Check verse files for proper indentation
- Ensure colons are followed by spaces
- Use YAML linter online

**Liquid syntax error:**
- Check templates in `_layouts/` and `_includes/`
- Ensure all {% raw %}`{% %}`{% endraw %} tags are properly closed

**Build succeeds locally but fails on GitHub:**
- Check `.github/workflows/` for CI configuration
- Verify GitHub Pages compatible plugins

## Content Generation with verse-content-sdk

All multimedia content is generated using the [verse-content-sdk](https://github.com/sanatan-learnings/verse-content-sdk):

- **verse-images** - Generate AI images with DALL-E 3
- **verse-audio** - Generate audio pronunciations with ElevenLabs
- **verse-embeddings** - Generate vector embeddings
- **verse-deploy** - Deploy Cloudflare Workers

Install once: `python3 -m venv venv && source venv/bin/activate && pip install verse-content-sdk`

See [scripts/README.md](../scripts/README.md) for complete documentation.

## Generate Custom Image Themes

Create new artistic themes using DALL-E 3.

### Quick Start

```bash
# Create and activate virtual environment (one-time setup)
python3 -m venv venv
source venv/bin/activate

# Install SDK
pip install verse-content-sdk

# Get API key from https://platform.openai.com/api-keys
export OPENAI_API_KEY='your-key-here'

# Generate all 47 images
verse-images traditional-art --style "traditional Indian devotional art"

# See all options
verse-images --help
```

### Configuration Options

```bash
# Quality (standard or hd)
verse-images my-theme --quality hd

# Size (1024x1024 or 1024x1792)
verse-images my-theme --size 1024x1792

# Resume from specific image
verse-images my-theme --resume verse-15.png
```

### Cost Estimate

- **Standard quality**: ~$2 for 47 images ($0.040 per image)
- **HD quality**: ~$4 for 47 images ($0.080 per image)

### Adding Your Theme

After generating images:

1. **Update themes file:**
```yaml
# _data/themes.yml
traditional-art:
  name_en: "Traditional Art"
  name_hi: "पारंपरिक कला"
  path: "images/traditional-art"
```

2. **Test locally:**
```bash
bundle exec jekyll serve
# Check theme switcher in header
```

3. **Commit and push:**
```bash
git add images/traditional-art _data/themes.yml
git commit -m "Add traditional art theme"
git push
```

See [scripts/README.md](../scripts/README.md) for detailed instructions.

## Generate Audio Files

Create audio pronunciations for all verses using Eleven Labs text-to-speech.

### Quick Start

```bash
# Create and activate virtual environment (one-time setup)
python3 -m venv venv
source venv/bin/activate

# Install SDK
pip install verse-content-sdk

# Get API key from https://elevenlabs.io/app/settings/api-keys
export ELEVENLABS_API_KEY='your-key-here'

# Generate all 86 audio files (43 verses × 2 speeds)
verse-audio

# See all options
verse-audio --help
```

### Configuration Options

```bash
# Generate single file for testing
verse-audio --only doha_01_full.mp3

# Regenerate specific files
verse-audio --regenerate verse_10_full.mp3,verse_10_slow.mp3

# Force regenerate ALL files
verse-audio --force

# Resume from specific file
verse-audio --resume verse_15_full.mp3

# Use different voice
verse-audio --voice-id YOUR_VOICE_ID
```

### Cost Estimate

- **Total cost**: ~$0.02 for 86 audio files
- **Eleven Labs Free Tier**: 10,000 characters/month (sufficient for one-time generation)
- **Model**: eleven_multilingual_v2 (supports Hindi/Sanskrit)

### Audio Specifications

- **Format**: MP3 (128kbps+)
- **Full speed**: Natural recitation pace via Eleven Labs
- **Slow speed**: 75% speed via ffmpeg atempo filter (25% slower)
- **Total files**: 86 (43 verses × 2 speeds)

### Requirements

- Python 3.8+
- Eleven Labs API key
- ffmpeg (for slow speed processing)
  - macOS: `brew install ffmpeg`
  - Linux: `sudo apt-get install ffmpeg`

See [audio/README.md](../audio/README.md) for detailed instructions.

## Tech Stack

### Core Technologies

- **Jekyll 3.9.3** - Static site generator
- **Liquid** - Template language
- **YAML** - Data files and frontmatter
- **Markdown** - Content files
- **GitHub Pages** - Hosting

### Frontend

- **HTML5** - Semantic markup
- **CSS3** - Styling with Flexbox/Grid
- **Vanilla JavaScript** - No frameworks
- **Print CSS** - Optimized for PDF generation

### Development Tools

- **Python 3.8+** - Content generation SDK
- **verse-content-sdk** - Content generation toolkit (images, audio, embeddings)
- **OpenAI API** - DALL-E 3 integration for images
- **Eleven Labs API** - Text-to-speech for audio
- **ffmpeg** - Audio post-processing (speed control)
- **Ruby/Bundler** - Dependency management
- **Git** - Version control

### Key Libraries

- `jekyll-seo-tag` - SEO optimization
- `jekyll-sitemap` - Sitemap generation
- `verse-content-sdk` - Content generation SDK (includes openai, elevenlabs, requests, pillow)

## File Formats

### Verse Files (`_verses/*.md`)

```yaml
---
layout: verse
verse_number: 1
title_en: "Ocean of Knowledge and Virtues"
title_hi: "ज्ञान और गुणों का सागर"
image: /images/modern-minimalist/verse-01.png
---

devanagari: |
  श्रीगुरु चरन सरोज रज, निजमन मुकुरु सुधारि।
  बरनउं रघुबर बिमल जसु, जो दायकु फल चारि॥

transliteration: |
  Shri guru charan saroja raj, nija mana mukuru sudhari
  Baranau raghubara bimala jasu, jo dayaku phala chari

# ... more fields
```

### Translation Files (`_data/translations/*.yml`)

```yaml
language_name: "English"
language_code: "en"

home:
  title: "Hanuman Chalisa: A Comprehensive Guide"
  subtitle: "ॐ Shri Hanumate Namah"

sections:
  devanagari: "1. Original Hindi Text"
  # ... more sections
```

## Testing

### Manual Testing Checklist

- [ ] All verse pages load correctly
- [ ] Language switcher works (EN ↔ HI)
- [ ] Theme switcher changes images
- [ ] Search functionality works
- [ ] Arrow key navigation (← →)
- [ ] Print layout looks correct
- [ ] Book generator produces proper output
- [ ] Mobile responsive (test on small screens)
- [ ] No console errors

### Browser Testing

Test on:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Android)

### Print Testing

```bash
# Test print layout
1. Open any verse page
2. Press Cmd/Ctrl+P
3. Check print preview
4. Verify images and layout
```

## Deployment

The site auto-deploys via GitHub Pages when pushing to `main` branch.

### GitHub Pages Build

1. Push to `main` branch
2. GitHub Actions runs Jekyll build
3. Site deploys to `https://sanatan-learnings.github.io/hanuman-gpt/`
4. Check Actions tab for build status

### Pre-commit Validation

A pre-commit hook validates:
- YAML syntax in verse files
- Jekyll build success
- Liquid syntax issues

See `.git/hooks/pre-commit` for details.

## Performance Optimization

### Image Optimization

All images should be:
- **Dimensions**: 1024 × 1536 pixels (2:3 ratio)
- **Format**: PNG with compression
- **Size**: Under 500KB per image

### Lazy Loading

```html
<img src="..." loading="lazy" alt="...">
```

### Caching Strategy

- Static assets cached by GitHub Pages CDN
- `data/search.json` regenerated on each build
- Images served with long cache headers

## API Integration

### DALL-E 3 Configuration

The verse-content-sdk handles all API configuration. Default settings:

```python
# verse_content_sdk/images/generator.py
DALLE_MODEL = "dall-e-3"
IMAGE_SIZE = "1024x1792"  # Portrait, crop to 1024x1536
IMAGE_QUALITY = "standard"  # or "hd"
IMAGE_STYLE = "natural"  # or "vivid"
```

Override via command-line options:
```bash
verse-images my-theme --quality hd --size 1024x1792 --style vivid
```

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for:
- How to contribute
- Contribution guidelines
- Code of conduct

## Troubleshooting

### Build Fails on GitHub but Works Locally

- Check GitHub Actions logs
- Verify `Gemfile.lock` is committed
- Ensure no local-only dependencies

### Images Not Loading

- Check image paths are relative
- Verify {% raw %}`{{ site.baseurl }}`{% endraw %} is used
- Check browser console for 404s

### Language Switching Not Working

- Check `language.js` is loaded
- Verify `data-lang` attributes exist
- Check localStorage is enabled

## Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Liquid Template Language](https://shopify.github.io/liquid/)
- [GitHub Pages Docs](https://docs.github.com/en/pages)
- [DALL-E 3 API](https://platform.openai.com/docs/guides/images)

## Getting Help

- **Questions**: [GitHub Discussions](https://github.com/sanatan-learnings/hanuman-gpt/discussions)
- **Bugs**: [GitHub Issues](https://github.com/sanatan-learnings/hanuman-gpt/issues)
- **Technical Docs**: See `docs/` directory

---

**Happy coding! 🙏**
