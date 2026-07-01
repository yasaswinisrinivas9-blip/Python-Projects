# Caesar Cipher

## Description

A Python implementation of the classical **Caesar Cipher**, one of the earliest and simplest encryption techniques.

The program allows users to:

* Encrypt a message
* Decrypt a message
* Restart the program multiple times
* Preserve spaces, numbers, and special characters

---

## Features

* Encrypt text using a shift value
* Decrypt encrypted messages
* Supports repeated execution
* Handles uppercase and lowercase letters
* Preserves non-alphabetic characters

---

## How It Works

The Caesar Cipher shifts each alphabet character by a fixed number of positions.

For example, with a shift of **3**:

```text
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

During decryption, the shift is applied in the opposite direction.

---

## Example

### Encrypt

```text
Input Message:
hello

Shift:
5

Output:
mjqqt
```

### Decrypt

```text
Input Message:
mjqqt

Shift:
5

Output:
hello
```

---

## Concepts Used

* Strings
* Lists
* Loops
* Functions
* Conditional Statements
* Modular Arithmetic
* User Input Validation

---

## Time Complexity

**O(N)**

Where **N** is the length of the message.

---

## Space Complexity

**O(N)**

A new encrypted/decrypted string is created.

---

## Learning Outcome

This project demonstrates:

* Classical encryption techniques
* Character manipulation
* Function decomposition
* Modular arithmetic
* Building interactive command-line applications
