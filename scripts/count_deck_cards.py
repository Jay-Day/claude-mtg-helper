#!/usr/bin/env python3
"""
MTG Deck Card Counter

Counts cards in a deck file and verifies the total matches expected format requirements.
Supports standard Magic deck formats:
- Commander/EDH: 100 total cards (99 main deck + 1 commander)
- Standard/Modern/Pioneer/Legacy: 60 cards
- Limited (Draft/Sealed): 40 cards
"""

import sys
import os
import re

def count_cards_in_deck(file_path):
    """
    Count cards in a deck file that uses the format:
    1x Card Name
    2x Another Card
    etc.

    Returns tuple of (total_cards, card_breakdown, errors)
    """
    if not os.path.exists(file_path):
        return 0, {}, [f"File not found: {file_path}"]

    total_cards = 0
    card_breakdown = {}
    errors = []
    line_number = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line_number += 1
                line = line.strip()

                # Skip empty lines and headers/comments
                if not line or line.startswith('#') or line.isupper() or '=' in line:
                    continue

                # Match pattern: NumberX Card Name or Number x Card Name
                match = re.match(r'^(\d+)x?\s+(.+)$', line, re.IGNORECASE)
                if match:
                    quantity = int(match.group(1))
                    card_name = match.group(2).strip()

                    total_cards += quantity
                    card_breakdown[card_name] = quantity
                elif line and not line.startswith('TOTAL:') and not line.startswith('-'):
                    # Line looks like it should be a card but doesn't match format
                    errors.append(f"Line {line_number}: Unrecognized format: '{line}'")

    except Exception as e:
        errors.append(f"Error reading file: {e}")

    return total_cards, card_breakdown, errors

def analyze_deck_format(total_cards, file_path):
    """Determine what format this deck is for based on card count"""
    filename = os.path.basename(file_path).lower()

    if 'commander' in filename or 'edh' in filename:
        expected = 100  # 100 total cards (99 main deck + 1 commander)
        format_name = "Commander/EDH"
    elif total_cards == 100:
        expected = 100
        format_name = "Commander/EDH"
    elif total_cards == 60:
        expected = 60
        format_name = "Standard/Modern/Pioneer/Legacy"
    elif total_cards == 40:
        expected = 40
        format_name = "Limited (Draft/Sealed)"
    else:
        expected = None
        format_name = "Unknown"

    return expected, format_name

def main():
    if len(sys.argv) != 2:
        print("Usage: python count_deck_cards.py <deck_file_path>")
        print("Example: python count_deck_cards.py decks/my-deck.txt")
        sys.exit(1)

    deck_file = sys.argv[1]

    print(f"Counting cards in: {deck_file}")
    print("=" * 50)

    total_cards, card_breakdown, errors = count_cards_in_deck(deck_file)

    if errors:
        print("ERRORS FOUND:")
        for error in errors:
            print(f"  ERROR: {error}")
        print()

    print(f"TOTAL CARDS: {total_cards}")

    expected, format_name = analyze_deck_format(total_cards, deck_file)

    if expected:
        print(f"DETECTED FORMAT: {format_name} (expects {expected} cards)")
        if total_cards == expected:
            print("CORRECT: Card count matches expected")
        else:
            difference = total_cards - expected
            if difference > 0:
                print(f"ERROR: TOO MANY cards (+{difference})")
            else:
                print(f"ERROR: TOO FEW cards ({difference})")
    else:
        print(f"DETECTED FORMAT: {format_name}")

    print("\nCARD BREAKDOWN:")
    print("-" * 30)

    # Group by quantity for easier reading
    by_quantity = {}
    for card, qty in card_breakdown.items():
        if qty not in by_quantity:
            by_quantity[qty] = []
        by_quantity[qty].append(card)

    for qty in sorted(by_quantity.keys(), reverse=True):
        print(f"{qty}x cards ({len(by_quantity[qty])} unique):")
        for card in sorted(by_quantity[qty]):
            print(f"  {qty}x {card}")
        print()

    # Summary
    print("SUMMARY:")
    print(f"  Total cards: {total_cards}")
    print(f"  Unique cards: {len(card_breakdown)}")
    print(f"  Format: {format_name}")

    if expected and total_cards != expected:
        sys.exit(1)  # Exit with error code if count is wrong

if __name__ == "__main__":
    main()