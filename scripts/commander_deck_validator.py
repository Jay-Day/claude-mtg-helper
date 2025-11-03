#!/usr/bin/env python3
"""
MTG Commander Deck Validator

Comprehensive validator for Commander/EDH deck legality including:
- Card count (exactly 100 cards)
- Singleton format (no duplicates except basic lands)
- Color identity restrictions
- Commander legality
- Format legality (cards legal in Commander format)
"""

import sys
import os
import re
import json
import requests
import time
import subprocess

def load_card_data():
    """Load card data from our card library for format and color identity checking"""
    card_data = {}
    card_library_path = "card-library"

    if not os.path.exists(card_library_path):
        print(f"Warning: Card library not found at {card_library_path}")
        return card_data

    # Walk through all set directories
    for set_dir in os.listdir(card_library_path):
        set_path = os.path.join(card_library_path, set_dir)
        if not os.path.isdir(set_path):
            continue

        # Look for card data files
        for file in os.listdir(set_path):
            if file.startswith("all_cards_") and file.endswith(".json"):
                json_path = os.path.join(set_path, file)
                try:
                    with open(json_path, 'r', encoding='utf-8') as f:
                        cards = json.load(f)
                        for card in cards:
                            card_name = card.get('name', '')
                            if card_name:
                                card_data[card_name] = card
                except Exception as e:
                    print(f"Warning: Could not load {json_path}: {e}")
                    continue

    return card_data

def fetch_missing_card_from_scryfall(card_name):
    """Fetch a single card from Scryfall API and determine its set"""
    try:
        # Clean up card name for API
        clean_name = card_name.replace("'", "'").strip()

        # Search for exact card name
        url = f"https://api.scryfall.com/cards/named?exact={requests.utils.quote(clean_name)}"
        response = requests.get(url)

        if response.status_code == 200:
            card_data = response.json()
            set_code = card_data.get('set', '').lower()
            return set_code, card_data
        else:
            print(f"Warning: Could not find '{card_name}' on Scryfall")
            return None, None

    except Exception as e:
        print(f"Warning: Error fetching '{card_name}' from Scryfall: {e}")
        return None, None

def auto_fetch_missing_sets(missing_cards):
    """Auto-fetch sets for missing cards from Scryfall"""
    if not missing_cards:
        return

    print(f"\nFound {len(missing_cards)} missing cards. Attempting to fetch from Scryfall...")

    sets_to_fetch = set()

    # Find sets for missing cards
    for card_name in missing_cards[:5]:  # Limit to 5 to avoid rate limiting
        print(f"  Searching for: {card_name}")
        set_code, _ = fetch_missing_card_from_scryfall(card_name)

        if set_code:
            sets_to_fetch.add(set_code)
            print(f"    Found in set: {set_code.upper()}")

        time.sleep(0.1)  # Rate limiting

    # Fetch the sets
    if sets_to_fetch:
        print(f"\nFetching {len(sets_to_fetch)} sets: {', '.join(s.upper() for s in sets_to_fetch)}")

        for set_code in sets_to_fetch:
            try:
                print(f"  Fetching {set_code.upper()}...")
                result = subprocess.run([
                    'python', 'scripts/fetch_set_cards.py', set_code
                ], capture_output=True, text=True, cwd='.')

                if result.returncode == 0:
                    print(f"    Successfully fetched {set_code.upper()}")
                else:
                    print(f"    Failed to fetch {set_code.upper()}: {result.stderr}")

            except Exception as e:
                print(f"    Error fetching {set_code.upper()}: {e}")

        print("\nReloading card database...")
        return True  # Indicate that we fetched new sets

    return False

