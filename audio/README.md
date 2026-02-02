# Audio Directory

This directory contains audio pronunciations for verses across multiple sacred text collections, generated using Eleven Labs text-to-speech.

## Multi-Collection Organization

Audio files are organized by collection:

```
audio/
├── hanuman-chalisa/         # Hanuman Chalisa audio (86 files)
│   ├── doha_01_full.mp3
│   ├── doha_01_slow.mp3
│   ├── verse_01_full.mp3
│   ├── verse_01_slow.mp3
│   └── ...
├── sundar-kaand/            # Sundar Kaand audio (520+ files when complete)
│   ├── chaupai_01_full.mp3
│   ├── chaupai_01_slow.mp3
│   └── ...
└── bajrang-baan/            # Bajrang Baan audio (future)
    └── ...
```

## Generating Audio Files

### For Hanuman Chalisa

Use the automated generation script:

```bash
# Generate all 86 audio files for Hanuman Chalisa
./scripts/generate_audio.sh

# Resume from specific file
./scripts/generate_audio.sh --resume verse_15_full.mp3

# Use different voice
./scripts/generate_audio.sh --voice-id YOUR_VOICE_ID
```

### For Sundar Kaand (Future)

Will need collection-specific generation script:

```bash
# TODO: Create generate_sundar_kaand_audio.sh
./scripts/generate_sundar_kaand_audio.sh
```

**Requirements:**
- Eleven Labs API key in `.env` file: `ELEVENLABS_API_KEY=your-key-here`
- Get API key from: https://elevenlabs.io/app/settings/api-keys
- `ffmpeg` installed (for slow speed processing)
  - macOS: `brew install ffmpeg`
  - Linux: `sudo apt-get install ffmpeg`

## File Naming Conventions

### Hanuman Chalisa (44 verses × 2 speeds = 88 files)

**Opening Dohas:**
- `doha_01_full.mp3` / `doha_01_slow.mp3`
- `doha_02_full.mp3` / `doha_02_slow.mp3`

**Main Verses (1-40):**
- `verse_01_full.mp3` / `verse_01_slow.mp3`
- `verse_02_full.mp3` / `verse_02_slow.mp3`
- ... through verse 40

**Closing Doha:**
- `doha_closing_full.mp3` / `doha_closing_slow.mp3`

### Sundar Kaand (260+ verses × 2 speeds = 520+ files when complete)

**Chaupais:**
- `chaupai_01_full.mp3` / `chaupai_01_slow.mp3`
- `chaupai_02_full.mp3` / `chaupai_02_slow.mp3`
- ... (200+ chaupais)

**Dohas:**
- `doha_01_full.mp3` / `doha_01_slow.mp3`
- `doha_02_full.mp3` / `doha_02_slow.mp3`
- ... (60+ dohas)

## Audio Specifications

- **Format**: MP3
- **Quality**: 128kbps+ (Eleven Labs default)
- **Model**: eleven_multilingual_v2 (supports Hindi/Sanskrit/Awadhi)
- **Voice**: Rachel (default) - clear, neutral female voice
- **Full speed**: Natural conversational pace
- **Slow speed**: 75% speed (slowed down via ffmpeg without pitch change) + pauses for learning

## How Audio Files Are Referenced

The verse layout template automatically constructs audio paths based on:
1. **Collection key** from verse frontmatter (`collection_key: "hanuman-chalisa"`)
2. **Filename** extracted from verse path (`doha_01.md` → `doha_01`)

Example:
```liquid
{% assign collection = page.collection_key | default: "hanuman-chalisa" %}
{% assign audio_full = "/audio/" | append: collection | append: "/" | append: audio_base | append: "_full.mp3" %}
```

Results in: `/audio/hanuman-chalisa/doha_01_full.mp3`

## Total Files by Collection

| Collection | Verses | Audio Files | Status |
|------------|--------|-------------|--------|
| Hanuman Chalisa | 44 | 88 | ✅ Complete |
| Sundar Kaand | 260+ | 520+ | ⚪ Future |
| Bajrang Baan | TBD | TBD | ⚪ Future |

## Cost Estimates

Eleven Labs pricing:
- Free tier: 10,000 characters/month
- Starter: $5/month for 30,000 characters
- Creator: $22/month for 100,000 characters

### Hanuman Chalisa
- Total characters: ~10,000-15,000
- Cost: Free tier (one-time generation)
- Status: ✅ Already generated

### Sundar Kaand
- Total characters: ~80,000-100,000
- Cost: Creator tier for 1-2 months
- Estimated: $44-$66 total
- Status: Not yet started

## Adding Audio for New Collections

1. **Create collection directory**:
   ```bash
   mkdir -p audio/your-collection
   ```

2. **Prepare text content**: Extract devanagari text from verse markdown files

3. **Generate audio**: Create or adapt generation script for the collection

4. **Verify naming**: Ensure filenames match verse filenames (e.g., `chaupai_01.md` → `chaupai_01_full.mp3`)

5. **Test playback**: Visit verse pages to verify audio loads correctly

## Testing Audio

After generating audio files:

1. **Build locally**:
   ```bash
   bundle exec jekyll serve
   ```

2. **Navigate to verse pages**:
   - `/hanuman-chalisa/verse_01/`
   - `/sundar-kaand/chaupai_01/`

3. **Verify playback**:
   - Both full and slow speed players work
   - Audio quality is clear
   - Pronunciation is accurate
   - No distortion in slow speed version

4. **Check mobile compatibility**:
   - Test on iOS Safari and Android Chrome
   - Verify audio controls work on touch devices

## Technical Details

### Slow Speed Generation

Slow speed audio is generated using ffmpeg:

```bash
ffmpeg -i input_full.mp3 -filter:a "atempo=0.75" output_slow.mp3
```

This preserves pitch while slowing down the audio to 75% of original speed.

### Audio Player Implementation

Verse pages use HTML5 `<audio>` elements:
- `preload="metadata"` - Loads metadata but not full audio initially
- Native browser controls for consistency
- Fallback message for unsupported browsers

## Troubleshooting

### Audio Not Playing
- Check file exists at correct path: `audio/{collection}/{filename}_{speed}.mp3`
- Verify collection_key in verse frontmatter matches directory name
- Clear browser cache
- Check browser console for 404 errors

### Slow Speed Issues
- Ensure ffmpeg is installed
- Verify atempo filter is supported
- Check slow file isn't corrupted

### Quality Issues
- Use HD voice if available in Eleven Labs
- Verify bitrate is 128kbps or higher
- Check source text for errors

## Resources

- **Eleven Labs**: [https://elevenlabs.io](https://elevenlabs.io)
- **Generation script**: [scripts/generate_audio.sh](../scripts/generate_audio.sh)
- **Verse layout**: [_layouts/verse.html](../_layouts/verse.html)
- **Developer guide**: [docs/developer-guide.md](../docs/developer-guide.md)
