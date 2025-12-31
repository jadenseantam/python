import random
name = input("What is your name? ")
print("Let's play rock paper scissors, " + name + "!")

player_score = 0
computer_score = 0

while True:
    print("\n--- Rock, Paper, Scissors ---")

    winner = "none"
    moves = ["rock", "paper", "scissors"]
    player_choice = input("Choose rock, paper or scissors: ").strip().lower()
    computer_choice = random.choice(moves)
    print("Computer's pick is " + computer_choice)
    if player_choice == computer_choice:
        print("It's a tie.")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("Rock crushes scissors! You win!")
        winner = "player"
    elif player_choice == "paper" and computer_choice == "rock":
        print("Paper wins Rock! You win!")
        winner = "player"
    elif player_choice == "scissors" and computer_choice == "paper":
        print("Scissors cuts paper! You win!")
        winner = "player"
    elif player_choice == "scissors" and computer_choice == "rock":
        print("Rock crushes scissors! You lose!")
        winner = "computer"
    elif player_choice == "rock" and computer_choice == "paper":
        print("Paper wins Rock! You lose!")
        winner = "computer"
    elif player_choice == "paper" and computer_choice == "scissors":
        print("Scissors cuts paper! You lose!")
        winner = "computer"
    else: 
        print("Hmm that wasn't one of our choice!")
        continue

    if winner == "player":
        player_score += 1
    elif winner == "computer":
        computer_score += 1

    print("Score: You =", player_score, "| Computer =", computer_score)

    play_again = input("Do you want to play again? (yes/no): ")

    if play_again != "yes":
        print("Thanks for playing. Press enter to exit...")
        input()
        break