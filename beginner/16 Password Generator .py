import string
import random

print("Password Generator\n")

while True:
    # Use printable characters for password generation
    allchar = string.printable[:-6]  # Exclude non-printable characters (like whitespace)
    length = 0

    # Get the desired password length from the user
    while True:
        try:
            length = int(input("Enter length of password\n>> "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please enter a valid number.")

    # Generate a random password
    password = ''.join(random.choice(allchar) for _ in range(length))

    print(f"Your password is: {password}")