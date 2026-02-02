#!/usr/bin/env python3
"""
Multi-collection embeddings generator wrapper.

This script:
1. Reads enabled collections from _data/collections.yml
2. For each collection, processes verses from _verses/{subdirectory}/
3. Calls verse-embeddings SDK for each collection subdirectory
4. Merges embeddings into unified data/embeddings.json with collection metadata
"""

import json
import os
import subprocess
import sys
import yaml
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def load_collections():
    """Load collections metadata from _data/collections.yml."""
    collections_file = Path('_data/collections.yml')

    if not collections_file.exists():
        print(f"Error: {collections_file} not found")
        sys.exit(1)

    with open(collections_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def get_permalinks_from_directory(verses_dir):
    """Extract permalinks from all verse markdown files in directory."""
    import re
    permalinks = {}

    for md_file in verses_dir.glob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extract title_en and permalink
                # Try quoted titles first (most common)
                title_match = re.search(r'title_en:\s*"([^"]+)"', content)
                if not title_match:
                    title_match = re.search(r"title_en:\s*'([^']+)'", content)
                if not title_match:
                    # Fallback to unquoted
                    title_match = re.search(r'title_en:\s*([^\n]+)', content)

                permalink_match = re.search(r'permalink:\s*([^\n]+)', content)

                if title_match and permalink_match:
                    title = title_match.group(1).strip()
                    permalink = permalink_match.group(1).strip()
                    permalinks[title] = permalink
        except Exception as e:
            print(f"  Warning: Could not read {md_file.name}: {e}")

    return permalinks

def generate_collection_embeddings(collection_key, subdirectory, permalink_base, provider='openai'):
    """Generate embeddings for a single collection."""
    verses_dir = Path(f'_verses/{subdirectory}')

    if not verses_dir.exists():
        print(f"Warning: Verse directory {verses_dir} does not exist")
        return None

    # Get actual permalinks from frontmatter
    permalinks_map = get_permalinks_from_directory(verses_dir)

    # Create temp output file for this collection
    temp_output = Path(f'/tmp/embeddings_{collection_key}.json')

    print(f"\n{'='*60}")
    print(f"Generating embeddings for: {collection_key}")
    print(f"Verses directory: {verses_dir}")
    print(f"Provider: {provider}")
    print(f"{'='*60}\n")

    # Call verse-embeddings SDK
    cmd = [
        'verse-embeddings',
        '--provider', provider,
        '--verses-dir', str(verses_dir),
        '--output', str(temp_output)
    ]

    try:
        # Pass current environment (including loaded .env vars) to subprocess
        result = subprocess.run(cmd, check=True, capture_output=True, text=True, env=os.environ.copy())
        print(result.stdout)

        # Read generated embeddings
        with open(temp_output, 'r', encoding='utf-8') as f:
            embeddings_data = json.load(f)

        # Add collection metadata to each verse and fix URLs
        for lang in ['en', 'hi']:
            if lang in embeddings_data.get('verses', {}):
                for verse in embeddings_data['verses'][lang]:
                    verse['collection'] = collection_key

                    # Try to match title to get actual permalink
                    verse_title = verse.get('title', '')
                    if verse_title in permalinks_map:
                        verse['url'] = permalinks_map[verse_title]
                    elif 'url' in verse:
                        # Fallback: Update URL to use collection permalink_base
                        # e.g., /verses/verse_01 -> /chalisa/verse_01
                        verse['url'] = verse['url'].replace('/verses/', permalink_base)

        # Clean up temp file
        temp_output.unlink()

        return embeddings_data

    except subprocess.CalledProcessError as e:
        print(f"Error generating embeddings for {collection_key}:")
        print(e.stderr)
        return None
    except FileNotFoundError:
        print("\nError: verse-embeddings command not found!")
        print("Please install the SDK:")
        print("  python3 -m venv venv")
        print("  source venv/bin/activate")
        print("  pip install verse-content-sdk")
        sys.exit(1)

def merge_embeddings(embeddings_list):
    """Merge multiple collection embeddings into unified structure."""
    if not embeddings_list:
        return None

    # Use first collection's metadata as base
    merged = {
        'model': embeddings_list[0]['model'],
        'dimensions': embeddings_list[0]['dimensions'],
        'provider': embeddings_list[0]['provider'],
        'generated_at': datetime.now().isoformat(),
        'verses': {
            'en': [],
            'hi': []
        }
    }

    # Merge all verses
    for embeddings in embeddings_list:
        for lang in ['en', 'hi']:
            if lang in embeddings.get('verses', {}):
                merged['verses'][lang].extend(embeddings['verses'][lang])

    return merged

def main():
    """Main entry point."""
    # Parse arguments
    provider = 'openai'  # default
    if len(sys.argv) > 1 and sys.argv[1] == '--provider':
        provider = sys.argv[2]

    print("Multi-Collection Embeddings Generator")
    print("=" * 60)

    # Load collections
    collections = load_collections()

    if not collections:
        print("Error: No collections found in _data/collections.yml")
        sys.exit(1)

    # Get enabled collections
    enabled_collections = {
        key: info for key, info in collections.items()
        if info.get('enabled', False)
    }

    if not enabled_collections:
        print("Error: No enabled collections found")
        sys.exit(1)

    print(f"\nEnabled collections: {', '.join(enabled_collections.keys())}")
    print(f"Provider: {provider}\n")

    # Generate embeddings for each collection
    all_embeddings = []
    for coll_key, coll_info in enabled_collections.items():
        subdirectory = coll_info.get('subdirectory', coll_key)
        permalink_base = coll_info.get('permalink_base', f'/{coll_key}/')
        embeddings = generate_collection_embeddings(coll_key, subdirectory, permalink_base, provider)

        if embeddings:
            all_embeddings.append(embeddings)
            verse_count_en = len(embeddings['verses'].get('en', []))
            verse_count_hi = len(embeddings['verses'].get('hi', []))
            print(f"✓ Generated {verse_count_en} EN + {verse_count_hi} HI embeddings for {coll_key}")
        else:
            print(f"✗ Failed to generate embeddings for {coll_key}")

    if not all_embeddings:
        print("\nError: No embeddings were generated")
        sys.exit(1)

    # Merge all embeddings
    print("\nMerging embeddings...")
    merged = merge_embeddings(all_embeddings)

    # Write unified embeddings file
    output_file = Path('data/embeddings.json')
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    total_en = len(merged['verses']['en'])
    total_hi = len(merged['verses']['hi'])

    print(f"\n{'='*60}")
    print(f"✓ Successfully generated unified embeddings")
    print(f"  Output: {output_file}")
    print(f"  Total verses: {total_en} EN + {total_hi} HI")
    print(f"  Collections: {len(all_embeddings)}")
    print(f"  Provider: {provider}")
    print(f"  Model: {merged['model']}")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()
