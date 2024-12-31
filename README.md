# Palindrome Checker 🔄

A Python program to check whether a given string is a palindrome. This project uses two methods to determine if the string is the same when read forwards and backwards.

## Problem Statement
Write a Python program to:
1. Reverse a string and compare it with the original.
2. Use the `reversed()` function for comparison.

## Features
- Two methods for palindrome checking:
  - **Slicing**: Reverse the string using slicing (`[::-1]`).
  - **Reversed()**: Use the built-in `reversed()` function.
- Case-insensitive comparison using `casefold()`.

## How to Run
1. Run the program:
   ```bash
   python palindrome_checker.py

## Sample Output
Palindrome Checker
Enter the string you want to check: Madam
Reversed String: madaM
Yes, it is a palindrome (checked using slicing).
Yes, it is a palindrome (checked using reversed()).
