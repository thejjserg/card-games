# Card Game Probability Tools

A collection of probability calculators, simulations, and analysis scripts for various card games I enjoy playing — including **Yu-Gi-Oh!**, **Lorcana**, **Poker**, **Blackjack**, and more.  
Each project is built with Python and focuses on answering real in-game questions, estimating odds, and giving practical insights for deck building, play decisions, and strategy.

---

## 📌 Current Projects

### 1. Lorcana – Ally Hit Odds Calculator
**Script:** `lorcana_ally_odds.py`  

In Lorcana, some cards allow you to **look at the top N cards of your deck and pick certain types** (e.g., "Ally" characters). This script calculates the exact probability of hitting at least one Ally given:
- Total cards left in the deck
- Number of Allies left
- Number of cards you look at (default = 3)

**Key Features:**
- Uses **Hypergeometric Probability** for exact calculations  
- Works interactively from the command line  
- Also displays the full probability distribution (0, 1, 2, … Allies found)  
- Handles any deck size and card type counts (not just Lorcana Allies)

**Example Run:**
