import time
import tools
import random

def StartScene():
    print("Welcome to the Ultimate Adventure! Let's start playing! Remember, you are Weasley!\n")
    input("Press enter to continue...\n")
    IntroScene()

def IntroScene():
    IntroSceneVar1 = input("Do you want to go an advanture at the city of Tech (C.O.Tech)? (y/n) \n>> ")
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
    Adv1Var2 = input("Will you press that button? (y/n)\n>> ")
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
    if UserInput2.strip().lower() == "Unlock the door as quick as possible. To the guard.".strip().lower():
        print("You unlocked the door! Welcome to C.O.Tech!", end="")
        input()
        Adv3()
    elif "Unlock the door as quick as possible".strip().lower() in UserInput2.strip().lower():
        print("Your letter didn't tell the guard to unlock the door, but fell into a wrong hand. You lose!")
    elif "To the guard".strip().lower() in UserInput2.strip().lower():
        print("You didn't tell the guard what to do! You lose!")
    else:
        print("You lose!")

def Adv3():
    Adv3Var1Backstory = ["There is a very famous singer, whose son - Don was kidnapped by someone. ", "He is your friend, and he needs your help.", "You arrived at the scene where Don was kidnapped. There was a paper and a computer - written... "]
    for line in Adv3Var1Backstory:
        print(line, end="")
        input()
    Adv3Var2 = input("Type 'Flip' to flip the paper.\n>> ")
    while Adv3Var2 != "Flip":
        if Adv3Var2 == "Flip":
            print("****THE TEST OF REACTIONS****\nPress enter when you are ready...\nPress 10 keys within 8 seconds...\nAfter you press a key, hit ENTER...\nIf you pass it, some hints will be given to you...\n...to rescue Don...\nIf you lose, you and Don will be dead very soon...")
        else: 
            tools.InvalidInput()
            Adv3Var2 = input("Type 'Flip' to flip the paper.\n>> ")

    target = ["cjendbidso", "dcteckdiel", "xuwmfvikdi", "djvywejxoc", "gajemxjvtw", "kshencirw"]

    current = random.choice(target)

    user = input(f"Remember and type: {current}.")

    if current == user.strip().lower():
        
        
    




StartScene()
