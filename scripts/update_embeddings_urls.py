#!/usr/bin/env python3
"""
Update embeddings.json URLs from /verses/ to /chalisa/ for hanuman-chalisa collection.
Also adds collection metadata to each verse.
"""

import json
from pathlib import Path

def main():
    embeddings_file = Path('data/embeddings.json')

    if not embeddings_file.exists():
        print(f"Error: {embeddings_file} not found")
        return

    # Read embeddings
    with open(embeddings_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("Updating embeddings URLs and adding collection metadata...")

    # Update both EN and HI verses
    for lang in ['en', 'hi']:
        if lang in data.get('verses', {}):
            for verse in data['verses'][lang]:
                # Update URL from /verses/ to /chalisa/
                if 'url' in verse:
                    verse['url'] = verse['url'].replace('/verses/', '/chalisa/')

                # Add collection metadata
                verse['collection'] = 'hanuman-chalisa'

    # Write back
    with open(embeddings_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    en_count = len(data['verses'].get('en', []))
    hi_count = len(data['verses'].get('hi', []))

    print(f"✓ Updated {en_count} EN + {hi_count} HI embeddings")
    print(f"  - Changed URLs from /verses/ to /chalisa/")
    print(f"  - Added collection: 'hanuman-chalisa'")
    print(f"  - Output: {embeddings_file}")

if __name__ == '__main__':
    main()
