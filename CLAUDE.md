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
- `formats/formats.md` - ✅ Complete format specifications and rules
- `formats/banned-restricted.md` - ✅ Current banned/restricted lists 
- `formats/commander-color-identity.md` - ✅ Comprehensive Commander color identity guide
- `card-library/` - ✅ Comprehensive card database with 970 paper-playable MTG sets
- `card-library/mtg_sets.txt` - ✅ Complete list of all 971 paper set codes for reference
- `scripts/fetch_set_cards.py` - ✅ Tool to fetch new sets from Scryfall API
- `scripts/search_cards.py` - ✅ Efficient card search with ASCII display
- `rules/comprehensive-rules-summary.md` - 📋 Key rules and interactions (planned)
- `rules/tournament-procedures.md` - 📋 Tournament and competitive play rules (planned)
- `rulings/common-interactions.md` - 📋 Frequently asked ruling questions (planned)
- `tools/deck-analysis-tools.md` - 📋 Templates for deck legality checking (planned)

## Available Commands
When working in this project, you can ask Claude to help with:

### Card Search
Ask Claude to search for specific cards: "search for Lightning Bolt" or "find cards with 'dragon' in the name"
- ✅ Uses the efficient `scripts/search_cards.py` script
- ✅ Displays results in ASCII MTG card format
- ✅ Supports partial name matching and set filtering

### Rulings Lookup
Ask for rulings on specific cards or interactions: "what are the rulings for Kaalia of the Vast?"

### Format Information  
Ask about format specifications: "what are the deck construction rules for Modern?"

### Card Legality
Ask about card legality: "is Lightning Bolt legal in Standard?"

### Set Data Management
Ask Claude to fetch new sets: "fetch the Bloomburrow set" or "add Dominaria United to the database"
- ✅ Uses `scripts/fetch_set_cards.py` to get data from Scryfall API

### Ban List Updates
Ask for help updating banned/restricted lists when new announcements are made

### Deck Building
Ask Claude to build any Magic deck: "make me a commander deck around Skullbriar", "build a budget Modern burn deck", or "create a Standard aggro deck"
- ✅ Creates complete decklists with strategy guides for any format
- ✅ Automatically saves decklists to `decks/` folder as .txt files (gitignored)
- ✅ Respects format restrictions and color identity (Commander)
- ✅ Includes proper manabase (35 lands for Commander), removal, ramp, and win conditions
- ✅ Commander decks have exactly 100 total cards (99 main deck + 1 commander)
- ✅ Uses "1x Card Name" format for easy deck builder import
- ✅ Personal deck creations won't pollute the repository

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

### `scripts/count_deck_cards.py`
Simple card counter for any Magic deck format

**Usage:**
- `python scripts/count_deck_cards.py decks/my-deck.txt`

**Features:**
- Counts total cards in deck file
- Detects format based on card count
- Validates against expected count for format

### `scripts/commander_deck_validator.py`
Comprehensive Commander/EDH deck legality validator

**Usage:**
- `python scripts/commander_deck_validator.py decks/my-commander-deck.txt`

