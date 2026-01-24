# Technology Stack

This document outlines the technologies, tools, and services used to build and maintain the Hanuman Chalisa interactive website.

## Core Technologies

### Static Site Generation

**Jekyll** (v4.x)
- Ruby-based static site generator
- Built into GitHub Pages
- Converts Markdown → HTML automatically
- Uses Liquid templating language
- **Why:** Zero-config deployment with GitHub Pages, perfect for content-focused sites

**GitHub Pages**
- Free hosting service by GitHub
- Automatic Jekyll builds on every push
- Custom domain support
- HTTPS enabled by default
- **Why:** Free, reliable, and integrated with our git workflow

## Frontend

### HTML/CSS/JavaScript

**Vanilla JavaScript**
- No frameworks needed for our use case
- Arrow key navigation implementation
- Keyboard shortcut handling
- **Why:** Lightweight, fast, no dependencies

**Custom CSS**
- Responsive design
- Mobile-first approach
- Orange/saffron color scheme (devotional theme)
- **Why:** Full control, no bloated CSS frameworks needed

### Fonts & Typography

**System Fonts**
- `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto`
- Native Devanagari script support
- **Why:** Fast loading, native look and feel

## Content Generation

### Images

**Midjourney** (Planned)
- AI image generation service
- Subscription-based: $10-$60/month
- High-quality, artistic outputs
- Perfect for iconographic representations

**Workflow:**
1. Create prompts for each verse theme
2. Generate multiple variations
3. Select best image
4. Export as JPG (800×600px recommended)
5. Place in `/images/` directory
6. Naming: `verse_01.jpg`, `doha_01.jpg`, etc.

**Alternative Options:**
- DALL-E 3 (OpenAI)
- Stable Diffusion (open source, self-hosted)
- Traditional artwork (scan and digitize)
- Stock photo services (iStock, Shutterstock)

### Audio Recitations

**ElevenLabs** (Planned)
- AI voice synthesis and cloning
- Multilingual support including Hindi
- Natural-sounding voice generation
- Subscription: $5-$330/month depending on usage

**Workflow:**
1. Input Hindi verse text
2. Select or clone appropriate voice (devotional tone)
3. Generate full-speed version
4. Generate slow-speed version (adjust rate/pace)
5. Export as MP3 (128kbps minimum)
6. Place in `/audio/` directory
7. Naming: `verse_01_full.mp3`, `verse_01_slow.mp3`, etc.

**Alternative Options:**
- Google Cloud Text-to-Speech (API-based, Hindi support)
- Amazon Polly (AWS, limited Hindi voices)
- Azure Cognitive Services Speech (Microsoft)
- Human voice recording (most authentic but time-intensive)
- Festival TTS (open source, limited quality)

### Content Creation

**Markdown**
- All verse content written in Markdown
- Easy to read, write, and version control
- **Why:** Simple, portable, git-friendly

**AI Assistance**
- Claude (Anthropic) for content structuring
- **Used for:** Template creation, content organization, Jekyll setup

## Version Control & Deployment

### Git & GitHub

**Git**
- Version control for all content and code
- Full history of changes
- Branch-based workflow

**GitHub**
- Remote repository hosting
- Collaboration platform
- Automatic Jekyll builds
- Issue tracking for content improvements

### Deployment Pipeline

```
Local Changes → Git Commit → Git Push → GitHub Pages Build → Live Site
```

**Build Time:** 1-2 minutes after push

## Development Tools

### Code Editors

Any Markdown-compatible editor:
- VS Code (recommended)
- Sublime Text
- Atom
- JetBrains IDEs (IntelliJ, WebStorm)

### Local Testing (Optional)

**Jekyll Local Server**
```bash
bundle install
jekyll serve
```
- Preview changes before pushing
- Hot reload during development
- Runs on `http://localhost:4000`

**Note:** Local testing is optional - you can edit and push directly to GitHub

## Content Management

### File Structure

```
Content (Markdown) → Jekyll Processing → Static HTML
```

**Markdown Files:** `/verses/*.md`
- 43 verse files with front matter
- Template-based structure
- Easy to edit in any text editor

