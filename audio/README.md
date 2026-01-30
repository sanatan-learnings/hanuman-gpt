# Audio Directory

This directory contains audio pronunciations for each verse of the Hanuman Chalisa, generated using Eleven Labs text-to-speech.

## Generating Audio Files

Use the automated generation script:

```bash
# Generate all 86 audio files
./scripts/generate_audio.sh

# Resume from specific file
./scripts/generate_audio.sh --resume verse_15_full.mp3

# Use different voice
./scripts/generate_audio.sh --voice-id YOUR_VOICE_ID
```

**Requirements:**
- Eleven Labs API key in `.env` file: `ELEVENLABS_API_KEY=your-key-here`
- Get API key from: https://elevenlabs.io/app/settings/api-keys
- `ffmpeg` installed (for slow speed processing)
  - macOS: `brew install ffmpeg`
  - Linux: `sudo apt-get install ffmpeg`

## File Naming Convention

Each verse has two audio files:

### Opening Dohas
- `doha_01_full.mp3` - Full speed recitation
- `doha_01_slow.mp3` - Slow recitation for learning
- `doha_02_full.mp3` - Full speed recitation
- `doha_02_slow.mp3` - Slow recitation for learning

### Main Verses (1-40)
- `verse_01_full.mp3`, `verse_01_slow.mp3`
- `verse_02_full.mp3`, `verse_02_slow.mp3`
- ... and so on through verse 40

### Closing Doha
- `doha_closing_full.mp3` - Full speed recitation
- `doha_closing_slow.mp3` - Slow recitation for learning

## Audio Specifications

- **Format**: MP3
- **Quality**: 128kbps+ (Eleven Labs default)
- **Model**: eleven_multilingual_v2 (supports Hindi/Sanskrit)
- **Voice**: Rachel (default) - clear, neutral female voice
- **Full speed**: Natural conversational pace
- **Slow speed**: 75% speed (slowed down via ffmpeg without pitch change) + pauses for learning

## Total Files

**86 audio files** (43 verses × 2 speeds each)

## Cost Estimate

Eleven Labs pricing:
- Free tier: 10,000 characters/month
- Starter: $5/month for 30,000 characters
- Total characters needed: ~10,000-15,000

One-time generation fits within free tier limits.
