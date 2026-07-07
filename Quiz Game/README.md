# Quiz Game

## Description

A command-line Quiz Game built using Python and Object-Oriented Programming (OOP).

The application presents True/False questions to the player, evaluates each response, keeps track of the score, and displays the final result after all questions have been answered.

---

## Features

- Multiple-choice True/False questions
- Score tracking
- Object-Oriented Design
- Question bank management
- Immediate answer validation
- Final score summary

---

## Project Structure

```
Quiz-Game
│
├── main.py
├── question_model.py
├── quiz_brain.py
├── data.py
└── README.md
```

---

## How It Works

1. Load the quiz questions from `data.py`.
2. Convert each question into a `Question` object.
3. Store all questions in a question bank.
4. Create a `QuizBrain` object.
5. Display one question at a time.
6. Check whether the user's answer is correct.
7. Update the score.
8. Display the final score after all questions are completed.

---

## Example

```text
Q.1: A slug's blood is green.
(True/False): True

You got it right!
Current Score: 1/1

Q.2: The loudest animal is the African Elephant.
(True/False): False

Correct!

You've completed the quiz!
Your final score is: 9/10
```

---

## Concepts Used

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors
- Methods
- Lists
- Loops
- Conditional Statements
- Modules
- User Input

---

## Time Complexity

**O(N)**

Where **N** is the number of quiz questions.

Each question is processed exactly once.

---

## Space Complexity

**O(N)**

The question bank stores all quiz questions as objects.

---

## Learning Outcome

This project demonstrates:

- Designing applications using Object-Oriented Programming
- Creating and using custom classes
- Separating code into multiple modules
- Managing application state through objects
- Building an interactive command-line quiz application