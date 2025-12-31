import random

def check_guess(guess, target):
    
    result = ""
    for i in range(guess_len):
        if guess[i] == target[i]:
            result += GREEN + guess[i] + RESET
        elif guess[i] in target:
            result += YELLOW + guess[i] + RESET
        else:
            result += RED + guess[i] + RESET
    return result

print("Guess a word in 6 letters: (Friendly Reminder: Use capital letters to type. It will be easier for you to read.)")

guesses = 0
attempts = 7
targets = ["STROLL", "PIZZAS", "BANANA", "ORANGE", "APPLES"]
target = random.choice(targets).upper().strip()

while attempts >= 1:
    guess = input().strip().upper()
    guess_len = len(guess)

    if (len(guess) > 6) or (len(guess) < 6):
        print("Guess a 6-letters word!")
    else:
        result = check_guess(guess, target)
        print(result)

    if guess == target:
        print(f"You have guessed the word!\n\n\n\n")
        target = random.choice(targets).upper().strip()
        break
        
    attempts -= 1
    print(f"You have {attempts} attempts left!")

if attempts == 0:
    print("You lose!") 
    print(f"The password is {target}")