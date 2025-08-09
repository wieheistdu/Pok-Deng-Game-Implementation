# Pok-Deng Game

A simple command-line **Pok-Deng** (ป๊อกเด้ง) game implemented in `Python`. 
___ 
Game Rules:
- Player places a bet (e.g., 5 chips).
- Dealer shuffles a standard 52-card deck.
- *Player* gets the **first two cards**, while *the dealer* gets **the last two**.
- Card values:
  - Ace = **1 point**
  - Cards **2–9** = their face values
  - King, Queen, Jack, and 10 = **0 points**
- Scores:
    - Calculated as the sum of card values modulo 10 (units digit). *This will make the values ranging from 0-9*
    - **Win:** You beat the dealer and receive a payout equal to your original bet.
    - **Tie:** You neither win nor lose chips to the dealer.
    - **Lose:** You forfeit your bet to the dealer.
---

## Requirements
- Python 3.8 or later  
- No external libraries required (uses Python standard library only (`random`)).

---

## Installation & Running

1. **Git Clone or download** this repository.
2. **(Optional)** Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
