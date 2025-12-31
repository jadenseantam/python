Admin = False

def admin():
    try:
        length = int(input("Enter the number of options: "))
    except ValueError:
        print("Invalid input!")
        return  # Exit the function if input is invalid

    options = []  # Initialize the options list
    for _ in range(length):
        optionq = input("Option: ")
        options.append(optionq)

    print("Options added:", options)
    return options  # Return the list of options

def vote(options):
    votes = {option: 0 for option in options}  # Initialize vote counts
    while True:
        print("\nAvailable options:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Vote for an option number (0 to finish voting): "))
            if choice == 0:
                break
            if 1 <= choice <= len(options):
                votes[options[choice - 1]] += 1
                print(f"Vote cast for: {options[choice - 1]}")
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Voting complete. Final votes:")
    for option, count in votes.items():
        print(f"{option}: {count} votes")

def main():
    options = []  # Initialize options outside the loop

    while True:
        adminq = input("Are you admin? (y/n)\n>> ")
        if adminq.lower() == "y":
            adminpass = input("Enter admin password: ")
            if adminpass == "votingadmin":
                options = admin()  # Get the options from admin
            else:
                print("Admin password invalid.")
        else:
            if options:
                print("User is voting.")
                vote(options)  # Allow users to vote on the options
            else:
                print("No options available for voting. Please ask an admin to set options.")

if __name__ == "__main__":
    main()