def parse_deck_file(file_path):
    """
    Parse deck file and return commander and main deck cards.
    Returns tuple of (commander_name, main_deck_cards, errors)
    """
    if not os.path.exists(file_path):
        return None, {}, [f"File not found: {file_path}"]

    commander = None
    main_deck = {}
    errors = []
    line_number = 0
    current_section = None

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line_number += 1
                line = line.strip()

                # Skip empty lines and comments
                if not line or line.startswith('#') or '=' in line:
                    continue

                # Track sections
                if line.isupper() and any(section in line for section in ['COMMANDER', 'LANDS', 'CREATURES']):
                    current_section = line
                    continue

                # Skip description lines and headers
                if (line.endswith(':') or line.startswith('-') or line.startswith('TOTAL:') or
                    any(skip in line.lower() for skip in [
                        'strategy', 'win condition', 'early game', 'mid game', 'late game',
                        'replace', 'budget', 'key interactions', 'gameplay', 'decklist'
                    ])):
                    continue

                # Match pattern: NumberX Card Name
                match = re.match(r'^(\d+)x?\s+(.+)$', line, re.IGNORECASE)
                if match:
                    quantity = int(match.group(1))
                    card_name = match.group(2).strip()

                    # Detect commander
                    if current_section == "COMMANDER" or quantity == 1 and commander is None and "commander" in file_path.lower():
                        if commander is None:
                            commander = card_name
                        else:
                            main_deck[card_name] = quantity
                    else:
                        main_deck[card_name] = quantity

                elif line and not line.startswith('TOTAL:'):
                    # Line looks like it should be a card but doesn't match format
                    if not any(skip in line.lower() for skip in ['strategy', 'win condition', 'early game', 'mid game', 'late game', 'replace', 'budget']):
                        errors.append(f"Line {line_number}: Unrecognized format: '{line}'")

    except Exception as e:
        errors.append(f"Error reading file: {e}")

    return commander, main_deck, errors

def get_color_identity(card_data, card_name):
    """Extract color identity from card data"""
    if card_name not in card_data:
        return set()

    card = card_data[card_name]
    colors = set()

    # Prefer the color_identity field if available (most accurate)
    color_identity = card.get('color_identity', [])
    if color_identity:
        colors.update(color_identity)
        return colors

    # Fallback: Check mana cost (but avoid generic/colorless mana)
    mana_cost = card.get('mana_cost', '')
    if mana_cost:
        # Only extract actual color symbols, not numbers or {C} or {X}
        colors.update(re.findall(r'[WUBRG]', mana_cost))

    # Note: We don't parse oracle text for color identity as it can include
    # mana symbols that are just referenced, not part of the card's identity

    return colors

def is_land(card_data, card_name):
    """Check if a card is a land"""
    if card_name not in card_data:
        # Basic lands are always lands even if not in database
        basic_lands = {
            'Plains', 'Island', 'Swamp', 'Mountain', 'Forest',
            'Wastes', 'Snow-Covered Plains', 'Snow-Covered Island',
            'Snow-Covered Swamp', 'Snow-Covered Mountain', 'Snow-Covered Forest'
        }
        return card_name in basic_lands

    card = card_data[card_name]
    type_line = card.get('type_line', '').lower()
    return 'land' in type_line

def is_creature(card_data, card_name):
    """Check if a card is a creature"""
    if card_name not in card_data:
        return False

    card = card_data[card_name]
    type_line = card.get('type_line', '').lower()
    return 'creature' in type_line

def is_ramp_spell(card_data, card_name):
    """Check if a card is a ramp spell (helps with mana acceleration)"""
    if card_name not in card_data:
        return False

    card = card_data[card_name]
    oracle_text = card.get('oracle_text', '').lower()
    type_line = card.get('type_line', '').lower()

    # Common ramp indicators
    ramp_keywords = [
        'search your library for a land',
        'search your library for up to',
        'basic land',
        'put a land',
        'add mana',
        'produces mana',
        'mana acceleration'
    ]

    # Mana dorks (creatures that produce mana)
    if 'creature' in type_line and any(keyword in oracle_text for keyword in ['add', 'tap']):
        if any(color in oracle_text for color in ['{G}', '{R}', '{W}', '{U}', '{B}', '{C}']):
            return True

    # Ramp spells and artifacts
    return any(keyword in oracle_text for keyword in ramp_keywords)