**Static Assets:**
- Images: `/images/` (43 JPG files)
- Audio: `/audio/` (86 MP3 files)
- CSS: `/assets/css/style.css`
- JS: `/assets/js/navigation.js`

## Browser Support

### Target Browsers

- Chrome/Edge (Chromium) - Latest 2 versions
- Firefox - Latest 2 versions
- Safari - Latest 2 versions
- Mobile browsers (iOS Safari, Chrome Mobile)

### Features Used

- CSS Grid & Flexbox (widely supported)
- Arrow key events (universal support)
- HTML5 Audio API (universal support)
- Responsive images (universal support)

**No polyfills needed** - all features well-supported

## Analytics (Optional)

Currently not implemented, but can add:
- Google Analytics
- Plausible Analytics (privacy-focused)
- Simple analytics pixel

**Privacy consideration:** Keep it minimal for a devotional site

## Performance

### Current Optimizations

- Static HTML (no server processing)
- System fonts (no font downloads)
- Lazy loading for images
- Minified CSS (can be added)
- CDN via GitHub Pages

### Metrics

- **Load Time:** < 1 second (text only)
- **Full Load:** 2-3 seconds (with images)
- **Audio:** Loaded on demand
- **Lighthouse Score:** Target 90+ (all categories)

## Accessibility

### Standards

- Semantic HTML5
- Keyboard navigation (arrow keys)
- Screen reader compatible
- High contrast text
- Responsive design (mobile accessible)

### WCAG Compliance

Target: WCAG 2.1 Level AA
- Keyboard navigation ✓
- Color contrast ✓
- Responsive design ✓
- Semantic markup ✓

## Security

### Built-in Security

- **Static Site:** No database, no server-side code
- **HTTPS:** Enforced by GitHub Pages
- **No User Input:** Read-only content
- **No Cookies:** No tracking

**Attack Surface:** Minimal - just static content delivery

## Cost Breakdown

### Hosting & Infrastructure
- GitHub Pages: **Free**
- Domain (optional): $10-15/year

### Content Generation
- Midjourney: $10-60/month (one-time generation)
- ElevenLabs: $5-330/month (based on usage)

### Total Estimated Cost
- **Initial Setup:** $50-200 (one-time for all images and audio)
- **Ongoing:** $0/month (just hosting)
- **Optional Domain:** $10-15/year

## Future Enhancements

Potential additions:

### Features
- Search functionality
- Verse bookmarking
- Print-friendly version
- Dark mode toggle
- Language selection (English/Hindi)

### Content
- Video recitations
- Translation in multiple languages
- Interactive quizzes
- Commentary from scholars

### Technical
- Progressive Web App (PWA)
- Offline support
- Social sharing
- RSS feed for updates

## Resources & Documentation

### Official Documentation
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages Docs](https://docs.github.com/en/pages)
- [Markdown Guide](https://www.markdownguide.org/)
- [Midjourney Documentation](https://docs.midjourney.com/)
- [ElevenLabs Documentation](https://docs.elevenlabs.io/)

### Internal Documentation
- [github-pages-setup.md](github-pages-setup.md) - Setup and deployment guide
- [verse-structure.md](verse-structure.md) - Verse content structure
- [background.md](background.md) - Hanuman Chalisa background
- [guide.md](guide.md) - Usage and recitation guide

## Contributing

### Content Updates
1. Edit Markdown files in `/verses/`
2. Commit changes
3. Push to GitHub
4. Site updates automatically

### Technical Changes
1. Edit files in `/_layouts/`, `/assets/`
2. Test locally (optional)
3. Commit and push
4. Verify on live site

### Media Assets
1. Generate images (Midjourney) or audio (ElevenLabs)
2. Add to `/images/` or `/audio/` directories
3. Follow naming conventions
4. Commit and push

## Contact & Support

For technical issues:
- [GitHub Issues](https://github.com/arun-gupta/hanuman-chalisa/issues)

For content suggestions:
- Open an issue or submit a pull request

---

**Last Updated:** January 2026
**Tech Stack Version:** 1.0
