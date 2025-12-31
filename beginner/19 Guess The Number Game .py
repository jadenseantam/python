import random

print("\n\n***** Guess-a-Number Game *****")

while True:
    try:
        lo = int(input("Enter the lowest number of range: "))
        hi = int(input("Enter the highest number of range: "))
        if lo >= hi:
            print("Lowest number must be less than highest number. Please try again.")
            continue
    except ValueError:
        print("Invalid input. Please enter integers only.")
        continue

    x = random.randint(lo, hi)
    guesses = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guesses += 1
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        if guess > x:
            print("Too high! Try again!")
        elif guess < x:
            print("Too low! Try again!")
        else:
            if guesses == 1:
                print(f"Correct! The number was {x}. You guessed it in {guesses} try only!")
            else:
                print(f"Correct! The number was {x}. You guessed it in {guesses} tries.")
            break