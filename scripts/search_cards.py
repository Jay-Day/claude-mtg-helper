#!/usr/bin/env python3
"""
MTG Card Search Script for Claude Code /search command
Searches through the local card database efficiently
"""

import json
import os
import sys
import re
from pathlib import Path
from typing import List, Dict, Any, Optional

def load_card_data() -> List[Dict[str, Any]]:
    """Load all card data from the card-library directory"""
    cards = []
    card_library_path = Path("card-library")
    
    if not card_library_path.exists():
        return cards
    
    # Find all all_cards_*.json files
    for json_file in card_library_path.rglob("all_cards_*.json"):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                set_data = json.load(f)
                if isinstance(set_data, list):
                    cards.extend(set_data)
                elif isinstance(set_data, dict) and 'data' in set_data:
                    cards.extend(set_data['data'])
        except (json.JSONDecodeError, FileNotFoundError, KeyError):
            continue
    
    return cards

def search_cards(query: str, set_filter: Optional[str] = None) -> List[Dict[str, Any]]:
    """Search for cards matching the query"""
    cards = load_card_data()
    results = []
    
    # Create case-insensitive regex pattern
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    
    for card in cards:
        # Skip if set filter specified and doesn't match
        if set_filter and card.get('set', '').lower() != set_filter.lower():
            continue
            
        # Search in card name
        if pattern.search(card.get('name', '')):
            results.append(card)
    
    # Sort results by exact match first, then alphabetically
    def sort_key(card):
        name = card.get('name', '').lower()
        query_lower = query.lower()
        if name == query_lower:
            return (0, name)  # Exact match first
        elif name.startswith(query_lower):
            return (1, name)  # Starts with query second
        else:
            return (2, name)  # Contains query last
    
    results.sort(key=sort_key)
    return results

def format_mana_symbols(mana_cost: str) -> str:
    """Convert mana cost to readable symbols"""
    if not mana_cost:
        return ""
    
    # Replace mana symbols with readable equivalents
    mana_cost = mana_cost.replace('{', '').replace('}', '')
    mana_cost = re.sub(r'(\d+)', r'(\1)', mana_cost)
    mana_cost = mana_cost.replace('W', '(W)').replace('U', '(U)').replace('B', '(B)')
    mana_cost = mana_cost.replace('R', '(R)').replace('G', '(G)').replace('C', '(C)')
    mana_cost = mana_cost.replace('X', '(X)').replace('Y', '(Y)').replace('Z', '(Z)')
    
    return mana_cost

def wrap_text(text: str, width: int) -> List[str]:
    """Wrap text to specified width"""
    if not text:
        return [""]
    
    words = text.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line + " " + word) <= width:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    return lines if lines else [""]

def format_card_output(card: Dict[str, Any]) -> str:
    """Format a single card in ASCII MTG card format"""
    name = card.get('name', 'Unknown')
    mana_cost = format_mana_symbols(card.get('mana_cost', ''))
    type_line = card.get('type_line', '')
    oracle_text = card.get('oracle_text', '')
    power = card.get('power')
    toughness = card.get('toughness')
    set_name = card.get('set_name', '')
    set_code = card.get('set', '').upper()
    collector_number = card.get('collector_number', '')
    
    # Card dimensions
    card_width = 50
    
    # Build the card
    output = "+" + "-" * (card_width - 2) + "+\n"
    
    # Name and mana cost line
    name_line = f"{name}"
    if mana_cost:
        name_line += f" {mana_cost}"
    
    if len(name_line) > card_width - 4:
        name_line = name_line[:card_width - 7] + "..."
    
    output += f"| {name_line:<{card_width - 3}} |\n"
    output += "+" + "-" * (card_width - 2) + "+\n"
    
    # Type line
    if len(type_line) > card_width - 4:
        type_line = type_line[:card_width - 7] + "..."
    output += f"| {type_line:<{card_width - 3}} |\n"
    
    if oracle_text:
        output += "+" + "-" * (card_width - 2) + "+\n"
        
        # Oracle text (wrapped)
        text_lines = wrap_text(oracle_text, card_width - 4)
        for line in text_lines:
            output += f"| {line:<{card_width - 3}} |\n"
    
    # Power/Toughness for creatures
    if power is not None and toughness is not None:
        output += "+" + "-" * (card_width - 2) + "+\n"
        pt_text = f"{power}/{toughness}"
        output += f"|{' ' * (card_width - len(pt_text) - 3)}{pt_text} |\n"
    
    # Set info
    output += "+" + "-" * (card_width - 2) + "+\n"
    set_info = f"{set_name} ({set_code}) #{collector_number}"
    if len(set_info) > card_width - 4:
        set_info = set_info[:card_width - 7] + "..."
    output += f"| {set_info:<{card_width - 3}} |\n"
    
    # Close the card
    output += "+" + "-" * (card_width - 2) + "+\n"
    
    return output

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python search_cards.py <card_name> [--set <set_code>]")
        sys.exit(1)
    
    # Parse arguments
    query = sys.argv[1]
    set_filter = None
    
    if '--set' in sys.argv:
        try:
            set_index = sys.argv.index('--set')
            set_filter = sys.argv[set_index + 1]
        except (IndexError, ValueError):
            print("Error: --set requires a set code")
            sys.exit(1)
    
    # Perform search
    results = search_cards(query, set_filter)
    
    if not results:
        print(f"No cards found matching '{query}'", file=sys.stderr)
        if set_filter:
            print(f"in set '{set_filter}'", file=sys.stderr)
        sys.exit(0)
    
    # Display results - using stderr so it's not collapsible
    
    print(f"Found {len(results)} card(s) matching '{query}':", file=sys.stderr)
    if set_filter:
        print(f"(filtered to set: {set_filter})", file=sys.stderr)
    print(file=sys.stderr)
    
    for i, card in enumerate(results[:10]):  # Limit to 10 results
        print(format_card_output(card), file=sys.stderr)
        if i < len(results) - 1 and i < 9:
            print("---", file=sys.stderr)
    
    if len(results) > 10:
        print(f"... and {len(results) - 10} more results", file=sys.stderr)

if __name__ == "__main__":
    main()