# Password Strength Checker 🔐

A simple Python program built as **Project 1** of the DecodeLabs Cyber Security Industrial Training Kit (Batch 2026).

## About

This program checks whether a password is **Weak**, **Medium**, or **Strong**, and gives suggestions on how to improve it. It also checks the password against a list of common leaked passwords, since a long password is still risky if it's one attackers try first.

## Features

- Checks password length (minimum 8 characters)
- Checks for uppercase letters, lowercase letters, numbers, and symbols
- Flags common/leaked passwords (e.g. `123456`, `qwerty`, `password`) as weak, regardless of length
- Gives specific suggestions for improving a weak or medium password
- Runs in a loop so you can test multiple passwords in one session

## How it works

1. If the password matches a known common password, it's immediately marked **Weak**.
2. If the password is under 8 characters, it's immediately marked **Weak**.
3. Otherwise, it's scored on 4 criteria: uppercase, lowercase, digit, symbol.
   - 0–1 criteria met → **Weak**
   - 2–3 criteria met → **Medium**
   - All 4 criteria met → **Strong**

## How to run

1. Make sure Python 3 is installed on your system.
2. Clone this repository or download `password_strength_checker.py`.
3. Open a terminal in the project folder and run:
   ```
   python password_strength_checker.py
   ```
4. Enter a password when prompted. Type `quit` to exit.

## Example

```
Enter a password to check: qwerty

Password entered : ******
Strength result  : Weak
Suggestions to improve it:
  - This is one of the most common leaked passwords. Choose something unique.
--------------------------------------------------
Enter a password to check: MyP@ssw0rd2026

Password entered : **************
Strength result  : Strong
Great job! This password meets all the security criteria.
```

## Key skills practiced

- String handling
- Conditional logic
- Basic security concepts (entropy, common password lists)

## Author

Built as part of the DecodeLabs Cyber Security internship program.