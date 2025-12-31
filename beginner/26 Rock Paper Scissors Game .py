import random

print("Rock Paper Scissors Game")

while True:
    choices = ['rock', 'paper', 'scissors']
    x = input("Enter your choice:\n1. Rock\n2. Paper\n3. Scissors\n>> ").lower().strip()
    computer_choice = random.choice(choices)

    if x == '1':
        x = "rock"
    elif x == '2':
        x = "paper"
    elif x == '3':
        x = "scissors"
    else:
        print("Invalid choice. Please try again.")
        continue  # Skip the rest of the loop if the choice is invalid

    print(f"You chose: {x}")
    print(f"Computer chose: {computer_choice}")

    if x == computer_choice:
        print("It's a tie!")
    elif (x == 'rock' and computer_choice == 'scissors') or \
         (x == 'scissors' and computer_choice == 'paper') or \
         (x == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("You lose!")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break