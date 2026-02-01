# Documentation

Documentation for the Hanuman Chalisa website.

## Structure

```
docs/
├── guides/                      # Step-by-step how-to guides
│   ├── local-development.md     # Setup and running locally
│   ├── content-generation.md    # Creating verses and media
│   ├── cloudflare-worker-setup.md # API proxy deployment
│   └── user-guide.md            # Using the website
├── reference/                   # Reference material
│   ├── tech-stack.md            # Technical architecture
│   ├── verse-structure.md       # YAML data format
│   ├── image-prompts.md         # Scene descriptions
│   ├── background.md            # About Hanuman Chalisa
│   ├── book-generation.md       # PDF/print book generation
│   ├── spiritual-guidance.md    # RAG system
│   └── multilingual.md          # Internationalization
└── themes/                      # Image theme configurations
```

## Quick Start

### Generate Content

```bash
# Generate images for a theme
verse-images --theme-name modern-minimalist

# Generate audio recitations
verse-audio

# Generate embeddings for search
verse-embeddings
```

### Commands

- `verse-images` - Generate images using DALL-E 3
- `verse-audio` - Generate audio using ElevenLabs
- `verse-embeddings` - Generate embeddings for semantic search
- `verse-deploy` - Deploy Cloudflare Worker

See [verse-content-sdk](https://github.com/sanatan-learnings/verse-content-sdk) for full SDK documentation.

## Guides

- **[Local Development](guides/local-development.md)** - Setup and run locally
- **[Content Generation](guides/content-generation.md)** - Create verses and media
- **[Cloudflare Worker](guides/cloudflare-worker-setup.md)** - Deploy API proxy
- **[User Guide](guides/user-guide.md)** - Using the website

## Reference

- **[Tech Stack](reference/tech-stack.md)** - Architecture overview
- **[Verse Structure](reference/verse-structure.md)** - YAML data format
- **[Image Prompts](reference/image-prompts.md)** - Scene descriptions
- **[Background](reference/background.md)** - About Hanuman Chalisa
- **[Book Generation](reference/book-generation.md)** - PDF/print books
- **[Spiritual Guidance](reference/spiritual-guidance.md)** - RAG system
- **[Multilingual](reference/multilingual.md)** - Internationalization
- **[Themes](themes/)** - Visual style configurations

## Quick Links

- 🌐 [Live Website](https://sanatan-learnings.github.io/hanuman-chalisa/)
- 📦 [verse-content-sdk](https://github.com/sanatan-learnings/verse-content-sdk)
- 🐙 [GitHub Repository](https://github.com/sanatan-learnings/hanuman-chalisa)
