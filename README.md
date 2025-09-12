# Magic: The Gathering Claude Code Helper

A comprehensive Magic: The Gathering reference repository optimized for use with Claude Code, providing instant access to rules, format information, and card data without requiring web searches.

## 🎯 Purpose

This repository serves as a local MTG knowledge base that eliminates the need for web scraping by providing:
- **Instant Reference**: All MTG data stored locally for immediate access
- **AI-Optimized Structure**: Organized specifically for Claude Code to quickly find information
- **Comprehensive Coverage**: Rules, formats, tournaments, and card databases
- **Always Current**: Updated with latest banned/restricted lists and set releases

## 📁 Repository Structure

```
├── card-library/           # Card databases by set
├── rules/                  # Comprehensive rules and interactions (planned)
├── formats/               # Format specifications and ban lists (planned)
├── rulings/               # Common ruling scenarios (planned)
├── tools/                 # Deck analysis templates (planned)
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

4. **Use custom commands** (when available):
   - `/ruling [card name]` - Look up specific rulings
   - `/legal [format] [card]` - Check card legality  
   - `/format [format]` - Get format details and banned lists

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

## 🎮 Supported Formats

- **Standard** - Current Standard environment and rotation
- **Pioneer** - Pioneer-legal sets and banned list
- **Modern** - Modern card pool and restrictions
- **Legacy** - Legacy banned list and key interactions
- **Vintage** - Vintage restricted list and power level
- **Commander** - EDH rules and banned list
- **Pauper** - Commons-only format restrictions

## 📊 Current Data

- **Last Updated**: September 11, 2025
- **Rules Version**: Comprehensive Rules effective July 25, 2025
- **Current Standard Sets**:
  - Magic: The Gathering—FINAL FANTASY
  - Tarkir: Dragonstorm
  - Magic: The Gathering Foundations
  - Duskmourn: House of Horror
  - Bloomburrow

## 🔧 Features

- **No Web Dependencies**: All data stored locally
- **Claude Code Optimized**: Structured for AI consumption with clear headers and searchable keywords
- **Tournament Ready**: Includes tournament procedures and infraction guidelines
- **Format Specific**: Separate banned/restricted lists for each competitive format
- **Card Databases**: Searchable card references organized by set

## 🤝 Contributing

When updating this repository:
1. Always verify information from official Wizards of the Coast sources
2. Update version information in relevant files
3. Maintain consistent markdown formatting
4. Test that Claude can quickly locate new information

## 📜 Legal Notice

This repository contains reference materials for Magic: The Gathering, a game owned by Wizards of the Coast. This is an unofficial reference tool for educational and competitive play purposes. All card names, rules text, and game terminology are property of Wizards of the Coast LLC.

---

**Built for Claude Code** | **Maintained by the MTG Community** | **Always Up-to-Date**