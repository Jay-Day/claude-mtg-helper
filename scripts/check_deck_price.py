#!/usr/bin/env python3
"""
Check deck price for $30 Value Vintage format compliance.

This script reads a decklist file and checks the total price against the $30 budget limit.
Uses Scryfall API to fetch TCGplayer Market prices for the cheapest English printing.

Usage:
    python scripts/check_deck_price.py <deck_file_path>

Example:
    python scripts/check_deck_price.py decks/my-deck.txt

$30 Value Vintage Pricing Rules:
- Total deck + sideboard must be <= $30 USD
- Uses cheapest English-language, tournament-legal printing
- Basic lands (Plains, Island, Swamp, Mountain, Forest) = $0.00
- Snow-covered basics and Wastes are priced normally
- Prices from TCGplayer Market via Scryfall API
"""

import sys
import requests
import time
import re
from pathlib import Path

# Scryfall API endpoints
SCRYFALL_SEARCH_API = "https://api.scryfall.com/cards/search"
SCRYFALL_NAMED_API = "https://api.scryfall.com/cards/named"

# Basic lands that are free in Value Vintage
FREE_BASICS = {
    "plains", "island", "swamp", "mountain", "forest"
}

def parse_decklist(file_path):
    """
    Parse a decklist file and extract card names with quantities.

    Returns:
        tuple: (main_deck, sideboard) where each is a list of (quantity, card_name) tuples
    """
    main_deck = []
    sideboard = []
    current_section = main_deck

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()

                # Skip empty lines and section headers
                if not line or line.startswith('===') or line.startswith('//'):
                    continue

                # Check for sideboard marker
                if 'SIDEBOARD' in line.upper():
                    current_section = sideboard
                    continue

                # Skip obvious non-card lines (headers, strategy sections, etc.)
                if any(keyword in line.upper() for keyword in [
                    'COMMANDER', 'CREATURES', 'SPELLS', 'LANDS', 'STRATEGY',
                    'FORMAT:', 'DECK SIZE:', 'COLORS:', 'BUDGET', 'KEY INTERACTIONS',
                    'GAME PLAN', 'TOTAL ESTIMATED', 'NON-CREATURE', 'PERMANENTS'
                ]):
                    continue

                # Parse card line: "4x Card Name" or "4 Card Name"
                match = re.match(r'^(\d+)x?\s+(.+)$', line)
                if match:
                    quantity = int(match.group(1))
                    card_name = match.group(2).strip()

                    # Clean up any extra info in parentheses or after //
                    card_name = re.sub(r'\s*\(.*?\)', '', card_name)
                    card_name = card_name.split('//')[0].strip()

                    current_section.append((quantity, card_name))

    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    return main_deck, sideboard


def get_card_price(card_name):
    """
    Fetch the cheapest English printing price from Scryfall.
    Searches all printings and returns the minimum TCGplayer Market price.

    Args:
        card_name: Name of the card

    Returns:
        float: Price in USD, or None if not found
    """
    # Check if it's a free basic land
    if card_name.lower() in FREE_BASICS:
        return 0.0

    try:
        # Query Scryfall for all printings of the card
        # Filter to English, paper printings only
        params = {
            'q': f'!"{card_name}" lang:en game:paper',
            'unique': 'prints',
            'order': 'usd',
            'dir': 'asc'
        }

        response = requests.get(SCRYFALL_SEARCH_API, params=params, timeout=10)

        # Rate limiting: Scryfall requests ~100ms between calls
        time.sleep(0.1)

        if response.status_code == 404:
            print(f"  [!] Card not found: {card_name}")
            return None

        if response.status_code != 200:
            print(f"  [!] API error for {card_name}: {response.status_code}")
            return None

        data = response.json()

        if 'data' not in data or len(data['data']) == 0:
            print(f"  [!] No printings found for: {card_name}")
            return None

        # Search through all printings to find the cheapest with a valid price
        cheapest_price = None

        for card in data['data']:
            # Only consider tournament-legal printings (exclude gold-bordered, etc.)
            if not card.get('legal', True):
                continue

            prices = card.get('prices', {})
            price_usd = prices.get('usd')

            if price_usd is not None:
                price_float = float(price_usd)
                if cheapest_price is None or price_float < cheapest_price:
                    cheapest_price = price_float

        if cheapest_price is None:
            print(f"  [!] No price available for: {card_name}")
            return None

        return cheapest_price

    except requests.exceptions.RequestException as e:
        print(f"  [!] Network error fetching {card_name}: {e}")
        return None
    except Exception as e:
        print(f"  [!] Error processing {card_name}: {e}")
        return None


