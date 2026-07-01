# Secret Auction Program

## Description

A command-line Python application that simulates a **secret auction**.

Multiple participants can place their bids without seeing previous bids. Once all participants have submitted their bids, the program determines and announces the highest bidder.

---

## Features

- Accepts multiple bidders
- Stores bidder names and bid amounts using a dictionary
- Determines the highest bidder automatically
- Clears the screen between bidders to maintain bid privacy
- Displays the winner and highest bid

---

## How It Works

1. Ask the user for their name.
2. Ask for their bid amount.
3. Store the bid in a dictionary.
4. Ask whether there are more bidders.
5. Repeat until there are no more bidders.
6. Traverse the dictionary to find the highest bid.
7. Display the winner.

---

## Example

```text
What is your name?: Alice
What is your bid?: $150
Are there any other bidders? yes

What is your name?: Bob
What is your bid?: $220
Are there any other bidders? yes

What is your name?: Charlie
What is your bid?: $180
Are there any other bidders? no

The winner is Bob with the highest bid of $220
```

---

## Concepts Used

- Dictionaries
- Functions
- Loops
- Conditional Statements
- User Input
- Variables
- Traversing Dictionaries

---

## Time Complexity

**O(N)**

Where **N** is the number of bidders.

The dictionary is traversed once to determine the highest bid.

---

## Space Complexity

**O(N)**

A dictionary stores all bidder names and their corresponding bid amounts.

---

## Learning Outcome

This project demonstrates:

- Working with Python dictionaries
- Creating reusable functions
- Finding the maximum value in a dictionary
- Building interactive command-line applications
- Separating logic into modular functions