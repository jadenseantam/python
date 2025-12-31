import time
import tools
import random
import signal
import sys
import os

RED = "\033[31m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
SYAN = "\033[36m"
RESET = "\033[0m"
BrightBlack = "\u001b[90m"
BrightRed = "\u001b[91m"
BrightGreen = "\u001b[92m"
BrightYellow = "\u001b[93m"
BrightBlue = "\u001b[94m"
BrightMagenta = "\u001b[95m"
BrightCyan = "\u001b[96m"
BrightWhite = "\u001b[97m"

def display_img(filename):
    try:
        filepath = os.path.join("/media/student/NO NAME/Week 6 Jaden/Game/art", filename)
        with open(filepath, "r") as f:
            content = f.read()
        print(content)
        sys.stdout.flush() 
    except FileNotFoundError:
        print(f"File '{filename}' at '{filepath}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

def StartScene():
    print(RED + "The " + BLUE + "ULTIMATE " + YELLOW + "ADVENTURE " + PURPLE + "by " + SYAN + "Jaden " + GREEN + "Tam"  + YELLOW + "!" + RESET)
    print(BrightGreen + "Welcome" + BrightRed + " to " + BrightYellow + "the " + SYAN + "Ultimate " + RESET + PURPLE + "Adventure! " + RESET)
    print("Let's start playing! Remember, you are Weasley!")
    input("Press enter to continue...")
    IntroScene()

def IntroScene():
    IntroSceneVar1 = input("Do you want to go an advanture at the city of " + GREEN + "Tech (C.O.Tech)? " + RESET + "(y/n) \n>> ").lower().strip()
    if IntroSceneVar1 == "y":
        IntroSceneVar2 = ("One more reminder: Press enter to continue to the Adventure!")
        print(IntroSceneVar2)
        input("\n")
        Adv1()
    elif IntroSceneVar1 == "n":
        print("Goodbye!")
    else:
        tools.InvalidInput()
        IntroScene()

def Adv1():
    Adv1Var1Backstory = ["You see a wall in front you, surrounding you.", "There is a door on the wall, which is led to the C.O.Tech, but it is locked.", "You saw a green light flashing, and you found that it is a button. "] ##### Draw picture #####
    
    for line in Adv1Var1Backstory:
        print(line, end="")
        input()

    Adv1Var2 = input("Will you press that button? (y/n)\n>> ").lower().strip()
    while Adv1Var2 != "y" or Adv1Var2 != "n":
        if Adv1Var2 == "y":
            print("You are dead! That button is actually a huge bomb! You lose!")
            break
        elif Adv1Var2 == "n":
            print("That button is actually a bomb! However, You have to solve a puzzle to unlock the door to get into the C.O.Tech")
            Adv2()
            break
        else:
            tools.InvalidInput()
            Adv1Var2 = input("Will you press that button? (y/n)\n>> ")

def Adv2():
    print("\nThe key to unlock the door is that you have to have to send a letter to the city. However, another bomb is going to explode 25 seconds after you pressed Enter. If you press Enter, you will start the letter.", end="")
    input()
    print("You have to type out 'Unlock the door as quick as possible. To the guard.' in 20 seconds.", end="")
    UserInput2 = tools.TimedInput(UserInputQ="\nStart typing: ", TimesUp="\nTime's Up! You lose!", TimeToElapse=int(25))
    if ("unlock the door as quick as possible" in UserInput2.strip().lower()) and ("guard" in UserInput2.strip().lower()):
        print("You unlocked the door! Welcome to C.O.Tech!", end="")
        input()
        Adv3()
    elif "Unlock the door as quick as possible".strip().lower() in UserInput2.strip().lower():
        print("Your letter didn't tell the guard to unlock the door, but fell into a wrong hand. You lose!")
    elif "To the guard".strip().lower() in UserInput2.strip().lower():
        print("You didn't tell the guard what to do! You lose! Hit Ctrl + C")
    else:
        print("You lose! Hit Ctrl + C to quit!")

def Adv3():
    Adv3Var1Backstory = ["There is a very famous singer, whose son - Don was kidnapped by someone. ", "He is your friend, and he needs your help.", "You arrived at the scene where Don was kidnapped. There was a paper and a computer - written... "]
    for line in Adv3Var1Backstory:
        print(line, end="")
        input()
    Adv3Var2 = input("Type 'Flip' to flip the paper.\n>> ").strip().lower()
    printer = ["****THE TEST OF REACTIONS****", "Press enter when you are ready...", "There is 8 letters...", "Memorise them...", "Type it out...", "If you pass it, some hints will be given to you...", "...to rescue Don...", "If you lose, you and Don will be dead very soon..."]
    for i in printer:
        print(i, end="")
        input()
            
            
    while Adv3Var2 != "flip":
            tools.InvalidInput()
            Adv3Var2 = input("Type 'Flip' to flip the paper.\n>> ")

    target = ["cjenidso", "dcteckdi", "xuwmfkdi", "djiyexoc", "gajejvtw", "kshenmrw"]

    current = random.choice(target)
    print(f"Remember and type: {current}. You have ten seconds to memorise." + RED + " Don't " + BrightRed + "press enter in this 10 seconds!" + RESET)
    time.sleep(10)
    i = 0 
    while i <= 900:
        display_img("load.txt")
        i += 1

    user = input(">> ")

    
    if current == user.strip().lower():
        print("You passed this test! You got the hint!")
        Adv3Var3 = input("Type 'Open' to open the hint.\n>> ").lower().strip()
        while Adv3Var3 != "open".strip().lower():
            tools.InvalidInput()
            Adv3Var3 = input("Type 'Open' to open the hint.\n>> ")
        if Adv3Var3 == "open".strip().lower():
            print("Pass this word if for guessed the word lock and of course, Don! Read odd numbers of words and skip punctuations.", end="")
            input()
            Adv4()
    else:
        print("You can't remember it! You lose!")

def Adv4():
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

    
    print("Guess a word in 6 letters: (Friendly Reminder: Use capital letters to type. It will be easier for you to read. Type 'hint' for hints.)")

    guesses = 0
    attempts = 7
    hints = 0
    targets = ["STROLL", "PIZZAS", "BANANA", "ORANGE", "APPLES", "POTATO", "TOMATO", "FRUITS", "LEAVES", "LAPTOP", "CAMPER", "PEOPLE", "FRIDGE", "TABLES", "TOILET", "GRAPES", "FLYING", "TISSUE", "DONUTS", "GARDEN", "PENCIL", "PAINTS", "CANDLE", "AUGUST", "HOODIE"]
    target = random.choice(targets).upper().strip()
    while attempts >= 1:
        guess = input().strip().upper()
        guess_len = len(guess)
        if guess.lower().strip() == "hint" and hints == 0:
            starts_letter = target[0]
            print(f"The word starts with '{starts_letter}'.")
            hints += 1
        elif guess.lower().strip() == "hint" and hints == 1:
            print(f"The second letter is '{target[1]}'.")
            hints += 1
        elif guess.lower().strip() == "hint" and hints == 2:
            print(f"The last letter of the word is '{target[-1]}'")
            hints = 100
        elif (len(guess) > 6) or (len(guess) < 6):
            print("Guess a 6-letters word!")
        else:
            result = check_guess(guess, target)
            print(result)
        if hints == 100:
            print("No more hints available! Guess it yourself!")

        if guess == target:
            print(f"You have guessed the word!\n\n\n\n")
            break
            
        attempts -= 1
        print(f"You have {attempts} attempts left!")

    if attempts == 0:
        print("You lose!") 
        print(f"The password is {target}")

    password = input("Enter password to rescue Don: ")
    if password.upper().strip() == target.upper().strip():
        print("Phew! After a long, long journey, you finally win! Congratulations!")
        target = random.choice(targets).upper().strip()

    else:
        print("You didn't rescue Don! I hope his father will not get mad at you!")
    
    
StartScene()