yes# Simplified Theme Generation Workflow

This document explains the simplified process for generating theme images using theme YAML files.

## The Problem (Before)

Previously, to generate a new theme, you had to:

1. Read the comprehensive theme YAML specification
2. Manually extract style elements (colors, lighting, composition, etc.)
3. Construct a long style string combining all elements
4. Run: `./generate.sh my-theme --style "long manually-crafted style string"`

This was tedious and error-prone.

## The Solution (Now)

Theme YAML files now include a `generation` section that scripts can read automatically.

### Simplified Command

```bash
# Just specify the theme name!
./scripts/generate.sh modern-minimalist
```

That's it! The script automatically:
- Finds `docs/themes/modern-minimalist.yml`
- Reads the `generation.style_modifier` section
- Uses the `generation.dalle_params` settings
- Generates all 47 images with consistent style

## How It Works

### 1. Theme YAML Structure

```yaml
theme:
  # ... (documentation sections: identity, style, colors, etc.) ...

  # Generation configuration (used by scripts)
  generation:
    # Style description appended to base prompts
    style_modifier: |
      Modern minimalist spiritual art with saffron orange tones,
      dramatic lighting, sacred geometry, ethereal atmosphere...

    # DALL-E 3 API parameters
    dalle_params:
      model: "dall-e-3"
      size: "1024x1792"
      quality: "standard"
      style: "natural"

    # Generation behavior
    retry_count: 3
    rate_limit_delay: 2
    skip_existing: true
```

### 2. Script Behavior

When you run `./scripts/generate.sh theme-name`:

1. **Check for theme YAML**: Looks for `docs/themes/theme-name.yml`
2. **Read generation config**: Extracts `style_modifier` and `dalle_params`
3. **Apply settings**: Uses theme settings as defaults
4. **Generate images**: Combines base prompts from `docs/image-prompts.md` with theme style

### 3. Override Options

You can still override any setting:

```bash
# Override style completely
./scripts/generate.sh modern-minimalist --style "different style"

# Override quality
./scripts/generate.sh modern-minimalist --quality hd

# Override multiple settings
./scripts/generate.sh modern-minimalist \
  --style "custom style" \
  --quality hd \
  --size 1024x1024
```

## Usage Scenarios

### Scenario 1: Generate Existing Theme

**Use case**: Regenerate images for an existing documented theme

```bash
./scripts/generate.sh modern-minimalist
```

**Result**: Uses all settings from `docs/themes/modern-minimalist.yml`

### Scenario 2: Create New Documented Theme

**Use case**: Create a well-documented theme from the start

**Steps**:
1. Copy `docs/themes/modern-minimalist.yml` to `docs/themes/watercolor.yml`
2. Edit the `generation.style_modifier` section:
   ```yaml
   style_modifier: |
     Soft watercolor painting style with gentle pastel colors,
     flowing brush strokes, artistic texture, dreamy atmosphere...
   ```
3. Run: `./scripts/generate.sh watercolor`

**Benefits**: Theme is documented and reproducible

### Scenario 3: Quick Custom Theme

**Use case**: Quickly try a new style without creating documentation

```bash
./scripts/generate.sh experimental --style "cyberpunk neon style"
```

**Result**: Generates images with custom style, no theme YAML needed

### Scenario 4: Iterate on Theme

**Use case**: Refine a theme's style

**Steps**:
1. Generate initial version: `./scripts/generate.sh my-theme`
2. Review images, decide on improvements
3. Edit `docs/themes/my-theme.yml` generation section
4. Delete images: `rm -rf images/my-theme/`
5. Regenerate: `./scripts/generate.sh my-theme`

**Benefits**: Version control tracks style evolution

## Benefits

### 1. Simplicity
- **Before**: `./generate.sh theme --style "long complex style string with colors lighting composition..."`
- **After**: `./generate.sh theme`

### 2. Consistency
- Style definition is centralized in theme YAML
- Regenerating uses exact same settings
- No manual string construction errors

### 3. Documentation
- Theme YAML serves as both spec AND generation config
- Everything in one place
- Design decisions are recorded

### 4. Reproducibility
- Anyone can regenerate a theme exactly: `./generate.sh modern-minimalist`
- No need to ask "what style string did you use?"
- Version controlled with git

### 5. Flexibility
- Can still use manual `--style` for quick experiments
- Can override any theme setting
- Supports both documented and ad-hoc themes

## File Organization

