# verse-content-sdk Enhancement Proposal

## Overview

Enhance the verse-content-sdk to natively support multi-collection workflows, eliminating the need for wrapper scripts in individual projects.

## Current State

**What SDK provides:**
- `verse-embeddings` - Generate embeddings for a single directory
- `verse-audio` - Generate audio for Hanuman Chalisa (hardcoded)
- `verse-images` - Generate images from prompts

**Limitations:**
- No native multi-collection support
- Audio command is Chalisa-specific
- Embeddings command processes single directory only
- URL generation from filenames, not frontmatter permalinks
- No collection metadata in outputs

## Proposed Enhancements

### 1. Multi-Collection Configuration

Add support for reading a collections configuration file:

```yaml
# collections.yml or collections.json
hanuman-chalisa:
  key: "hanuman-chalisa"
  name_en: "Hanuman Chalisa"
  name_hi: "हनुमान चालीसा"
  permalink_base: "/chalisa/"
  subdirectory: "hanuman-chalisa"
  enabled: true

sundar-kaand:
  key: "sundar-kaand"
  name_en: "Sundar Kaand"
  name_hi: "सुंदर कांड"
  permalink_base: "/sundar-kaand/"
  subdirectory: "sundar-kaand"
  enabled: true
```

### 2. verse-embeddings Enhancements

**Current:**
```bash
verse-embeddings --provider openai --verses-dir ./_verses --output ./data/embeddings.json
```

**Proposed:**
```bash
# Single collection (existing behavior)
verse-embeddings --provider openai --verses-dir ./_verses/hanuman-chalisa --output embeddings.json

# NEW: Multi-collection mode
verse-embeddings --multi-collection --collections-file collections.yml --output embeddings.json
```

**Multi-collection behavior:**
1. Read collections configuration
2. Process each enabled collection
3. Add collection metadata to each verse:
   ```json
   {
     "title": "Verse 1: ...",
     "url": "/chalisa/verse_01/",
     "collection": "hanuman-chalisa",
     "embedding": [...]
   }
   ```
4. Merge all collections into single output file
5. Use permalink from frontmatter if available, otherwise generate from filename

**Implementation notes:**
- Read `permalink:` field from verse frontmatter for accurate URLs
- Fall back to generated URL if permalink not present
- Add collection name and key to metadata
- Maintain backward compatibility with single-directory mode

### 3. verse-audio Enhancements

**Current:**
```bash
verse-audio --voice-id VOICE_ID --start-from verse_15_full.mp3
```

Problems:
- Hardcoded for "Hanuman Chalisa verses" (see help text)
- Not collection-aware
- No multi-collection support

**Proposed:**
```bash
# Single collection (updated)
verse-audio --collection hanuman-chalisa --verses-dir _verses/hanuman-chalisa --output-dir audio/hanuman-chalisa

# NEW: Multi-collection mode
verse-audio --multi-collection --collections-file collections.yml
```

**Multi-collection behavior:**
1. Read collections configuration
2. For each enabled collection:
   - Process verses from `_verses/{subdirectory}/`
   - Generate audio files to `audio/{collection}/`
   - Follow collection-specific file naming (chaupai_XX, verse_XX, doha_XX, etc.)
3. Extract devanagari text from frontmatter
4. Generate full + slow speed audio
5. Support resume/regenerate per collection

**Implementation notes:**
- Remove "Hanuman Chalisa" hardcoding from help text and code
- Support arbitrary verse file naming conventions
- Output to collection-specific directories
- Allow collection-specific voice settings

### 4. verse-images Enhancements

**Current:**
```bash
verse-images --theme-name modern-minimalist --style "spiritual art style"
```

**Issues:**
- Generates to generic `images/modern-minimalist/` directory
- No collection context

**Proposed:**
```bash
# Single collection
verse-images --collection hanuman-chalisa --theme modern-minimalist --output-dir images/hanuman-chalisa/modern-minimalist

# Multi-collection (if prompts file has collection markers)
verse-images --multi-collection --collections-file collections.yml
```

**Multi-collection behavior:**
1. Read collections configuration
2. Look for collection-specific prompt files:
   - `docs/hanuman-chalisa-prompts.md`
   - `docs/sundar-kaand-prompts.md`
