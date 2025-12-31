import random

Mon = 1000

while True:
    CompChoice = random.randint(1, 5)
    print(f"You have {Mon} dollar(s).\n")
    HumanBet = input("Enter the amount of bet: ")
    try:
        HumanBet = int(HumanBet)
        if HumanBet < 5:
            print("Bet can't be smaller than 10!")
            continue
        if HumanBet > Mon:
            print("You don't have enough money!\n")
            continue
    except:
        print("Invalid input.\n")
        continue
    guess = input("Guess the number (1-5) the computer picked: ")
    if guess == str(CompChoice):
        print(f"You win! Computer choice is {CompChoice}!")
        Mon += HumanBet * 3
    else:
        print(f"Computer choice is {CompChoice}! You lose!")
        Mon -= HumanBet