def check_deck_price(file_path, budget_limit=30.0):
    """
    Check if a deck is legal for $30 Value Vintage budget.

    Args:
        file_path: Path to decklist file
        budget_limit: Budget limit in USD (default: 30.0)
    """
    print(f"\n{'='*60}")
    print(f"$30 Value Vintage Deck Price Checker")
    print(f"{'='*60}")
    print(f"Deck file: {file_path}")
    print(f"Budget limit: ${budget_limit:.2f} USD")
    print(f"{'='*60}\n")

    # Parse decklist
    main_deck, sideboard = parse_decklist(file_path)

    if not main_deck and not sideboard:
        print("Error: No cards found in decklist.")
        sys.exit(1)

    # Calculate prices
    main_deck_total = 0.0
    sideboard_total = 0.0
    main_deck_cards = 0
    sideboard_cards = 0
    errors = []

    print("MAIN DECK:")
    print("-" * 60)

    for quantity, card_name in main_deck:
        price = get_card_price(card_name)

        if price is None:
            errors.append(card_name)
            print(f"  {quantity}x {card_name:45} - [ERROR]")
        else:
            card_total = quantity * price
            main_deck_total += card_total
            main_deck_cards += quantity

            if price == 0.0:
                print(f"  {quantity}x {card_name:45} - FREE (basic land)")
            else:
                print(f"  {quantity}x {card_name:45} - ${price:.2f} ea (${card_total:.2f} total)")

    print(f"\nMain Deck Subtotal: ${main_deck_total:.2f} ({main_deck_cards} cards)")

    if sideboard:
        print(f"\n{'='*60}")
        print("SIDEBOARD:")
        print("-" * 60)

        for quantity, card_name in sideboard:
            price = get_card_price(card_name)

            if price is None:
                errors.append(card_name)
                print(f"  {quantity}x {card_name:45} - [ERROR]")
            else:
                card_total = quantity * price
                sideboard_total += card_total
                sideboard_cards += quantity
                print(f"  {quantity}x {card_name:45} - ${price:.2f} ea (${card_total:.2f} total)")

        print(f"\nSideboard Subtotal: ${sideboard_total:.2f} ({sideboard_cards} cards)")

    # Final results
    total_price = main_deck_total + sideboard_total
    total_cards = main_deck_cards + sideboard_cards
    remaining_budget = budget_limit - total_price

    print(f"\n{'='*60}")
    print("FINAL RESULTS:")
    print("-" * 60)
    print(f"Total Cards: {total_cards}")
    print(f"Total Price: ${total_price:.2f}")
    print(f"Budget Limit: ${budget_limit:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")
    print("-" * 60)

    if errors:
        print(f"\n[WARNING] {len(errors)} card(s) could not be priced:")
        for card in errors:
            print(f"  - {card}")
        print("\nPlease verify these cards manually on TCGplayer.")

    if total_price <= budget_limit:
        print(f"\n[LEGAL] This deck is within the ${budget_limit:.2f} budget!")
    else:
        over_budget = total_price - budget_limit
        print(f"\n[ILLEGAL] This deck is ${over_budget:.2f} OVER budget!")

    print(f"{'='*60}\n")

    return total_price <= budget_limit


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/check_deck_price.py <deck_file_path>")
        print("\nExample:")
        print("  python scripts/check_deck_price.py decks/my-deck.txt")
        sys.exit(1)

    deck_file = sys.argv[1]

    # Optional: custom budget limit
    budget_limit = 30.0
    if len(sys.argv) >= 3:
        try:
            budget_limit = float(sys.argv[2])
        except ValueError:
            print(f"Error: Invalid budget limit: {sys.argv[2]}")
            sys.exit(1)

    check_deck_price(deck_file, budget_limit)


if __name__ == "__main__":
    main()
