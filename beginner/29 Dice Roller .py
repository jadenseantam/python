import random
import time

while True:
    print("Dice Roller\n")

    try:
        DiceNumber = int(input("How many dice do you want to roll? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if DiceNumber <= 0:
        print("Please enter a positive number of dice.")
        continue

    total = 0  # Initialize total outside the loop

    print("Rolling the dice...")

    if DiceNumber > 100:
        for _ in range(DiceNumber):
            rand = random.randint(1, 6)
            total += rand
    else:
        for _ in range(DiceNumber):
            rand = random.randint(1, 6)
            total += rand
            print(f"Rolled: {rand}")  # Display each roll

    print(f"\nThe total is {total}")