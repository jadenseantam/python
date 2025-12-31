import sys, time, os

def typewriter(message):
    message = "This is a message. For testing, I am going to make it much much much much much much much much much much much much much much much longer. Next, I am going to make the testing keyboard! By the way, these are just for tesings, really."
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.05)
        else:
            time.sleep(0.8)
while True: 
    typewriter(message)
    input("Press enter to continue...")