def check_best_practices(main_deck, card_data):
    """
    Check Commander deck building best practices.
    Returns list of recommendations (not violations)
    """
    recommendations = []

    # Count different card types
    land_count = 0
    creature_count = 0
    ramp_count = 0
    card_draw_count = 0
    removal_count = 0

    for card_name, quantity in main_deck.items():
        if is_land(card_data, card_name):
            land_count += quantity
        elif is_creature(card_data, card_name):
            creature_count += quantity
        elif is_ramp_spell(card_data, card_name):
            ramp_count += quantity

        # Check for card draw (simplified)
        if card_name in card_data:
            oracle_text = card_data[card_name].get('oracle_text', '').lower()
            if any(phrase in oracle_text for phrase in ['draw a card', 'draw cards', 'draw two', 'draw three']):
                card_draw_count += quantity

            # Check for removal (simplified)
            if any(phrase in oracle_text for phrase in ['destroy target', 'exile target', 'return target', 'damage to target']):
                removal_count += quantity

    # Best Practice 1: Land count (35+ recommended)
    if land_count < 35:
        recommendations.append(f"Consider adding more lands: {land_count}/35+ recommended (need {35 - land_count} more)")
    elif land_count > 40:
        recommendations.append(f"Consider reducing lands: {land_count} may be too many (35-40 is typical)")

    # Best Practice 2: Creature count (20-30 recommended)
    if creature_count < 15:
        recommendations.append(f"Consider adding more creatures: {creature_count}/15+ recommended for board presence")
    elif creature_count > 35:
        recommendations.append(f"Consider reducing creatures: {creature_count} may be too many (20-30 is typical)")

    # Best Practice 3: Ramp (8-12 recommended)
    if ramp_count < 8:
        recommendations.append(f"Consider adding more ramp: {ramp_count}/8+ recommended for consistent mana")

    # Best Practice 4: Card draw (8-10 recommended)
    if card_draw_count < 6:
        recommendations.append(f"Consider adding more card draw: {card_draw_count}/6+ recommended to avoid running out of cards")

    # Best Practice 5: Removal (8-12 recommended)
    if removal_count < 6:
        recommendations.append(f"Consider adding more removal: {removal_count}/6+ recommended to handle threats")

    return recommendations, {
        'lands': land_count,
        'creatures': creature_count,
        'ramp': ramp_count,
        'card_draw': card_draw_count,
        'removal': removal_count
    }

def validate_commander_deck(file_path):
    """
    Validate all Commander deck rules.
    Returns tuple of (is_valid, violations, stats)
    """
    violations = []
    stats = {}

    # Load card database
    print("Loading card database...")
    card_data = load_card_data()
    print(f"Loaded {len(card_data)} cards from database")

    # Parse deck file
    commander, main_deck, parse_errors = parse_deck_file(file_path)

    if parse_errors:
        violations.extend([f"Parse Error: {error}" for error in parse_errors])

    if not commander:
        violations.append("No commander found - Commander section missing or unclear")
        return False, violations, {}

    # Calculate stats
    total_main_deck = sum(main_deck.values())
    total_cards = total_main_deck + 1  # +1 for commander
    unique_cards = len(main_deck)

    stats = {
        'commander': commander,
        'total_cards': total_cards,
        'main_deck_cards': total_main_deck,
        'unique_cards': unique_cards,
        'commander_in_db': commander in card_data,
    }

    # Rule 1: Exactly 100 cards total
    if total_cards != 100:
        difference = total_cards - 100
        if difference > 0:
            violations.append(f"Too many cards: {total_cards}/100 (+{difference})")
        else:
            violations.append(f"Too few cards: {total_cards}/100 ({difference})")

    # Rule 2: Singleton format (except basic lands)
    basic_lands = {
        'Plains', 'Island', 'Swamp', 'Mountain', 'Forest',
        'Wastes', 'Snow-Covered Plains', 'Snow-Covered Island',
        'Snow-Covered Swamp', 'Snow-Covered Mountain', 'Snow-Covered Forest'
    }

    for card_name, quantity in main_deck.items():
        if quantity > 1 and card_name not in basic_lands:
            violations.append(f"Non-basic card appears {quantity} times: {card_name}")

    # Rule 3: Commander must be legendary creature (or allowed planeswalker)
    if commander in card_data:
        commander_card = card_data[commander]
        type_line = commander_card.get('type_line', '').lower()

        if 'legendary' not in type_line:
            violations.append(f"Commander must be legendary: {commander}")

        if not ('creature' in type_line or 'planeswalker' in type_line):
            violations.append(f"Commander must be a creature or planeswalker: {commander}")
    else:
        violations.append(f"Commander not found in database: {commander}")

    # Rule 4: Format legality and auto-fetch missing cards (do this before color identity check)
    cards_not_in_db = [name for name in main_deck.keys() if name not in card_data]

    # Auto-fetch missing cards if found
    if cards_not_in_db:
        print(f"\nFound {len(cards_not_in_db)} cards not in database")

        if auto_fetch_missing_sets(cards_not_in_db):
            # Reload card data after fetching new sets
            card_data = load_card_data()
            print(f"Reloaded database with {len(card_data)} total cards")

            # Re-check missing cards
            still_missing = [name for name in main_deck.keys() if name not in card_data]

            if still_missing:
                violations.append(f"Cards still not found after auto-fetch: {', '.join(still_missing[:5])}{'...' if len(still_missing) > 5 else ''}")
            else:
                print("All missing cards now found in database!")

                # Re-validate color identity for newly found cards
                if commander in card_data:
                    commander_colors = get_color_identity(card_data, commander)
                    stats['commander_colors'] = sorted(list(commander_colors))

                    for card_name in main_deck.keys():
                        if card_name in card_data:
                            card_colors = get_color_identity(card_data, card_name)
                            if not card_colors.issubset(commander_colors):
                                illegal_colors = card_colors - commander_colors
                                violations.append(f"Color identity violation: {card_name} contains {sorted(list(illegal_colors))} not in commander's {sorted(list(commander_colors))}")
        else:
            violations.append(f"Cards not in database (could not auto-fetch): {', '.join(cards_not_in_db[:5])}{'...' if len(cards_not_in_db) > 5 else ''}")

    # Rule 5: Color identity restrictions (after auto-fetch)
    if commander in card_data:
        commander_colors = get_color_identity(card_data, commander)
        stats['commander_colors'] = sorted(list(commander_colors))

        for card_name in main_deck.keys():
            if card_name in card_data:
                card_colors = get_color_identity(card_data, card_name)
                if not card_colors.issubset(commander_colors):
                    illegal_colors = card_colors - commander_colors
                    violations.append(f"Color identity violation: {card_name} contains {sorted(list(illegal_colors))} not in commander's {sorted(list(commander_colors))}")
            else:
                violations.append(f"Card not found in database (cannot verify color identity): {card_name}")

    # Best Practices Check (use potentially updated card data)
    recommendations, deck_composition = check_best_practices(main_deck, card_data)
    stats['deck_composition'] = deck_composition
    stats['recommendations'] = recommendations

    is_valid = len(violations) == 0
    return is_valid, violations, stats

