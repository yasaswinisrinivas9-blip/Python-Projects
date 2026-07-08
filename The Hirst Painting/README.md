# Hirst Painting

## Description

A Python application that recreates a **Hirst-style dot painting** using the Turtle graphics library.

The program generates a 10 × 10 grid of colorful dots by randomly selecting colors from a predefined RGB palette.

---

## Features

- Generates a 10 × 10 dot grid
- Random color selection
- Uses RGB color mode
- Turtle graphics visualization
- Fast drawing using hidden turtle
- Automatic positioning for each row

---

## Project Structure

```
Hirst-Painting
│
├── main.py
└── README.md
```

---

## How It Works

1. Configure Turtle to use RGB colors.
2. Create and configure the turtle.
3. Move the turtle to the starting position.
4. Store a predefined list of RGB colors.
5. Draw one colored dot at a time.
6. Move forward after each dot.
7. After every 10 dots:
   - Move up one row.
   - Return to the left side.
8. Continue until all 100 dots are drawn.

---

## Example

The program creates a painting similar to:

```
● ● ● ● ● ● ● ● ● ●

● ● ● ● ● ● ● ● ● ●

● ● ● ● ● ● ● ● ● ●

...

(100 colorful dots)
```

Each dot is randomly selected from the predefined color palette.

---

## Concepts Used

- Turtle Graphics
- RGB Color Mode
- Loops
- Random Module
- Lists
- Coordinates
- Pen Control

---

## Time Complexity

**O(N)**

Where **N** is the total number of dots drawn.

For this project:

```
N = 100
```

---

## Space Complexity

**O(1)**

Only a fixed color list and a few variables are used.

---

## Learning Outcome

This project demonstrates:

- Drawing graphics using Python Turtle
- Working with RGB colors
- Random color generation
- Coordinate-based movement
- Automating repetitive drawing tasks
- Building graphical Python applications