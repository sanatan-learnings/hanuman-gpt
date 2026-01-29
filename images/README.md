# Images Directory

This directory contains themed visual representations for each verse of the Hanuman Chalisa, organized by theme.

## Theme-Based Organization

Images are organized in subdirectories by theme:

```
images/
├── modern-minimalist/    # Contemporary spiritual aesthetic (47 images)
├── kids-friendly/        # Child-friendly storybook style (generate with script)
└── [your-theme]/         # Add custom themes here
```

## File Naming Convention

Each theme directory contains 47 images:

- **Title page**: `title-page.png`
- **Opening dohas**: `opening-doha-01.png`, `opening-doha-02.png`
- **Main verses**: `verse-01.png` through `verse-40.png`
- **Closing doha**: `closing-doha.png`

**Total**: 47 images per theme

## Image Specifications

- **Format**: PNG
- **Resolution**: 1024 × 1536 pixels (portrait, 2:3 aspect ratio)
- **Quality**: Standard or HD (DALL-E 3)
- **Content**: Scene-based depictions following docs/image-prompts.md with theme-specific visual styling

## Generating New Theme Images

Use the automated image generation script to create images for any theme:

### Quick Start

```bash
# 1. Ensure your OpenAI API key is in .env file
cp .env.example .env
# Edit .env and add: OPENAI_API_KEY=sk-your-key-here

# 2. Generate images for a theme
./scripts/generate_images.sh kids-friendly
```

### How It Works

The script combines:
- **Scene descriptions** from `docs/image-prompts.md` (what happens in each verse)
- **Visual style** from `docs/themes/<theme-name>.yml` (colors, character design, mood)

Both are combined to create complete DALL-E 3 prompts, generating all 47 images automatically.

### Options

```bash
# Generate with HD quality (2x cost)
./scripts/generate_images.sh kids-friendly --quality hd

# Resume from a specific image (if interrupted)
./scripts/generate_images.sh kids-friendly --resume verse-15.png

# Custom style override
./scripts/generate_images.sh my-theme --style "watercolor painting style"
```

### Cost Estimate

- **Standard quality**: $0.040/image × 47 = **$1.88 per theme**
- **HD quality**: $0.080/image × 47 = **$3.76 per theme**

### Creating a New Theme

1. **Create theme specification**: Copy and customize `docs/themes/modern-minimalist.yml` or `docs/themes/kids-friendly.yml`
2. **Define visual style**: Specify colors, character designs, mood, composition
3. **Generate images**: Run `./scripts/generate_images.sh your-theme-name`
4. **Update site config**: Add theme to `_data/themes.yml`
5. **Test locally**: `bundle exec jekyll serve`

See [docs/developer-guide.md](../docs/developer-guide.md) for detailed instructions.

## Available Themes

### Modern Minimalist
- **Style**: Contemporary spiritual aesthetic with luminous saffron-gold tones
- **Audience**: Adults, modern devotional platforms
- **Status**: ✅ Complete (47 images)

### Kids Friendly
- **Style**: Bright cartoon storybook illustrations
- **Audience**: Children ages 5-12
- **Status**: ⚪ Generate using script

## Technical Details

### Image Pipeline

```
docs/image-prompts.md           docs/themes/theme-name.yml
(Scene descriptions)      +     (Visual style specs)
                          ↓
             scripts/generate_images.sh
                          ↓
             OpenAI DALL-E 3 API
                          ↓
        images/theme-name/*.png (47 files)
```

### Directory Structure

Each theme creates its own directory with all 47 images:

```
images/theme-name/
├── title-page.png
├── opening-doha-01.png
├── opening-doha-02.png
├── verse-01.png
├── verse-02.png
...
├── verse-40.png
└── closing-doha.png
```

## Resources

- **Scene descriptions**: [docs/image-prompts.md](../docs/image-prompts.md)
- **Theme specs**: [docs/themes/](../docs/themes/)
- **Generation script**: [scripts/generate_images.sh](../scripts/generate_images.sh)
- **Developer guide**: [docs/developer-guide.md](../docs/developer-guide.md)
