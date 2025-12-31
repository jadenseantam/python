print("***** PALINDROME CHECKER *****\n")

while True:
    x = input("Enter a string\n>> ").strip().lower()
    
    # Check if the string is a palindrome
    if x == x[::-1]:  # Compare the string with its reverse
        print("It's a palindrome.\n")
    else:
        print("It's not a palindrome.\n")