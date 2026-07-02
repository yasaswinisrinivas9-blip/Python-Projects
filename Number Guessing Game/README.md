# Number Guessing Game

## Description

A command-line Python game where the player attempts to guess a randomly generated number between **1 and 100**.

The game provides feedback after each guess and offers two difficulty levels with different numbers of attempts.

---

## Features

- Random number generation
- Easy and Hard difficulty modes
- Limited number of attempts
- Hint system ("Too High" / "Too Low")
- Win/Lose conditions
- Interactive command-line gameplay

---

## Difficulty Levels

| Difficulty | Attempts |
|------------|----------|
| Easy | 10 |
| Hard | 5 |

---

## How It Works

1. The computer randomly selects a number between **1 and 100**.
2. The player chooses a difficulty level.
3. The player enters a guess.
4. The program provides feedback:
   - Too High
   - Too Low
   - Correct Guess
5. The remaining attempts decrease after every incorrect guess.
6. The game ends when:
   - The player guesses the correct number.
   - The player runs out of attempts.

---

## Example

```text
Welcome to the Number Guessing Game!

I'm thinking of a number between 1 and 100.

Choose a difficulty. Type 'easy' or 'hard':
easy

You have 10 attempts remaining.

Make a guess:
50

Too High!

Guess again.

You have 9 attempts remaining.
```

---

## Concepts Used

- Functions
- Loops
- Conditional Statements
- Random Module
- Variables
- User Input
- Constants
- Return Values

---

## Project Structure

```
Number-Guessing-Game
│
├── main.py
├── art.py
└── README.md
```

---

## Time Complexity

**O(T)**

Where **T** is the number of guesses made by the player.

In the worst case:

- Easy Mode → **O(10)**
- Hard Mode → **O(5)**

Since the number of attempts is fixed, the complexity is effectively **O(1)**.

---

## Space Complexity

**O(1)**

The program uses only a fixed number of variables regardless of the number of guesses.

---

## Learning Outcome

This project demonstrates:

- Building an interactive command-line game
- Using random number generation
- Designing reusable functions
- Managing game state with loops
- Implementing difficulty levels
- Handling user input and validation