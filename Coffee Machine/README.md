# Coffee Machine

## Description

A command-line simulation of a coffee vending machine built with Python.

The program allows users to purchase different coffee beverages, processes coin payments, checks ingredient availability, updates resources, and generates reports.

---

## Features

- Order Espresso, Latte, or Cappuccino
- Resource availability check
- Coin payment system
- Change calculation
- Resource deduction after purchase
- Sales reporting
- Machine shutdown option

---

## Menu

| Drink | Water | Milk | Coffee | Cost |
|-------|------:|-----:|-------:|-----:|
| Espresso | 50 ml | 0 ml | 18 g | $1.50 |
| Latte | 200 ml | 150 ml | 24 g | $2.50 |
| Cappuccino | 250 ml | 100 ml | 24 g | $3.00 |

---

## How It Works

1. Display the available coffee options.
2. Accept the user's drink selection.
3. Check whether sufficient resources are available.
4. Prompt the user to insert coins.
5. Calculate the total payment.
6. Verify whether the payment is sufficient.
7. Return change if necessary.
8. Deduct the required ingredients.
9. Serve the selected coffee.

---

## Example

```text
Welcome to the Coffee Machine!

Available Drinks:
- Espresso
- Latte
- Cappuccino

What would you like?
latte

Please insert coins.

How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0

Here is $0.00 in change.

Here is your latte ☕. Enjoy!
```

---

## Concepts Used

- Functions
- Dictionaries
- Nested Dictionaries
- Loops
- Conditional Statements
- User Input
- Variables
- Resource Management

---

## Project Structure

```
Coffee-Machine
│
├── main.py
├── art.py
└── README.md
```

---

## Time Complexity

**O(1)**

Each operation (resource check, payment calculation, and coffee preparation) processes a fixed amount of data.

---

## Space Complexity

**O(1)**

Only predefined dictionaries and a fixed number of variables are used.

---

## Learning Outcome

This project demonstrates:

- Building a complete command-line application
- Managing resources using dictionaries
- Simulating real-world systems
- Processing monetary transactions
- Writing modular functions
- Organizing application logic effectively