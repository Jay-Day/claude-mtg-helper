#!/usr/bin/env python3
"""
Scryfall Set Cards Fetcher

This script fetches all cards from a specific Magic: The Gathering set
and saves them as JSON files in card-library/<set-name>/.

Usage:
    python fetch_set_cards.py <set_code>
    
Example:
    python fetch_set_cards.py dmu
    python fetch_set_cards.py "Dominaria United"
"""

import json
import os
import sys
import time
import requests
from pathlib import Path
import argparse

# Configuration
BASE_URL = "https://api.scryfall.com"
SEARCH_ENDPOINT = "/cards/search"
USER_AGENT = "MTG-Claude-Helper/1.0"
REQUEST_DELAY = 0.1  # 100ms delay between requests

# Headers required by Scryfall API
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "application/json"
}

def fetch_cards_from_set(set_identifier):
    """Fetch all cards from a specific set using Scryfall search API."""
    print(f"Fetching cards from set: {set_identifier}")
    
    # Use set search syntax - works with both set codes and set names
    query = f"set:{set_identifier}"
    
    all_cards = []
    next_page = None
    page_count = 0
    
    try:
        while True:
            page_count += 1
            print(f"Fetching page {page_count}...")
            
            # Build URL
            if next_page:
                url = next_page
            else:
                params = {
                    'q': query,
                    'order': 'set',
                    'unique': 'cards'
                }
                response = requests.get(f"{BASE_URL}{SEARCH_ENDPOINT}", 
                                      headers=HEADERS, params=params)
            
            if next_page:
                response = requests.get(next_page, headers=HEADERS)
            
            response.raise_for_status()
            data = response.json()
            
            # Add cards from this page
            if 'data' in data:
                all_cards.extend(data['data'])
                print(f"  Found {len(data['data'])} cards on page {page_count}")
            
            # Check if there are more pages
            if data.get('has_more', False) and 'next_page' in data:
                next_page = data['next_page']
                time.sleep(REQUEST_DELAY)  # Respect rate limits
            else:
                break
        
        print(f"Total cards found: {len(all_cards)}")
        return all_cards, data.get('data', [{}])[0].get('set_name', set_identifier) if all_cards else set_identifier
    
    except requests.RequestException as e:
        if response.status_code == 404:
            print(f"Set '{set_identifier}' not found. Please check the set code or name.")
        else:
            print(f"Error fetching cards: {e}")
        return None, None

def create_set_directory(set_name):
    """Create the card-library/<set-name> directory."""
    # Clean set name for filesystem
    safe_set_name = "".join(c for c in set_name if c.isalnum() or c in (' ', '-', '_')).strip()
    safe_set_name = safe_set_name.replace(' ', '-').lower()
    
    set_dir = Path("card-library") / safe_set_name
    set_dir.mkdir(parents=True, exist_ok=True)
    
    return set_dir

def save_cards(cards, set_dir, set_name):
    """Save cards to JSON files in the set directory."""
    
    # Get set code for filename
    set_code = cards[0].get('set') if cards else 'unknown'
    
    # Save complete set as one file with set code
    all_cards_file = set_dir / f"all_cards_{set_code}.json"
    with open(all_cards_file, 'w', encoding='utf-8') as f:
        json.dump(cards, f, indent=2, ensure_ascii=False)
    
    print(f"Saved all {len(cards)} cards to {all_cards_file}")
    
    # Create summary file
    summary = {
        'set_name': set_name,
        'set_code': set_code,
        'total_cards': len(cards),
        'card_types': list(set(card.get('type_line', '').split(' — ')[0].split()[0] 
                               for card in cards if card.get('type_line'))),
        'colors': list(set(''.join(card.get('colors', [])) for card in cards)),
        'fetched_at': time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())
    }
    
    summary_file = set_dir / f"set_info_{set_code}.json"
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print(f"Created set summary: {summary_file}")

def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(description='Fetch all cards from a Magic: The Gathering set')
    parser.add_argument('set_identifier', help='Set code (e.g., "dmu") or set name (e.g., "Dominaria United")')
    
    if len(sys.argv) < 2:
        print("Usage: python fetch_set_cards.py <set_code_or_name>")
        print("Examples:")
        print("  python fetch_set_cards.py dmu")
        print('  python fetch_set_cards.py "Dominaria United"')
        sys.exit(1)
    
    args = parser.parse_args()
    set_identifier = args.set_identifier
    
    print("MTG Set Cards Fetcher")
    print("=" * 40)
    
    # Fetch cards
    cards, set_name = fetch_cards_from_set(set_identifier)
    
    if not cards:
        print("No cards found or error occurred.")
        sys.exit(1)
    
    # Create directory
    set_dir = create_set_directory(set_name)
    print(f"Created directory: {set_dir}")
    
    # Save cards
    save_cards(cards, set_dir, set_name)
    
    print(f"\nSuccessfully saved {len(cards)} cards from {set_name}")
    print(f"Files saved in: {set_dir}/")
    print(f"  - all_cards_{cards[0].get('set', 'unknown')}.json (complete set)")
    print(f"  - set_info_{cards[0].get('set', 'unknown')}.json (summary)")

if __name__ == "__main__":
    main()