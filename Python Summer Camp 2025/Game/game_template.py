import signal
import sys
import os

# prints the ascii image from a text file
def display_img(filename):
    import signal
    import sys
    import os
    try:
        filepath = os.path.join("art", filename)
        with open(filepath, "r") as f:
            content = f.read()
        print(content)
        sys.stdout.flush() 
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

# used in if/else statements for an input not handled by case
def invalid_input(function):
    print("Invalid input, try again.")
    function()


def start():
    # add your title scene here
    pass
    

# This function is called to begin the game
start()
