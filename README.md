# Hanuman GPT: AI Spiritual Guide

🚩 **Jai Hanuman 🏹 Jai Shri Ram**

**🌐 [View the live interactive website →](https://sanatan-learnings.github.io/hanuman-gpt/)**

_May Lord Hanuman's blessings be with all who study and recite these sacred verses._

---

## About

A detailed, verse-by-verse exploration of sacred Hindu texts related to Lord Hanuman. Currently features:
- **Hanuman Chalisa** - 40 verses (chaupais) by Goswami Tulsidas glorifying Lord Hanuman
- **Sundar Kaand** - Selected verses from Ramcharitmanas describing Hanuman's journey to Lanka

This guide provides deep understanding of each verse with translations, meanings, stories from the Ramayana, and practical applications for modern life - all available in **English** and **हिन्दी (Hindi)**.

## Features

### 📖 Read & Study
- **Multiple collections** - Hanuman Chalisa (43 verses) + Sundar Kaand (3 verses)
- **Original Devanagari text** and transliteration
- **Word-by-word meanings** and literal translations
- **Interpretive meanings** explaining spiritual depth
- **Stories from Ramayana** providing context
- **Search functionality** across all collections
- **Bilingual support** - Switch between English and Hindi instantly
- **Beautiful AI-generated images** for each verse

### 🎵 Audio Pronunciation (Hanuman Chalisa)
- **86 audio files** - Every Chalisa verse in two speeds (full and slow)
- **Full speed** - Natural recitation pace for experienced practitioners
- **Slow speed** - 25% slower for learning pronunciation
- **AI-generated** - Clear, natural Hindi/Sanskrit pronunciation via Eleven Labs
- **Embedded players** - Listen directly on each verse page
- Perfect for learning correct pronunciation and recitation practice

### 💬 Spiritual Guidance (AI-Powered)
- **Ask questions** and receive spiritual guidance based on relevant verses
- **Multi-collection RAG system** - Searches across all collections
- **GPT-4 powered** - Thoughtful, context-aware responses
- **Bilingual** - Works in English and Hindi
- **Conversation history** - Maintains context for follow-up questions
- Requires your OpenAI API key (~$0.01 per query)

[Try Spiritual Guidance →](https://sanatan-learnings.github.io/hanuman-gpt/guidance)

### 📕 Generate Custom Books
Create personalized printable books:
- **Multiple collections**: Choose from available collections
- **Multiple sizes**: 6"×4" pocket, 8"×6" medium, A5, A4
- **Customizable content**: Choose what to include
- **Custom headers/footers**: Personalize with your own text
- **Print or PDF**: Ready for home or professional printing

[Visit Book Generator →](https://sanatan-learnings.github.io/hanuman-gpt/chalisa/book)

### 🎨 Multiple Themes
- Switch between different artistic styles
- Current: Modern Minimalist theme
- Generate your own themes using DALL-E 3 (see below)

## For Developers

Want to contribute or generate custom themes?

**→ See the [Developer Guide](docs/developer-guide.md)** for:
- Local development setup
- Generating custom image themes with DALL-E 3 (~$2 for 47 images)
- Generating audio files with Eleven Labs (~$0.02 for 86 files)
- **Regenerating embeddings** for the RAG system (FREE, runs locally)
- Project structure and architecture
- Testing and deployment

**→ See [CONTRIBUTING.md](CONTRIBUTING.md)** for contribution guidelines

### Regenerating Embeddings

The spiritual guidance feature uses pre-computed embeddings. To regenerate them (e.g., when adding new collections or translations):

```bash
# Install verse-content-sdk (first time only)
pip install verse-content-sdk

# Generate embeddings for all enabled collections
verse-embeddings --multi-collection \
  --collections-file _data/collections.yml \
  --verses-dir _verses \
  --output data/embeddings.json \
  --language en hi

# Output: data/embeddings.json (~4.6MB with all collections)
```

**Cost:** Requires OpenAI API key (~$0.01 per collection)

## Documentation

**User Guides:**
- [User Guide](docs/user-guide.md) - How to use the website
- [Background](docs/background.md) - History of the Hanuman Chalisa
- [Book Generation](docs/book-generation.md) - Create printable books

**Technical Docs:**
- [Developer Guide](docs/developer-guide.md) - Setup, architecture, and development
- [Verse Structure](docs/verse-structure.md) - How verses are organized
- [Tech Stack](docs/tech-stack.md) - Technologies used
- [Adding Themes](docs/adding-themes.md) - Create new image themes
- [Image Prompts](docs/image-prompts.md) - DALL-E 3 prompts used

## Contributing

We welcome contributions! Whether it's:
- Translation improvements
- Additional languages (Tamil, Telugu, Spanish planned)
- New image themes
- Bug fixes or features

See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

**Upcoming Features:** Check [GitHub Issues](https://github.com/sanatan-learnings/hanuman-gpt/issues)

## Acknowledgments

### Content Creation
- **DALL-E 3** (OpenAI) - AI-generated verse images
- **Eleven Labs** - AI text-to-speech for audio recitations (eleven_multilingual_v2)
- **ffmpeg** - Audio post-processing for speed control
- **GPT-4** (OpenAI) - Spiritual guidance generation
- **sentence-transformers** (Hugging Face) - Local embeddings for semantic search
- **Claude Code** (Anthropic) - AI-assisted content generation and development
- **Human review** - All content validated for accuracy and devotional authenticity

### Traditional Sources
Content draws upon:
- Valmiki Ramayana
- Tulsidas's Shri Ramcharitmanas
- Traditional commentaries by various acharyas
- Living oral traditions of Hanuman Chalisa recitation

### Technology
Built with Jekyll and GitHub Pages. Hosted on GitHub.

## License

Created for educational, devotional, and non-commercial purposes.
May it serve the spiritual upliftment of all beings.

---

🚩 **Jai Hanuman 🏹 Jai Shri Ram**

