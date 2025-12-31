print("*****REVERSE A STRING*****\n\n")

while True:
    string = input("Enter a string\n\n>>")

    # Process
    newString = string[::-1]

    # Print answer 
    print(f"The new string is {newString}.\n\n")

    choice = input("Do you want to play again? (y/n)")

    if choice.strip().lower() != "y":
        break