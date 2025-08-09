#  ♦️ Pok-Deng Game

A simple command-line **Pok-Deng** (ป๊อกเด้ง) game implemented in `Python`. 

## Game Rules:
- Player places a bet (e.g., 5 chips).
- Dealer shuffles a standard 52-card deck.
- *Player* gets the **first two cards**, while *the dealer* gets **the last two**.
- Card values:
  - Ace = **1 point**
  - Cards **2–9** = their face values
  - King, Queen, Jack, and 10 = **0 points**

## Scores:
  - Calculated as the sum of card values modulo 10 (units digit). *This will make the values ranging from 0-9*
  - **Win:** You beat the dealer and receive a payout equal to your original bet.
  - **Tie:** You neither win nor lose chips to the dealer.
  - **Lose:** You forfeit your bet to the dealer.
---

## Requirements
- **Python**: 3.8 or later  
- **Dependencies**: No external libraries required (uses Python standard library only (`random`)).
- Since this game uses only basic libraries, **creating a virtual environment is optional**.

---

## Installation & Running
1. **Git Clone or download** this repository.
   ```bash
   git clone https://github.com/wieheistdu/Pok-Deng-Game-Implementation.git

2. CD into the folder
   ```bash
   cd Pok-Deng-Game-Implementation

3. Run the Python code
   ```bash
   python pok-deng.py

## Examples of the output are as followed:
  **A Win**
  ```bash
  > npm start
  > Please put your bet
  > 5
  > You got Clubs-5, Clubs-4
  > The dealer got Clubs-2, Clubs-9
  > You won!!!, received 5 chips
  > Wanna play more (Yes/No)?
  > No
  > You got total 5 chips
  ```
  
  **A Tie**
  ```bash
  > npm start
  > Please put your bet
  > 5
  > You got Clubs-2, Spades-Queen
  > The dealer got Clubs-9, Diamonds-3
  > Tie, no chips exchanged
  > Wanna play more (Yes/No)?
  > No
  > You got total 0 chips
  ```
  
  **A Lose**
  ```bash
  > npm start
  > Please put your bet
  > 4
  > You got Clubs-9, Diamonds-Ace
  > The dealer got Hearts-3, Clubs-3
  > You lost..., paid 4 chips
  > Wanna play more (Yes/No)?
  > No
  > You got total -4 chips
  ```
*You can keep playing this game by typing "Yes".*
