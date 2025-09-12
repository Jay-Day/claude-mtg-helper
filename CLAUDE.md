# Magic: The Gathering Claude Code Helper

## Project Overview
This repository contains comprehensive Magic: The Gathering reference materials optimized for Claude Code. It provides instant access to rules, banned/restricted lists, format information, and common rulings without requiring web searches.

## How to Use This Project
1. Clone this repository to your local machine
2. Navigate to the project directory in your terminal
3. Run `claude` to start Claude Code
4. Claude will automatically load the CLAUDE.md file and have access to all reference materials

## Core Reference Files
- `CLAUDE.md` (this file) - Main project configuration and overview
- `formats/formats.md` - Complete format specifications and rules
- `card-library/` - Complete Standard card database by set
- `scripts/fetch_set_cards.py` - Tool to fetch new sets from Scryfall API
- `rules/comprehensive-rules-summary.md` - Key rules and interactions (planned)
- `rules/tournament-procedures.md` - Tournament and competitive play rules (planned)
- `formats/banned-restricted.md` - Current banned/restricted lists (planned)
- `rulings/common-interactions.md` - Frequently asked ruling questions (planned)
- `tools/deck-analysis-tools.md` - Templates for deck legality checking (planned)

## Custom Commands Available
When working in this project, you can use these slash commands:

### /ruling [card name or interaction]
Quickly look up rulings for specific cards or interactions

### /legal [format] [card name]
Check if a card is legal in a specific format

### /format [format name]
Get complete format information including banned list and deck construction rules

### /fetch [set_code or "set_name"]
Fetch a new MTG set from Scryfall API and add to local card database

**Examples:**
- `/fetch blb` - Fetch using set code
- `/fetch "Dominaria United"` - Fetch using full set name
- `/fetch --list` - Show available sets to fetch
- `/fetch --recent` - Fetch all sets from current year

### /search [card name]
Search the local card database for a specific card and display its details

**Examples:**
- `/search Lightning Bolt` - Find Lightning Bolt across all sets
- `/search "Jace, the Mind Sculptor"` - Search for planeswalker with exact name
- `/search Uril` - Partial name search (finds "Uril, the Miststalker")
- `/search --set blb Lightning` - Search only within Bloomburrow set

**Returns:**
- Card name, mana cost, type, power/toughness
- Oracle text and abilities
- Set information and collector number
- Format legality status
- Multiple printings if available in different sets

### /update-bans
Instructions for updating banned/restricted lists when new announcements are made

## Scripts Available
### `scripts/fetch_set_cards.py`
Fetches all cards from a specific MTG set via Scryfall API and saves to card-library/<set-name>/

**Usage:**
- `python scripts/fetch_set_cards.py <set_code>` (e.g., "blb", "dmu")  
- `python scripts/fetch_set_cards.py "<set_name>"` (e.g., "Dominaria United")

**Output:**
- `card-library/<set-name>/all_cards_<code>.json` - Complete card data
- `card-library/<set-name>/set_info_<code>.json` - Set metadata

**Note:** Always verify set codes/names exist in Scryfall before fetching

## MTG Knowledge Areas Covered

### Rules and Mechanics
- Comprehensive Rules summary with focus on competitive play
- Layer system and continuous effects
- Timing and priority
- State-based actions
- Replacement and prevention effects
- Stack interactions

### Competitive Formats
- **Standard**: Current Standard environment and rotation
- **Pioneer**: Pioneer-legal sets and banned list
- **Modern**: Modern card pool and restrictions  
- **Legacy**: Legacy banned list and key interactions
- **Vintage**: Vintage restricted list and power level
- **Commander**: EDH rules and banned list
- **Pauper**: Commons-only format restrictions

### Tournament Information
- Tournament Rules summary
- Infraction Procedure Guide highlights
- Deck registration procedures
- Sideboarding rules
- Time procedures

### Card Legality
- **Current as of September 2025**
- Format-specific banned/restricted lists
- Set legality by format
- Promo card legality
- Un-set and specialty product rules

## Key Features for Claude Code

### Instant Reference
All information is stored locally, so Claude can instantly answer questions about:
- Card legality in any format
- Rules interactions and timing
- Tournament procedures
- Deck construction requirements

### No Web Scraping Needed
This repository contains curated, up-to-date information so Claude doesn't need to search the web for:
- Current banned/restricted lists
- Rules clarifications
- Format specifications
- Common ruling scenarios

### Structured for AI Consumption
All files are organized with clear headers, consistent formatting, and searchable keywords to help Claude quickly find relevant information.

## Maintenance Schedule
- **After each Banned & Restricted Announcement**: Update banned/restricted lists
- **After each set release**: Update Standard rotation and new card legality
- **Quarterly**: Review and update tournament procedures
- **As needed**: Add new common rulings and interactions

## Version Information
- **Last Updated**: September 12, 2025
- **Rules Version**: Comprehensive Rules effective July 25, 2025
- **Card Database**: ~10,230+ cards across 39 complete sets
- **Format Coverage**: Complete Modern (2003+), extensive Legacy, current Standard
- **Current Standard Sets** (as of 2025 rotation): 
  - Edge of Eternities (EOE)
  - Magic: The Gathering—FINAL FANTASY (FIN) 
  - Tarkir: Dragonstorm (TDM)
  - Aetherdrift (DFT)
  - Magic: The Gathering Foundations (FDN)
  - Duskmourn: House of Horror (DSK)
  - Bloomburrow (BLB)
  - Outlaws of Thunder Junction (OTJ) (including The Big Score)
  - Murders at Karlov Manor (MKM)
  - The Lost Caverns of Ixalan (LCI)
  - Wilds of Eldraine (WOE)
- **Historic Sets Available**:
  - Modern cornerstones: Mirrodin, Time Spiral, Lorwyn, Scars of Mirrodin
  - Classic blocks: Zendikar, Innistrad, Return to Ravnica, Theros, Khans
  - Recent Standard: Dominaria, Guilds of Ravnica, War of the Spark, Throne of Eldraine
  - Master sets: Modern Masters, Eternal Masters, Time Spiral Remastered
  - Commander staples: Alara block, New Phyrexia, supplemental sets

## Contributing
When updating this repository:
1. Always verify information from official Wizards sources
2. Update the "Last Updated" date in this file
3. Use consistent formatting across all markdown files
4. Test that Claude can quickly find and reference new information

## Legal Notice
This repository contains reference materials for Magic: The Gathering, a game owned by Wizards of the Coast. This is an unofficial reference tool for educational and competitive play purposes. All card names, rules text, and game terminology are property of Wizards of the Coast LLC.

---

## Quick Reference Commands for Claude

When asked about MTG topics, Claude should:

1. **For format questions**: Reference `formats/formats.md` for complete format specifications
2. **For card searches**: Search `card-library/` directories for specific cards
3. **For Standard legality**: Check current Standard sets list and `card-library/` contents
4. **For rules questions**: Reference `rules/comprehensive-rules-summary.md` and `rulings/common-interactions.md` (when available)
5. **For tournament questions**: Reference `rules/tournament-procedures.md` (when available)
6. **For deck analysis**: Use templates in `tools/deck-analysis-tools.md` (when available)

Remember: This repository aims to eliminate the need for web searches on common MTG questions by providing comprehensive, current, and well-organized reference materials.