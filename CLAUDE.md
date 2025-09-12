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

## Available Commands
When working in this project, you can ask Claude to help with:

### Card Search
Ask Claude to search for specific cards: "search for Lightning Bolt" or "find cards with 'dragon' in the name"
- Uses the efficient `scripts/search_cards.py` script
- Displays results in ASCII MTG card format
- Supports partial name matching and set filtering

### Rulings Lookup
Ask for rulings on specific cards or interactions: "what are the rulings for Kaalia of the Vast?"

### Format Information  
Ask about format specifications: "what are the deck construction rules for Modern?"

### Card Legality
Ask about card legality: "is Lightning Bolt legal in Standard?"

### Set Data Management
Ask Claude to fetch new sets: "fetch the Bloomburrow set" or "add Dominaria United to the database"
- Uses `scripts/fetch_set_cards.py` to get data from Scryfall API

### Ban List Updates
Ask for help updating banned/restricted lists when new announcements are made

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
- **Card Database**: ~11,500+ cards across 42 complete sets
- **Format Coverage**: Complete Modern (2003+), extensive Legacy, current Standard

## Complete Set Database with Release Dates

### Current Standard Sets (2025):
- **Edge of Eternities (EOE)** - August 1, 2025
- **Magic: The Gathering—FINAL FANTASY (FIN)** - June 13, 2025  
- **Tarkir: Dragonstorm (TDM)** - April 11, 2025
- **Aetherdrift (DFT)** - February 14, 2025
- **Magic: The Gathering Foundations (FDN)** - November 15, 2024
- **Duskmourn: House of Horror (DSK)** - September 27, 2024
- **Bloomburrow (BLB)** - August 2, 2024
- **Outlaws of Thunder Junction (OTJ)** - April 19, 2024
- **Murders at Karlov Manor (MKM)** - February 9, 2024
- **The Lost Caverns of Ixalan (LCI)** - November 17, 2023
- **Wilds of Eldraine (WOE)** - September 8, 2023

### Supplemental Sets (2024-2025):
- **Murders at Karlov Manor Commander (MKC)** - February 9, 2024
- **Modern Horizons 3 (MH3)** - June 14, 2024
- **Fallout (PIP)** - March 8, 2024
- **Ravnica Remastered (RVR)** - January 12, 2024
- **Innistrad: Crimson Vow (VOW)** - November 19, 2021
- **Innistrad Remastered (INR)** - January 24, 2025

### Historic Standard Sets:
- **Foundations (FDN)** - November 15, 2024
- **War of the Spark (WAR)** - May 3, 2019
- **Guilds of Ravnica (GRN)** - October 5, 2018
- **Return to Ravnica (RTR)** - October 5, 2012
- **Gatecrash (GTC)** - February 1, 2013
- **Throne of Eldraine (ELD)** - October 4, 2019
- **Dominaria (DOM)** - April 27, 2018
- **Theros (THS)** - September 27, 2013
- **Khans of Tarkir (KTK)** - September 26, 2014

### Core Modern Sets:
- **Innistrad (ISD)** - September 30, 2011
- **Dark Ascension (DKA)** - February 3, 2012  
- **Avacyn Restored (AVR)** - May 4, 2012
- **Scars of Mirrodin (SOM)** - October 1, 2010
- **Mirrodin Besieged (MBS)** - February 4, 2011
- **New Phyrexia (NPH)** - May 13, 2011
- **Zendikar (ZEN)** - October 2, 2009
- **Worldwake (WWK)** - February 5, 2010
- **Rise of the Eldrazi (ROE)** - April 23, 2010
- **Shards of Alara (ALA)** - October 3, 2008
- **Conflux (CON)** - February 6, 2009
- **Alara Reborn (ARB)** - April 30, 2009
- **Lorwyn (LRW)** - October 12, 2007
- **Mirrodin (MRD)** - October 2, 2003
- **Time Spiral (TSP)** - October 6, 2006

### Master/Remaster Sets:
- **Ravnica: Clue Edition (CLU)** - February 23, 2024
- **Time Spiral Remastered (TSR)** - March 19, 2021
- **Modern Masters (MMA)** - June 7, 2013
- **Eternal Masters (EMA)** - June 10, 2016
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

## Commander Deck Building Guidelines

**CRITICAL: When recommending cards for Commander decks, ALWAYS respect color identity restrictions:**

- **Mono-White**: Only White (W) and colorless cards
- **Mono-Blue**: Only Blue (U) and colorless cards  
- **Mono-Black**: Only Black (B) and colorless cards
- **Mono-Red**: Only Red (R) and colorless cards
- **Mono-Green**: Only Green (G) and colorless cards
- **Dimir (UB)**: Only Blue, Black, and colorless cards
- **Azorius (WU)**: Only White, Blue, and colorless cards
- **Rakdos (BR)**: Only Black, Red, and colorless cards
- **Gruul (RG)**: Only Red, Green, and colorless cards
- **Selesnya (GW)**: Only Green, White, and colorless cards
- **Orzhov (WB)**: Only White, Black, and colorless cards
- **Izzet (UR)**: Only Blue, Red, and colorless cards
- **Golgari (BG)**: Only Black, Green, and colorless cards
- **Boros (RW)**: Only Red, White, and colorless cards
- **Simic (GU)**: Only Green, Blue, and colorless cards

**Examples:**
- For Mirko, Obsessive Theorist (Dimir): Only recommend Blue, Black, and colorless cards
- For Uril, the Miststalker (Naya): Only recommend Red, Green, White, and colorless cards
- Never recommend Green cards for a Dimir commander or Black cards for a Selesnya commander

**When searching for commander synergies:**
1. First identify the commander's color identity
2. Only search for and recommend cards within those colors
3. Focus on colorless utility when color restrictions are tight

Remember: This repository aims to eliminate the need for web searches on common MTG questions by providing comprehensive, current, and well-organized reference materials.