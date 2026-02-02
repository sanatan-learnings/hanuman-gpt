# Documentation

Documentation for the Hanuman GPT website (multi-collection sacred texts).

## Structure

```
docs/
├── guides/                      # Step-by-step how-to guides
│   ├── local-development.md     # Setup and running locally
│   ├── content-generation.md    # Creating verses and media
│   └── cloudflare-worker-setup.md # API proxy deployment
├── reference/                   # Reference material
│   ├── tech-stack.md            # Technical architecture
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
# Install verse-content-sdk (one-time)
pip install verse-content-sdk

# Generate embeddings for all collections
verse-embeddings --multi-collection \
  --collections-file _data/collections.yml \
  --verses-dir _verses \
  --output data/embeddings.json \
  --language en hi

# Generate images for a specific collection/theme
verse-images --collection hanuman-chalisa --theme-name modern-minimalist

# Generate audio (Hanuman Chalisa only currently)
verse-audio --collection hanuman-chalisa
```

### Commands

- `verse-embeddings` - Generate embeddings for semantic search (supports `--multi-collection`)
- `verse-images` - Generate images using DALL-E 3
- `verse-audio` - Generate audio using ElevenLabs
- `verse-deploy` - Deploy Cloudflare Worker

See [verse-content-sdk](https://github.com/sanatan-learnings/verse-content-sdk) for full SDK documentation.

## Guides

- **[Local Development](guides/local-development.md)** - Setup and run locally
- **[Content Generation](guides/content-generation.md)** - Create verses and media
- **[Cloudflare Worker](guides/cloudflare-worker-setup.md)** - Deploy API proxy

## Reference

- **[Tech Stack](reference/tech-stack.md)** - Architecture and YAML structure
- **[Image Prompts](reference/image-prompts.md)** - Scene descriptions
- **[Background](reference/background.md)** - About Hanuman Chalisa
- **[Book Generation](reference/book-generation.md)** - PDF/print books
- **[Spiritual Guidance](reference/spiritual-guidance.md)** - RAG system
- **[Multilingual](reference/multilingual.md)** - Internationalization
- **[Themes](themes/)** - Visual style configurations

## Quick Links

- 🌐 [Live Website](https://sanatan-learnings.github.io/hanuman-gpt/)
- 📦 [verse-content-sdk](https://github.com/sanatan-learnings/verse-content-sdk)
- 🐙 [GitHub Repository](https://github.com/sanatan-learnings/hanuman-gpt)
