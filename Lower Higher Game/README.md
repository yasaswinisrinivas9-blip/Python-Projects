# Higher Lower Game

## Description

A command-line implementation of the **Higher Lower Game** built using Python.

The player is presented with two public figures, brands, or organizations and must guess which one has more social media followers.

The game continues until the player makes an incorrect guess.

---

## Features

- Random account selection
- Follower count comparison
- Score tracking
- Continuous gameplay
- Randomized game data
- ASCII art interface

---

## How It Works

1. Randomly select two accounts.
2. Display their names, descriptions, and countries.
3. Ask the player to guess which account has more followers.
4. Compare the follower counts.
5. If the answer is correct:
   - Increase the score.
   - Continue to the next round.
6. Otherwise:
   - Display the final score.
   - End the game.

---

## Example

```text
Compare A:
Cristiano Ronaldo, a Footballer, from Portugal

VS

Against B:
Taylor Swift, a Singer, from United States

Who has more followers?
A

You're right!
Current score: 1
```

---

## Concepts Used

- Functions
- Dictionaries
- Lists
- Random Module
- Loops
- Conditional Statements
- User Input
- Game Logic

---

## Project Structure

```
Higher-Lower-Game
│
├── main.py
├── art.py
├── game_data.py
└── README.md
```

---

## Time Complexity

**O(R)**

Where **R** is the number of rounds played.

Each round performs a constant amount of work.

---

## Space Complexity

**O(1)**

The program uses a fixed amount of extra memory apart from the provided game dataset.

---

## Learning Outcome

This project demonstrates:

- Working with lists of dictionaries
- Accessing nested dictionary values
- Designing reusable functions
- Building interactive command-line games
- Managing game state with loops
- Using randomization effectively