```
hanuman-chalisa/
├── docs/
│   └── themes/
│       ├── README.md                  # Theme documentation overview
│       ├── GENERATION-WORKFLOW.md     # This file
│       └── modern-minimalist.yml      # Theme spec + generation config
│
├── _data/
│   └── themes.yml                     # Simple Jekyll site config
│
├── images/
│   └── modern-minimalist/             # Generated images
│       ├── title-page.png
│       ├── opening-doha-01.png
│       └── ...
│
└── scripts/
    ├── generate.sh                    # Bash wrapper (simplified interface)
    ├── generate_theme_images.py       # Python script (reads theme YAMLs)
    └── requirements.txt               # Includes PyYAML dependency
```

## Creating a New Theme: Complete Workflow

### Option A: Document First (Recommended)

1. **Create theme YAML**:
   ```bash
   cp docs/themes/modern-minimalist.yml docs/themes/my-theme.yml
   ```

2. **Edit generation section**:
   - Update `generation.style_modifier` with your style description
   - Adjust `generation.dalle_params` if needed (quality, size)
   - Update documentation sections (colors, style, purpose)

3. **Generate images**:
   ```bash
   ./scripts/generate.sh my-theme
   ```

4. **Review and iterate**:
   - Check generated images
   - Refine theme YAML if needed
   - Delete and regenerate: `rm -rf images/my-theme && ./scripts/generate.sh my-theme`

5. **Add to site**:
   Edit `_data/themes.yml`:
   ```yaml
   my-theme:
     name_en: "My Theme"
     name_hi: "मेरी थीम"
     description_en: "Theme description"
     description_hi: "थीम विवरण"
     folder: "my-theme"
     default: false
   ```

6. **Commit**:
   ```bash
   git add docs/themes/my-theme.yml
   git add images/my-theme/
   git add _data/themes.yml
   git commit -m "Add my-theme with documented specifications"
   ```

### Option B: Generate First, Document Later

1. **Generate with custom style**:
   ```bash
   ./scripts/generate.sh my-theme --style "your style description"
   ```

2. **Review images**

3. **Create theme YAML** (optional, for documentation):
   - Copy template
   - Document the style you used
   - Record generation parameters

4. **Add to site and commit** (same as Option A steps 5-6)

## Best Practices

1. **Create theme YAMLs for permanent themes**: If you plan to keep a theme, document it in a YAML file

2. **Use descriptive style modifiers**: Be specific about colors, lighting, composition, mood

3. **Test before full generation**: Generate 2-3 images first to verify style

4. **Version control theme YAMLs**: Track theme evolution through git history

5. **Document design decisions**: Use the theme YAML to record why you made certain choices

6. **Keep base prompts separate**: `docs/image-prompts.md` contains theme-agnostic verse descriptions; theme YAML adds style

## Technical Details

### Script Logic

1. `generate.sh` (bash wrapper):
   - Parses command line arguments
   - Checks for API key
   - Installs Python dependencies (including PyYAML)
   - Calls Python script with arguments

2. `generate_theme_images.py` (Python script):
   - Checks if `docs/themes/<theme-name>.yml` exists
   - If exists: loads YAML using PyYAML library
   - Reads `theme.generation.style_modifier` and `theme.generation.dalle_params`
   - Command line args override theme YAML settings
   - Combines base prompts with style modifier
   - Generates images via DALL-E 3 API

### Dependencies

Added to `scripts/requirements.txt`:
```
PyYAML>=6.0.0  # For reading theme YAML files
```

### Backward Compatibility

The simplification is fully backward compatible:

- **Old method still works**: `./generate.sh theme --style "manual style"`
- **New method is optional**: Theme YAML files are optional
- **Progressive enhancement**: Scripts check for theme YAML, fall back to manual style if not found

## Migration Guide

If you generated themes before this simplification:

1. **Create theme YAML** for each existing theme:
   ```bash
   cp docs/themes/modern-minimalist.yml docs/themes/your-theme.yml
   ```

2. **Document the style** you used in `generation.style_modifier`

3. **Test regeneration**:
   ```bash
   # Backup existing images
   cp -r images/your-theme images/your-theme-backup

   # Regenerate from theme YAML
   rm -rf images/your-theme
   ./scripts/generate.sh your-theme

   # Compare results
   ```

4. **Commit theme YAML** to document your theme

## Summary

The simplified workflow:
- **Reduces complexity**: One command instead of manual style construction
- **Improves documentation**: Theme specs double as generation config
- **Maintains flexibility**: Can still override or use manual styles
- **Ensures reproducibility**: `./scripts/generate.sh theme-name` always produces same results

**Before**: Extract style from docs, construct string manually, run command
**After**: Just run `./scripts/generate.sh theme-name`

---

**Created**: January 2026
**Last Updated**: January 2026
