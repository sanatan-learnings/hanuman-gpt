# Contributing to Hanuman Chalisa Guide

Thank you for your interest in contributing to this devotional project! 🙏

## How to Contribute

### 1. Find or Suggest an Idea

- Browse [existing issues](https://github.com/arun-gupta/hanuman-chalisa/issues) for contribution ideas
- Suggest new ideas by [creating an issue](https://github.com/arun-gupta/hanuman-chalisa/issues/new)

### 2. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/hanuman-chalisa.git
cd hanuman-chalisa
```

### 3. Make Your Changes

Edit files using any text editor. Common contribution areas:

- **Content:** Improve translations, add context, fix typos
- **Media:** Create images or audio for verses
- **Documentation:** Enhance guides and documentation
- **Features:** Add new functionality (PDF export, search, etc.)

### 4. Test Your Changes

**For content changes:**
- Preview Markdown files in your editor
- Ensure Devanagari script displays correctly
- Verify YAML syntax is correct (no missing colons, proper indentation)

**For code/layout changes - Test Locally (Recommended):**

Testing locally catches build errors before pushing to GitHub:

```bash
# One-time setup: Install dependencies
gem install bundler
bundle install

# Start local Jekyll server
bundle exec jekyll serve

# Visit http://localhost:4000/hanuman-chalisa/
```

**What to test:**
- Navigate through verses - check all links work
- Test language switcher (English ↔ Hindi)
- Verify search functionality
- Check print layout (Cmd/Ctrl+P)
- Test on mobile (resize browser)
- Check browser console for errors (F12)

**Common local build errors:**
- **Liquid syntax error:** Check templates in `_layouts/` for typos
- **YAML parsing error:** Check verse files for proper indentation
- **Missing translation key:** Check `_data/translations/*.yml`
- **Port already in use:** Kill existing Jekyll server or use `--port 4001`

**Local vs GitHub Pages:**
- Local uses latest Jekyll version
- GitHub Pages uses specific versions (see `Gemfile`)
- Always test with `bundle exec jekyll serve` to match GitHub environment
- If local build succeeds but GitHub fails, check Actions log

**Troubleshooting:**
```bash
# Check Jekyll version
bundle exec jekyll --version

# Build without serving (faster error checking)
bundle exec jekyll build

# Verbose output for debugging
bundle exec jekyll serve --verbose

# Clean and rebuild
bundle exec jekyll clean && bundle exec jekyll build
```

### 5. Commit and Push

```bash
git add .
git commit -m "Brief description of your changes"
git push origin main
```

### 6. Create a Pull Request

- Go to your fork on GitHub
- Click "Pull Request"
- Describe your changes
- Submit for review

## Contribution Ideas

Here are some ways you can contribute:

### Content Improvements
- Fix typos or grammatical errors
- Improve word-by-word meanings
- Add or enhance stories behind verses
- Improve practical applications
- Add Ramayana citations where missing

### Translations
- **Complete Hindi translations** - Help translate remaining verses (22/43 completed)
- **Add new languages** - Tamil, Telugu, Spanish, or other languages
- **Translate UI strings** - Add new language file in `_data/translations/`
- Review and improve existing translations
- **Translation format:**
  ```yaml
  literal_translation:
    en: "English text..."
    hi: "हिन्दी अनुवाद..."
    ta: "தமிழ் மொழிபெயர்ப்பு..."
  ```
See [multilingual-implementation.md](docs/multilingual-implementation.md) for translation guide.

### Media Creation
- **Create alternate themed images** - Design images based on different artistic themes (modern, traditional, minimalist, etc.)
- Record human voice recitations
- Create regional language audio versions
- Design verse-specific illustrations

### Documentation
- Translate guides to other languages
- Add pronunciation guides for non-Hindi speakers
- Create video tutorials
- Write blog posts about the project

### Technical Features
- **Create PDF export functionality** - Generate a printable PDF version of all verses
- Implement dark mode
- Add verse bookmarking
- Create mobile app version
- Add social sharing features
- Progressive Web App (PWA) with offline support
- Analytics integration (privacy-friendly)

### Accessibility
- Improve screen reader compatibility
- Add high contrast themes
- Enhance keyboard navigation
- Add audio descriptions

**See the [complete list of contribution ideas](https://github.com/arun-gupta/hanuman-chalisa/issues) in our issues.**

## Guidelines

### Content Quality
- Maintain respectful, devotional tone
- Verify accuracy of Sanskrit/Hindi translations
- Cite sources where applicable
- Keep explanations clear and accessible

### Code Quality
- Keep it simple - no unnecessary complexity
- Follow existing code style
- Comment your code where helpful
- Test before submitting

### File Naming
- Images: `verse_01.jpg`, `doha_01.jpg`
- Audio: `verse_01_full.mp3`, `verse_01_slow.mp3`
- Documents: Use kebab-case (e.g., `my-document.md`)

### Commit Messages
```
Brief description in present tense

- Bullet points for details
- What changed and why
- Keep under 72 characters per line

Co-Authored-By: Your Name <your.email@example.com>
```

## What to Avoid

❌ **Don't:**
- Make large changes without discussing first (create an issue)
- Change the core structure without approval
- Add dependencies without good reason
- Copy content from copyrighted sources
- Make theological claims without citations

✅ **Do:**
- Start small with documentation or content fixes
- Ask questions if unsure
- Be patient with the review process
- Respect the devotional nature of the project

## Getting Help

- **Questions?** [Open a discussion](https://github.com/arun-gupta/hanuman-chalisa/discussions)
- **Bug found?** [Create an issue](https://github.com/arun-gupta/hanuman-chalisa/issues/new)
- **Not sure?** Comment on an existing issue

## Code of Conduct

This is a devotional project. Please:
- Be respectful and kind
- Assume good intentions
- Welcome newcomers
- Keep discussions constructive
- Honor the sacred nature of the content

## Recognition

Contributors will be:
- Listed in commit history
- Mentioned in release notes for significant contributions
- Acknowledged in the project documentation

## Questions?

Feel free to reach out by:
- [Creating an issue](https://github.com/arun-gupta/hanuman-chalisa/issues/new)
- [Starting a discussion](https://github.com/arun-gupta/hanuman-chalisa/discussions)

---

_May your contributions be blessed by Lord Hanuman._ 🙏

**जय श्री राम | जय हनुमान**
