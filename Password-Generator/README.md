# Password Generator

## Description

A Python application that generates secure passwords based on user-defined requirements.

Users can choose the number of:

* Letters
* Symbols
* Numbers

The project contains two implementations that demonstrate different approaches to password generation.

---

## Project Structure

```text
Password-Generator
│
├── Easy
│   └── main.py
│
├── Hard
│   └── main.py
│
└── README.md
```

---

## Easy Version

The easy version generates the password by appending characters in the following order:

1. Letters
2. Symbols
3. Numbers

### Example

```text
Letters: 4
Symbols: 2
Numbers: 2

Output:
abCD!@12
```

The password follows a fixed pattern and is easier to understand for beginners.

---

## Hard Version

The hard version first collects all selected characters and then randomly shuffles them before generating the final password.

### Example

```text
Letters: 4
Symbols: 2
Numbers: 2

Output:
2@Ca!Db1
```

This produces a more secure and unpredictable password.

---

## Concepts Used

* Variables
* Lists
* Loops
* Random Module
* List Operations
* String Manipulation
* List Shuffling

---

## Time Complexity

**O(L + S + N)**

Where:

* **L** = Number of letters
* **S** = Number of symbols
* **N** = Number of numbers

---

## Space Complexity

**O(L + S + N)**

The generated password characters are stored before forming the final string.

---

## Learning Outcome

This project demonstrates:

* Random password generation
* Difference between ordered and shuffled outputs
* Using Python lists effectively
* Improving security through randomization
* Writing modular and readable Python code