**Validation Rules:**
- ✅ Card count (exactly 100 total cards)
- ✅ Singleton format (no duplicates except basic lands)
- ✅ Commander legality (legendary creature/planeswalker)
- ✅ Color identity restrictions (all cards must match commander's colors)
- ✅ Format legality (based on card database)

**Output:**
- Detailed violation reports
- Commander color identity analysis
- Deck statistics and composition

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
- **Current as of November 2025**
- Format-specific banned/restricted lists
- Set legality by format (970 paper-playable sets)
- Promo card legality across all formats
- Un-set and specialty product rules
- Excludes digital-only Arena cards (Alchemy rebalances, Historic Anthology)

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
- **Last Updated**: November 3, 2025
- **Rules Version**: Comprehensive Rules effective July 25, 2025
- **Card Database**: 970 paper-playable sets from Limited Edition Alpha (1993) through Edge of Eternities (2025)
- **Database Coverage**: Complete Modern, Legacy, Vintage, Pioneer, Standard, plus all Commander products, tokens, promos, and supplemental releases
- **Excluded**: Digital-only Arena sets (Alchemy, Historic Anthology, Arena Anthology)
- **Format Coverage**: Complete Modern (2003+), extensive Legacy/Vintage, current Standard, all Commander products

## Complete Set Database with Release Dates

**Note**: This repository contains **970 complete paper-playable MTG sets** spanning from Limited Edition Alpha (1993) through Edge of Eternities (2025). Below are highlighted examples of major sets included. For the complete list, see `card-library/mtg_sets.txt`.

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

### Supplemental Sets (2020-2025):
- **Murders at Karlov Manor Commander (MKC)** - February 9, 2024
- **Modern Horizons 3 (MH3)** - June 14, 2024
- **The Lord of the Rings: Tales of Middle-earth (LTR)** - June 23, 2023
- **Fallout (PIP)** - March 8, 2024
- **Ravnica Remastered (RVR)** - January 12, 2024
- **Commander Legends (CMR)** - November 20, 2020
- **Innistrad: Crimson Vow (VOW)** - November 19, 2021
- **Innistrad Remastered (INR)** - January 24, 2025

### Historic Standard Sets:
- **Kamigawa: Neon Dynasty (NEO)** - February 18, 2022
- **Kaldheim (KHM)** - February 5, 2021
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
- **Amonkhet Remastered (AKR)**, **Kaladesh Remastered (KLR)**, **Dominaria Remastered (DMR)**

### Comprehensive Database Coverage:
The card library includes **all paper Magic sets**, including:
- **All Standard-legal sets** from Alpha through current releases
- **All Modern-legal sets** (2003-present): Complete Mirrodin through Edge of Eternities
- **Legacy/Vintage staples**: Power Nine, Reserved List cards, dual lands, and classic sets
- **Commander products**: Every Commander precon release, Anthology sets, and Commander Legends
- **Supplemental sets**: Conspiracy, Battlebond, Modern Horizons series, Universes Beyond
- **Tokens and emblems**: Complete token sets for every major release
- **Promotional cards**: Judge Gifts, FNM Promos, Arena League, Grand Prix, MagicFest
- **Special editions**: Secret Lair, Collector's Edition, 30th Anniversary
- **Historic releases**: Chronicles, Anthologies, Duel Decks, From the Vault
- **Crossover sets**: Lord of the Rings, Doctor Who, Fallout, Warhammer 40K, Assassin's Creed, Marvel, TMNT, Avatar

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

1. **For format questions**: ✅ Reference `formats/formats.md` for complete format specifications
2. **For card searches**: ✅ Search `card-library/` directories for specific cards using `scripts/search_cards.py`
3. **For Standard legality**: ✅ Check current Standard sets list and `card-library/` contents
4. **For banned/restricted lists**: ✅ Reference `formats/banned-restricted.md`
5. **For rules questions**: ✅ Reference `rules/comprehensive-rules-summary.md` and `rulings/common-interactions.md` (planned)
6. **For tournament questions**: 📋 Reference `rules/tournament-procedures.md` (planned)
7. **For deck analysis**: 📋 Use templates in `tools/deck-analysis-tools.md` (planned)

## Commander Deck Building Guidelines

**CRITICAL: When recommending cards for Commander decks, ALWAYS respect color identity restrictions:**

- Only cards matching the commander's color identity can be included in the deck
- Color identity includes mana symbols in casting cost, rules text, and reminder text
- Colorless cards can be included in any Commander deck

**For complete color identity reference, see:** `formats/commander-color-identity.md`

**Quick Examples:**
- **Dimir Commander (UB)**: Only Blue, Black, and colorless cards
- **Naya Commander (RGW)**: Only Red, Green, White, and colorless cards  
- **Four-Color Commander (WUBG)**: Only White, Blue, Black, Green, and colorless cards
- **Five-Color Commander (WUBRG)**: All colors and colorless cards allowed

**When building Commander decks:**
1. First identify the commander's color identity using `formats/commander-color-identity.md`
2. Only search for and recommend cards within those colors
3. Focus on colorless utility when color restrictions are tight
4. Never recommend cards outside the commander's color identity

Remember: This repository aims to eliminate the need for web searches on common MTG questions by providing comprehensive, current, and well-organized reference materials.