def typewriter(s):
    import sys, time, os
    for char in s:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(0.05)
        else:
            time.sleep(1)


def InvalidInput():
    print("Invalid input, try again.\n")

def TimedInput(UserInputQ, TimesUp, TimeToElapse):
    import threading
    import time

    InputRecieved = [False]
    threading.Thread(target=lambda: (time.sleep(TimeToElapse), print(TimesUp) if not InputRecieved[0] else None)).start()
    UserInput = input(UserInputQ)
    InputRecieved[0] = True
    

    return UserInput

