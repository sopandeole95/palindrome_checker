# Method 1: Using slicing
def is_palindrome_slicing(word):
    reversed_word = word[::-1]
    print(f"Reversed String: {reversed_word}")
    if word == reversed_word:
        return True
    return False

# Method 2: Using reversed()
def is_palindrome_reversed(word):
    word = word.casefold()  # Convert to lowercase for case-insensitive comparison
    return list(word) == list(reversed(word))

# Main program
print("Palindrome Checker")
word = input("Enter the string you want to check: ")

# Check palindrome using both methods
if is_palindrome_slicing(word):
    print("Yes, it is a palindrome (checked using slicing).")
else:
    print("No, it is not a palindrome (checked using slicing).")

if is_palindrome_reversed(word):
    print("Yes, it is a palindrome (checked using reversed()).")
else:
    print("No, it is not a palindrome (checked using reversed()).")
