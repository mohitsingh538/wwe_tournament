
# WWE Tournament Simulator

## Overview

The **WWE Tournament Simulator** is a Python-based simulation that replicates the intensity and excitement of a WWE wrestling tournament. It allows players to engage in various match types like 1v1 and triple-threat matches. The simulator determines the outcome of matches, replenishes energy for players during the match, and generates victory messages based on the players' performances.

The tournament begins with multiple 1v1 matches, followed by a series of triple-threat matches, and culminates in the grand finale. Players are randomly selected to compete in each round, with energy replenishments and damage dealt through punches.

---

## Features

- **Wrestling Tournament Simulation**: Simulates WWE-style wrestling tournaments where players compete in different rounds to emerge victorious.
  
- **Dynamic Player Interaction**: Players can replenish their energy, get punched, and unleash their finishing moves on opponents.

- **Victory Messages**: A random victory message is generated for each winner, highlighting their performance and finishing move.

- **Match Types**: The simulator supports `1v1` and `triple-threat` match types, and ensures an exciting progression through the tournament stages.

- **Wild Card Entries**: Adds an unpredictable element to the tournament with wild card entries in the semifinals.

---

## Getting Started

### Prerequisites

- Python 3.x
- `pip` (Python package manager)

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/wwe-tournament-simulator.git
   cd wwe-tournament-simulator
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the simulation:
   ```bash
   python main.py
   ```

---

## How It Works

### Player Class

The `Player` class represents a wrestler. Each player has:
- `name`: The name of the player (e.g., "Brock Lesnar").
- `energy`: The current energy level of the player.
- `finishing_move`: The player's signature finishing move (e.g., "F-5").

Players can replenish their energy during the match and lose energy when punched.

### Match Class

The `Match` class represents a match between players. It handles:
- **Match Types**: Supports 1v1 and triple-threat matches.
- **Punches**: Players are randomly punched during the match, causing them to lose energy.
- **Victory Messages**: After the match ends, a victory message is generated based on the player's energy and finishing move.
- **Match Duration**: The match runs for 30 seconds, simulating an intense, fast-paced match.

### TournamentOrchestrator Class

The `TournamentOrchestrator` class manages the tournament:
- **First Round**: Conducts 1v1 matches between players.
- **Triple Threat Round**: Conducts triple-threat matches with winners from the first round.
- **Semifinals**: Conducts two semifinal matches to determine the finalists.
- **Grand Finale**: The final match to determine the WWE champion.
- **Wild Card Entries**: Adds wild card players to the tournament if necessary.

---

## Example Tournament Flow

1. **First Round (1v1 Matches)**: The tournament begins with 1v1 matches between the players.
2. **Triple Threat Round**: The winners from the first round compete in triple-threat matches.
3. **Semifinals**: The winners from the triple-threat round face off in the semifinals.
4. **Grand Finale**: The final two wrestlers compete for the WWE Championship.

---

## Sample Output

Here is a sample output from the simulation:

```
=== FIRST ROUND (1v1 Matches) ===
🔥 SINGLES MATCH: Brock Lesnar (80) vs John Cena (75) 🔥
🥊 John Cena got punched! (-30)   |   ⚡ 45
🥊 Brock Lesnar got punched! (-25)   |   ⚡ 55
...
💥 Brock Lesnar (⚡ 60) obliterates John Cena with a killer F-5!
⏱️ Match Duration: 14.7832 seconds

=== TRIPLE THREAT ROUND ===
🔥 TRIPLE THREAT MATCH: Brock Lesnar (60) vs Kurt Angle (40) vs The Undertaker (80) 🔥
🥊 Kurt Angle got punched! (-15)   |   ⚡ 25
🥊 Brock Lesnar got punched! (-40)   |   ⚡ 20
...
💥 The Undertaker (⚡ 85) crushes Brock Lesnar and Kurt Angle with the unstoppable Tombstone Piledriver!
⏱️ Match Duration: 22.0154 seconds

=== GRAND FINALE ===
🔥 GRAND FINALE: The Undertaker (85) vs Seth Rollins (90) 🔥
🥊 Seth Rollins got punched! (-50)   |   ⚡ 40
🥊 The Undertaker got punched! (-30)   |   ⚡ 55
...
💥 The Undertaker (⚡ 80) finishes Seth Rollins with a thunderous Tombstone Piledriver!
⏱️ Match Duration: 25.6179 seconds

🏆 NEW WWE CHAMPION: The Undertaker (⚡ 80) 🏆
The new champion celebrates victory with a final Tombstone Piledriver!
```

---
