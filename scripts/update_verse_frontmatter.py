#!/usr/bin/env python3
"""
Update all verse files in _verses/hanuman-chalisa/ to add:
1. collection_key: "hanuman-chalisa"
2. permalink: /chalisa/{filename}/
3. Update previous_verse and next_verse URLs to use /chalisa/ instead of /verses/
"""

import os
import re
from pathlib import Path

def update_verse_file(filepath):
    """Update a single verse file with collection metadata."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract frontmatter
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not match:
        print(f"Warning: No frontmatter found in {filepath}")
        return False

    frontmatter, body = match.groups()

    # Get filename without extension for permalink
    filename = Path(filepath).stem

    # Check if collection_key already exists
    if 'collection_key:' in frontmatter:
        print(f"Skipping {filepath} - already has collection_key")
        return False

    # Add collection_key after layout
    frontmatter = frontmatter.replace(
        'layout: verse',
        'layout: verse\ncollection_key: "hanuman-chalisa"'
    )

    # Add permalink after collection_key
    permalink_line = f'permalink: /chalisa/{filename}/'
    frontmatter = frontmatter.replace(
        'collection_key: "hanuman-chalisa"',
        f'collection_key: "hanuman-chalisa"\n{permalink_line}'
    )

    # Update previous_verse and next_verse URLs
    frontmatter = re.sub(
        r'previous_verse: "/verses/',
        'previous_verse: "/chalisa/',
        frontmatter
    )
    frontmatter = re.sub(
        r'next_verse: "/verses/',
        'next_verse: "/chalisa/',
        frontmatter
    )

    # Reconstruct file
    new_content = f'---\n{frontmatter}\n---\n{body}'

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Updated: {filepath}")
    return True

def main():
    verse_dir = Path('_verses/hanuman-chalisa')

    if not verse_dir.exists():
        print(f"Error: Directory {verse_dir} does not exist")
        return

    # Get all .md files
    verse_files = sorted(verse_dir.glob('*.md'))

    print(f"Found {len(verse_files)} verse files")
    updated_count = 0

    for filepath in verse_files:
        if update_verse_file(filepath):
            updated_count += 1

    print(f"\nUpdated {updated_count} files")

if __name__ == '__main__':
    main()
