# Comprehensive Rules Summary

**Last Updated**: September 13, 2025
**Rules Version**: Comprehensive Rules effective July 25, 2025

This document provides a focused summary of Magic: The Gathering's Comprehensive Rules, emphasizing areas most relevant for competitive play and complex interactions.

## Table of Contents
1. [Game Structure](#game-structure)
2. [Turn Structure and Phases](#turn-structure-and-phases)
3. [Priority and Timing](#priority-and-timing)
4. [The Stack](#the-stack)
5. [State-Based Actions](#state-based-actions)
6. [Layers and Continuous Effects](#layers-and-continuous-effects)
7. [Replacement and Prevention Effects](#replacement-and-prevention-effects)
8. [Card Types and Zones](#card-types-and-zones)
9. [Combat Rules](#combat-rules)
10. [Damage and Life Loss](#damage-and-life-loss)
11. [Mana and Mana Abilities](#mana-and-mana-abilities)
12. [Keywords and Abilities](#keywords-and-abilities)

---

## Game Structure

### Basic Game Concepts
- **Life Total**: Players start at 20 life (Commander: 40 life)
- **Hand Size**: 7-card starting hand, maximum hand size 7
- **Library**: Deck of cards a player draws from
- **Graveyard**: Discard pile for used/destroyed cards
- **Battlefield**: Where permanents exist and interact
- **Exile Zone**: Cards removed from the game temporarily or permanently

### Winning and Losing
Players lose the game if:
- Life total reaches 0 or less
- Attempt to draw from an empty library
- Have 10+ poison counters
- Specific card effects (e.g., Door to Nothingness)

### Zones
1. **Library** - Face-down deck
2. **Hand** - Cards held by player
3. **Battlefield** - Where permanents exist
4. **Graveyard** - Discard pile
5. **Stack** - Where spells and abilities wait to resolve
6. **Exile** - Removed from game zone
7. **Command Zone** - Emblems, commanders, conspiracies

---

## Turn Structure and Phases

### Turn Phases (in order):
1. **Beginning Phase**
   - Untap Step: Untap permanents
   - Upkeep Step: Upkeep triggers occur
   - Draw Step: Draw a card

2. **First Main Phase**
   - Play lands, cast spells, activate abilities

3. **Combat Phase**
   - Beginning of Combat Step
   - Declare Attackers Step
   - Declare Blockers Step
   - Combat Damage Step
   - End of Combat Step

4. **Second Main Phase**
   - Play lands, cast spells, activate abilities

5. **Ending Phase**
   - End Step: "At end of turn" triggers
   - Cleanup Step: Discard to hand size, damage wears off

### Key Rules:
- **Sorcery Speed**: Main phases only, when stack is empty
- **Instant Speed**: Any time you have priority
- **Land Drop**: One per turn, main phases only (unless otherwise specified)

---

## Priority and Timing

### Priority System
- **Active Player, Non-Active Player (APNAP)**: Order of priority passing
- Players receive priority in APNAP order
- Must pass priority consecutively for spell/ability to resolve
- Passing priority with empty stack moves to next phase/step

### When Players Get Priority:
1. After each spell or ability is put on the stack
2. After each spell or ability resolves
3. At the beginning of each phase and step
4. When state-based actions are performed
5. When triggered abilities are put on the stack

### Special Cases:
- **Mana Abilities**: Don't use the stack, resolve immediately
- **Static Abilities**: Always active, don't use the stack
- **Triggered Abilities**: Use the stack, can be responded to

---

## The Stack

### Stack Rules:
- **LIFO**: Last In, First Out (resolves in reverse order)
- Players can respond to spells/abilities on the stack
- Targets are chosen when spell/ability is put on the stack
- Legality of targets checked on resolution

### What Uses the Stack:
- Spells (except mana abilities)
- Activated abilities (except mana abilities)
- Triggered abilities

### What Doesn't Use the Stack:
- Static abilities
- Mana abilities
- Special actions (playing lands, turning face-down creatures face up)

### Resolution:
1. Check if spell/ability is still legal (targets, etc.)
2. If illegal, it's countered and removed from stack
3. If legal, resolve the effect
4. Active player gets priority

---

## State-Based Actions

State-based actions are checked immediately whenever a player receives priority and are performed simultaneously if multiple apply.

### Common State-Based Actions:
1. **Player with 0 or less life loses**
2. **Player with 10+ poison counters loses**
3. **Player drawing from empty library loses**
4. **Creature with damage ≥ toughness is destroyed**
5. **Creature with 0 or less toughness is put into graveyard**
6. **Planeswalker with 0 loyalty is put into graveyard**
7. **Two+ legendary permanents with same name - choose one to keep**
8. **Auras with illegal/no targets are put into graveyards**
9. **Equipment/Fortifications attached to illegal permanents become unattached**
10. **Counters on permanents that can't have them are removed**

### Timing:
- Checked before triggered abilities are put on the stack
- Performed as many times as necessary until none apply
- Cannot be responded to

---

## Layers and Continuous Effects

The layer system determines how continuous effects interact. Effects are applied in layer order:

### Layer 1: Rules and Effects that Change Types
- Copy effects
- Effects that change card types

### Layer 2: Control-Changing Effects
- Gain/lose control of permanents

### Layer 3: Text-Changing Effects
- Effects that add or remove abilities

### Layer 4: Type-Changing Effects
- Effects that change types without changing rules text

### Layer 5: Color-Changing Effects
- Effects that change or add colors

### Layer 6: Ability-Adding/Removing Effects
- Effects that grant or remove abilities

### Layer 7: Power/Toughness Effects
- **7a**: Characteristic-defining abilities
- **7b**: Effects that set P/T to specific values
- **7c**: Effects that modify P/T (+X/+X, etc.)
- **7d**: Counters
- **7e**: Effects that switch P/T

### Dependency Rules:
- If Effect A depends on Effect B, apply B first
- Timestamp order breaks ties within layers
- Some effects create dependencies between layers

---

## Replacement and Prevention Effects

### Replacement Effects:
- **Format**: "If [event], [effect] instead" or "As [event], [effect]"
- Replace one event with another
- Applied before the event would occur
- Can only apply once to any given event

### Prevention Effects:
- **Format**: "Prevent [damage/effect]"
- Stop something from happening
- Applied as the event would occur
- Can prevent multiple instances

### Self-Replacement Rule:
- Replacement effects can't replace themselves
- Example: If a replacement effect causes the same event it's replacing, it won't apply again

### Multiple Replacement Effects:
- Controller of affected object chooses order
- If no controller, affected player chooses
- Each can only apply once per event

---

## Card Types and Zones

### Permanent Types:
- **Artifact**: Represents magical items
- **Creature**: Has power, toughness, can attack/block
- **Enchantment**: Ongoing magical effects
- **Land**: Produces mana, usually
- **Planeswalker**: Has loyalty, can be attacked
- **Battle**: Has defense, can be attacked

### Non-Permanent Types:
- **Instant**: Resolves immediately
- **Sorcery**: Main phase only, resolves immediately
- **Tribal**: Shares creature types (mostly obsolete)

### Supertypes:
- **Basic**: Basic lands
- **Legendary**: "Legendary rule" applies
- **Snow**: For snow-based effects
- **World**: Obsolete supertype

---

## Combat Rules

### Combat Phase Steps:

#### 1. Beginning of Combat
- Triggered abilities trigger
- Players can cast spells/activate abilities

#### 2. Declare Attackers
- **Active player declares attackers**
- Attacking creatures become tapped (unless vigilance)
- Choose what each attacker attacks (player/planeswalker/battle)
- Triggered abilities trigger
- Players can respond

#### 3. Declare Blockers
- **Defending player declares blockers**
- Each blocker can block one attacker (unless otherwise specified)
- Multiple creatures can block the same attacker
- Triggered abilities trigger
- Players can respond

#### 4. Combat Damage
- **Assign damage in APNAP order**
- For blocked attackers: assign damage to blockers first
- Excess damage can "trample" through
- All combat damage dealt simultaneously
- Players can respond after damage

#### 5. End of Combat
- Remove creatures from combat
- "At end of combat" triggers occur

### Key Combat Rules:
- **Can't Attack**: Summoning sick, tapped, specific restrictions
- **Must Attack**: Some creatures have forced attack requirements
- **Trample**: Excess damage goes through
- **Flying**: Can only be blocked by flying/reach creatures
- **First Strike**: Deals damage in separate step
- **Double Strike**: Deals damage in both first strike and regular steps

---

## Damage and Life Loss

### Types of Damage:
- **Combat Damage**: From attacking/blocking creatures
- **Non-Combat Damage**: From spells, abilities, other sources

### Damage Rules:
- Damage doesn't lower toughness, it's marked on the creature
- Damage marked ≥ toughness destroys the creature (state-based action)
- Damage to players causes life loss
- Damage wears off during cleanup step

### Life Loss vs. Damage:
- **Life Loss**: Directly reduces life total, can't be prevented as damage
- **Damage**: Can be prevented, redirected, or modified by damage-affecting effects

### Deathtouch:
- Any amount of damage from deathtouch source destroys creature
- Applies to combat and non-combat damage

---

## Mana and Mana Abilities

### Mana Rules:
- **Mana Pool**: Temporary storage for mana
- **Mana Burn**: No longer exists (removed in 2010)
- **Emptying**: Mana pools empty at end of each phase/step
- **Floating Mana**: Mana in pool that hasn't been spent

### Mana Abilities:
- **Don't use the stack**
- **Resolve immediately**
- **Can't be responded to**
- **Can be activated while other spells/abilities are resolving**

### Criteria for Mana Abilities:
1. Activated ability that adds mana to mana pool
2. Doesn't target
3. Isn't a loyalty ability

### Color Identity (Commander):
- Mana symbols anywhere on the card determine color identity
- Includes mana costs, rules text, reminder text
- Excludes mana symbols in names/flavor text

---

## Keywords and Abilities

### Evergreen Keywords:
- **Flying**: Can only be blocked by creatures with flying or reach
- **First Strike**: Deals combat damage before normal damage
- **Double Strike**: Deals first strike and normal combat damage
- **Deathtouch**: Any damage destroys creature
- **Haste**: Can attack and use tap abilities immediately
- **Hexproof**: Can't be targeted by opponents' spells/abilities
- **Indestructible**: Can't be destroyed by damage or "destroy" effects
- **Lifelink**: Damage dealt gains you that much life
- **Menace**: Can't be blocked except by 2+ creatures
- **Reach**: Can block flying creatures
- **Trample**: Excess combat damage goes to defending player
- **Vigilance**: Doesn't tap when attacking
- **Ward**: Opponents pay cost or spell/ability targeting this is countered

### Common Mechanics:
- **Activated Abilities**: "[Cost]: [Effect]"
- **Triggered Abilities**: "When/Whenever/At [trigger], [effect]"
- **Static Abilities**: Continuous effects while permanent is in play
- **Replacement Effects**: "If/Instead" effects
- **Prevention Effects**: "Prevent" effects

### Timing Restrictions:
- **Sorcery Speed**: Main phase, stack empty, your turn only
- **Instant Speed**: Any time you have priority
- **Special Actions**: Don't use stack (land drops, morph, etc.)

---

## Quick Reference Tables

### Priority Order:
1. Active Player (AP)
2. Non-Active Player in turn order (NAP)

### Stack Resolution:
1. Last In, First Out (LIFO)
2. Check legality on resolution
3. Resolve or counter if illegal

### State-Based Actions Check Points:
- Before triggered abilities go on stack
- When player receives priority
- Before moving to next phase/step

### Layer Application Order:
1. Copy effects → 2. Control → 3. Text changing → 4. Type changing → 5. Color → 6. Abilities → 7. Power/Toughness

---

## Common Rulings and Interactions

### Triggered Ability Timing:
- All triggered abilities from same event go on stack in APNAP order
- Controlled abilities can be ordered by controller
- Resolve in reverse order (stack = LIFO)

### Replacement Effect Priority:
- Controller of affected permanent chooses
- Self-replacement rule prevents infinite loops
- Can only apply once per event

### Mana Ability Special Rules:
- Can be played in response to mana abilities
- Can be played while spells are resolving
- Don't trigger abilities that trigger on "casting spells" or "activating abilities"

This summary covers the most essential rules for competitive Magic play. For complete and official rules, consult the official Comprehensive Rules document from Wizards of the Coast.