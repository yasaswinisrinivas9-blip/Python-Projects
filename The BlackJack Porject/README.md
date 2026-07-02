# Blackjack

## Description

A command-line implementation of the classic **Blackjack (21)** card game built using Python.

The game allows a player to compete against the computer by drawing cards, calculating scores, and determining the winner based on standard Blackjack rules.

---

## Features

- Random card dealing
- Blackjack detection
- Ace value adjustment (11 → 1)
- Player hit or stand
- Computer dealer logic
- Winner determination
- Replay the game without restarting

---

## Game Rules

- Both the player and the dealer receive two cards initially.
- Face cards (Jack, Queen, King) are worth **10**.
- An Ace can be worth **11** or **1** depending on the total score.
- A Blackjack is an Ace and a 10-value card as the first two cards.
- The player can choose to:
  - Hit (draw another card)
  - Stand (end their turn)
- The dealer continues drawing cards according to the game logic.
- The player closest to **21** without exceeding it wins.

---

## Example

```text
Your cards: [10, 8], current score: 18
Computer's first card: 9

Type 'y' to get another card, type 'n' to pass:
n

User's final hand: [10, 8], final score: 18
Computer's final hand: [9, 7, 2], final score: 18

Draw 🙃
```

---

## Concepts Used

- Functions
- Lists
- Loops
- Conditional Statements
- Random Module
- Recursion
- Game Logic
- Score Calculation

---

## Project Structure

```
Blackjack
│
├── main.py
├── art.py
└── README.md
```

---

## Time Complexity

**O(N)**

Where **N** is the number of cards drawn during a game.

---

## Space Complexity

**O(N)**

The player's and dealer's hands grow dynamically as cards are drawn.

---

## Learning Outcome

This project demonstrates:

- Building a complete command-line game
- Implementing game rules using Python
- Managing game state with loops and functions
- Working with lists and randomization
- Handling user interaction and decision-making