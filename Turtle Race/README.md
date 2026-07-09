# Turtle Race

## Description

A Python Turtle Graphics application that simulates a turtle race.

The player places a bet on which colored turtle will win. Six turtles race across the screen with randomly generated movement, making every race unique.

---

## Features

- Six colorful racing turtles
- User betting system
- Randomized turtle movement
- Winner detection
- Interactive graphical interface
- Race result announcement

---

## Project Structure

```
Turtle-Race
│
├── main.py
└── README.md
```

---

## How It Works

1. Create six turtles with different colors.
2. Position each turtle at the starting line.
3. Ask the user to bet on a turtle color.
4. Start the race.
5. Each turtle moves forward by a random distance.
6. Continue until one turtle reaches the finish line.
7. Compare the winning turtle with the user's bet.
8. Display whether the user won or lost.

---

## Example

```text
Make your bet!

Which turtle will win the race?

Enter a color:
blue

🏁 Race Started...

Winner:
Green Turtle

You've lost! The green turtle has won the race!
```

---

## Concepts Used

- Turtle Graphics
- Random Module
- Loops
- Lists
- User Input
- Conditional Statements
- Coordinates
- Object-Oriented Programming (Turtle Objects)

---

## Time Complexity

**O(R × T)**

Where:

- **R** = Number of race iterations
- **T** = Number of turtles (6)

Since the number of turtles is fixed, the complexity is effectively **O(R)**.

---

## Space Complexity

**O(T)**

A list stores all turtle objects.

For this project:

```
T = 6
```

---

## Learning Outcome

This project demonstrates:

- Building graphical applications with Turtle Graphics
- Creating multiple objects using loops
- Simulating animations with random movement
- Handling user interaction
- Managing collections of objects
- Applying Object-Oriented Programming concepts