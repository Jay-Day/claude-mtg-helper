# Magic: The Gathering Claude Code Helper

A comprehensive Magic: The Gathering reference repository optimized for use with Claude Code, providing instant access to rules, format information, and complete card databases covering Modern, Legacy, Commander, and Standard formats without requiring web searches.

## 🎯 Purpose

This repository serves as a local MTG knowledge base that eliminates the need for web scraping by providing:
- **Instant Reference**: All MTG data stored locally for immediate access
- **AI-Optimized Structure**: Organized specifically for Claude Code to quickly find information
- **Comprehensive Coverage**: Rules, formats, tournaments, and card databases
- **Always Current**: Updated with latest banned/restricted lists and set releases

## 📁 Repository Structure

```
├── card-library/           # ✅ Complete card database by set (44+ sets)
├── formats/                # ✅ Format specifications and banned lists
│   ├── formats.md         # ✅ Complete format rules and specifications
│   └── banned-restricted.md # ✅ Current banned/restricted lists
├── scripts/                # ✅ Data fetching and utility scripts
│   ├── fetch_set_cards.py # ✅ Scryfall API fetcher
│   ├── search_cards.py    # ✅ Card search with ASCII display
│   ├── count_deck_cards.py # ✅ Simple deck card counter
│   └── commander_deck_validator.py # ✅ Comprehensive Commander deck validator
├── rules/                  # 📋 Comprehensive rules and interactions (planned)
├── rulings/                # 📋 Common ruling scenarios (planned)
├── tools/                  # 📋 Deck analysis templates (planned)
├── CLAUDE.md              # ✅ Main project configuration
└── README.md              # This file
```

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Jay-Day/claude-mtg-helper.git
   cd claude-mtg-helper
   ```

2. **Install Python dependencies** (if fetching new sets):
   ```bash
   pip install requests
   ```

3. **Start Claude Code**:
   ```bash
   claude
   ```

4. **Ask Claude for help with MTG questions**:
   - "Search for Lightning Bolt" - ✅ Find cards with ASCII display
   - "What are the rulings for Kaalia?" - 📋 Get specific card rulings (planned)
   - "Is Lightning Bolt legal in Modern?" - ✅ Check format legality
   - "What are Modern format rules?" - ✅ Get complete format specifications
   - "What's banned in Pioneer?" - ✅ Get current banned/restricted lists
   - "Build me a Commander deck around Bello" - ✅ Complete deck building with validation
   - "Validate my Commander deck" - ✅ Comprehensive legality and best practices check

## 🔄 Fetching Card Data

### Requirements
- Python 3.x
- `requests` library (`pip install requests`)
- Internet connection

### Usage
Use the included script to fetch card data from any MTG set:

```bash
python scripts/fetch_set_cards.py <set_code>
python scripts/fetch_set_cards.py "<set_name>"
```

**Examples:**
```bash
python scripts/fetch_set_cards.py blb                    # Bloomburrow
python scripts/fetch_set_cards.py "Dominaria United"    # Full set name
```

**Output:** Creates `card-library/<set-name>/` with:
- `all_cards_<code>.json` - Complete set data
- `set_info_<code>.json` - Set metadata

The script automatically handles API rate limiting and creates organized directories for easy querying.

## 🎯 Commander Deck Validation

The repository includes a comprehensive Commander deck validator that checks both format legality and best practices:

### Usage
```bash
python scripts/commander_deck_validator.py decks/my-deck.txt
```

### Features
- **Format Legality**: Validates all Commander rules (100 cards, singleton, color identity, etc.)
- **Best Practices**: Recommends optimal deck composition
- **Detailed Analysis**: Counts lands, ramp, card draw, and removal
- **Color Identity**: Automatically detects commander colors and validates deck accordingly

### Best Practices Checked
- **35+ Lands**: Minimum recommended for consistent mana
- **8+ Ramp Spells**: For mana acceleration and consistency
- **6+ Card Draw**: To maintain hand advantage
- **6+ Removal**: To handle threats and interactions

### Sample Output
```
DECK STATISTICS:
  Commander: Bello, Bard of the Brambles
  Total cards: 100
  Commander colors: Green, Red
  Lands: 30
  Ramp: 11
  Card draw: 15
  Removal: 12

VALIDATION RESULT: LEGAL
This deck follows all Commander format rules!

BEST PRACTICES RECOMMENDATIONS:
  1. Consider adding more lands: 30/35+ recommended (need 5 more)
```

## 🎮 Supported Formats

- **Standard** - Current Standard environment and rotation
- **Pioneer** - Pioneer-legal sets and banned list
- **Modern** - Modern card pool and restrictions
- **Legacy** - Legacy banned list and key interactions
- **Vintage** - Vintage restricted list and power level
- **Commander** - EDH rules and banned list
- **Pauper** - Commons-only format restrictions

## 📊 Current Data

- **Last Updated**: September 12, 2025
- **Rules Version**: Comprehensive Rules effective July 25, 2025
- **Format Information**: Complete specifications for Standard, Commander, Pioneer, Modern, Legacy, Vintage, Pauper, Draft, and Sealed
- **Banned/Restricted Lists**: Current ban lists for all competitive formats (240+ cards)
- **Card Database**: 44 complete sets (~11,500+ cards) with full JSON data
- **Standard Coverage**: All 11 current Standard-legal sets (2023-2025)
- **Modern Coverage**: Complete Modern card pool from Mirrodin forward (2003+)
- **Historic Sets**: Classic blocks including Zendikar, Innistrad, Return to Ravnica, Theros, Khans of Tarkir
- **Master Sets**: Modern Masters, Eternal Masters, Time Spiral Remastered with format staples
- **Commander Support**: Comprehensive multicolor and tribal support sets

## 🔧 Features

- **No Web Dependencies**: All data stored locally for instant access
- **Claude Code Optimized**: Structured for AI consumption with clear headers and searchable keywords
- **Comprehensive Coverage**: 44 complete sets spanning Modern format's entire history (2003-2025)
- **Current Ban Lists**: Up-to-date banned/restricted cards for all competitive formats
- **Complete Modern Pool**: Every card legal in Modern format with full metadata
- **Eternal Format Support**: Extensive Legacy and Commander card coverage
- **Easy Updates**: Automated scripts for fetching new set releases
- **Format Specifications**: Complete rules and deck construction for all major formats
- **Searchable Database**: JSON format enables fast card lookup and filtering
- **Historic Coverage**: From original Mirrodin through current Standard rotation
- **Commander Deck Validation**: Comprehensive legality checking with best practices recommendations
- **Deck Building Tools**: Complete deck construction with format compliance and optimization

## 🤝 Contributing

When updating this repository:
1. Always verify information from official Wizards of the Coast sources
2. Update version information in relevant files
3. Maintain consistent markdown formatting
4. Test that Claude can quickly locate new information

## 📜 Legal Notice

This repository contains reference materials for Magic: The Gathering, a game owned by Wizards of the Coast. This is an unofficial reference tool for educational and competitive play purposes. All card names, rules text, and game terminology are property of Wizards of the Coast LLC.

---

**Built for Claude Code** | **11,500+ Cards Across 44 Sets** | **Complete Modern Format Coverage** | **Always Up-to-Date**