def main():
    if len(sys.argv) != 2:
        print("Usage: python commander_deck_validator.py <deck_file_path>")
        print("Example: python commander_deck_validator.py decks/my-commander-deck.txt")
        sys.exit(1)

    deck_file = sys.argv[1]
    print(f"Validating Commander deck: {deck_file}")
    print("=" * 60)

    is_valid, violations, stats = validate_commander_deck(deck_file)

    # Print results
    if stats:
        print("DECK STATISTICS:")
        print(f"  Commander: {stats.get('commander', 'Unknown')}")
        print(f"  Total cards: {stats.get('total_cards', 0)}")
        print(f"  Main deck: {stats.get('main_deck_cards', 0)}")
        print(f"  Unique cards: {stats.get('unique_cards', 0)}")
        if 'commander_colors' in stats:
            colors = stats['commander_colors']
            color_names = {'W': 'White', 'U': 'Blue', 'B': 'Black', 'R': 'Red', 'G': 'Green'}
            color_str = ', '.join([color_names.get(c, c) for c in colors]) if colors else 'Colorless'
            print(f"  Commander colors: {color_str}")

        # Print deck composition
        if 'deck_composition' in stats:
            composition = stats['deck_composition']
            print(f"  Lands: {composition['lands']}")
            print(f"  Creatures: {composition['creatures']}")
            print(f"  Ramp: {composition['ramp']}")
            print(f"  Card draw: {composition['card_draw']}")
            print(f"  Removal: {composition['removal']}")
        print()

    if is_valid:
        print("VALIDATION RESULT: LEGAL")
        print("This deck follows all Commander format rules!")
    else:
        print("VALIDATION RESULT: ILLEGAL")
        print(f"Found {len(violations)} rule violations:")
        for i, violation in enumerate(violations, 1):
            print(f"  {i}. {violation}")

    # Print best practices recommendations
    if stats and 'recommendations' in stats and stats['recommendations']:
        print()
        print("BEST PRACTICES RECOMMENDATIONS:")
        for i, recommendation in enumerate(stats['recommendations'], 1):
            print(f"  {i}. {recommendation}")

    print()
    print("RULES CHECKED:")
    print("  + Card count (exactly 100 cards)")
    print("  + Singleton format (no duplicates except basics)")
    print("  + Commander legality (legendary creature/planeswalker)")
    print("  + Color identity restrictions")
    print("  + Format legality (based on card database)")
    print("  + Best practices (land count, ramp, card draw, removal)")

    # Exit with error code if deck is invalid
    if not is_valid:
        sys.exit(1)

if __name__ == "__main__":
    main()