3. Generate images to collection-specific directories
4. Support different naming conventions per collection

## File Structure After SDK Changes

```
project/
├── _data/
│   └── collections.yml          # Multi-collection config
├── _verses/
│   ├── hanuman-chalisa/
│   │   ├── doha_01.md
│   │   └── verse_01.md
│   └── sundar-kaand/
│       ├── chaupai_01.md
│       └── doha_01.md
├── audio/
│   ├── hanuman-chalisa/
│   │   ├── doha_01_full.mp3
│   │   └── verse_01_full.mp3
│   └── sundar-kaand/
│       ├── chaupai_01_full.mp3
│       └── doha_01_full.mp3
├── images/
│   ├── hanuman-chalisa/
│   │   ├── modern-minimalist/
│   │   ├── kids-friendly/
│   │   └── traditional/
│   └── sundar-kaand/
│       └── modern-minimalist/
└── data/
    └── embeddings.json          # Unified, multi-collection
```

## Benefits

1. **Single source of truth**: Collection logic in SDK, not wrapper scripts
2. **Consistency**: All commands work the same way across collections
3. **Reusability**: Other projects can use multi-collection support
4. **Maintainability**: Less custom code per project
5. **Error handling**: Centralized, better tested
6. **Documentation**: SDK docs cover multi-collection use cases

## Migration Path

For existing projects like hanuman-chalisa:

1. **Before SDK update**: Use wrapper scripts
   - `scripts/generate_embeddings_multi.py` (current)
   - Can continue using these until SDK updated

2. **After SDK update**: Direct SDK commands
   ```bash
   # Old (wrapper)
   python scripts/generate_embeddings_multi.py

   # New (SDK)
   verse-embeddings --multi-collection --collections-file _data/collections.yml

   # Old (wrapper)
   python scripts/generate_audio_multi.py  # if we created it

   # New (SDK)
   verse-audio --multi-collection --collections-file _data/collections.yml
   ```

3. **Delete wrapper scripts**: Remove custom scripts, use SDK directly

## Backward Compatibility

- All existing single-collection commands work unchanged
- `--multi-collection` is opt-in
- Collections file is optional (defaults to single collection mode)
- Existing projects continue working until they choose to adopt multi-collection

## Implementation Priority

### Phase 1 (Critical):
1. ✅ **verse-embeddings multi-collection support**
   - Most important for search/guidance functionality
   - Already have working reference implementation in wrapper script

2. ✅ **verse-audio collection-aware**
   - Remove hardcoded "Hanuman Chalisa" references
   - Support collection-specific output directories

### Phase 2 (Enhancement):
3. **verse-images multi-collection support**
   - Less urgent (can generate per-collection manually)
   - Nice to have for consistency

### Phase 3 (Polish):
4. **Comprehensive docs and examples**
5. **Collection templates/scaffolding**
6. **Validation and error messages**

## Reference Implementation

See current working wrapper script:
- `scripts/generate_embeddings_multi.py` - Shows how multi-collection embeddings work
- Key features to port:
  - Read collections.yml
  - Process enabled collections
  - Extract permalinks from frontmatter
  - Merge results with collection metadata
  - Use python-dotenv for API keys

## Questions/Decisions

1. **Config format**: YAML or JSON? (Suggest YAML for readability)
2. **Config location**: Accept path or search standard locations? (Suggest `--collections-file` parameter)
3. **URL generation**: Always read permalink from frontmatter or make it optional? (Suggest always read if present)
4. **Collection metadata**: What fields to include? (Suggest: collection key, name, permalink_base)
5. **Error handling**: Fail on first error or continue with warnings? (Suggest continue with warnings)

## Testing Checklist

- [ ] Single collection mode still works (backward compat)
- [ ] Multi-collection mode with 2 collections
- [ ] Multi-collection mode with 1 enabled, 1 disabled
- [ ] Permalink extraction from frontmatter
- [ ] URL fallback when permalink missing
- [ ] Collection metadata in all outputs
- [ ] Error handling for missing directories
- [ ] Error handling for invalid YAML/JSON
- [ ] Different verse naming conventions (verse_XX, chaupai_XX, doha_XX)
- [ ] Large collections (100+ verses)
