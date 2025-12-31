import math

print("***** BASIC CALCULATOR *****\n")

def add():
    total = 0
    i = 1
    while True:
        x = input(f"Enter the {i} number (or 'n' to stop): ")
        if x.lower() == 'n':
            break
        try:
            total += float(x)
            i += 1
        except ValueError:
            print("Please enter a valid number.\n")
    
    print(f"The sum is {total}.\n")

def subtract():
    total = float(input("Enter the first number: "))
    while True:
        x = input("Enter the next number to subtract (or 'n' to stop): ")
        if x.lower() == 'n':
            break
        try:
            total -= float(x)
        except ValueError:
            print("Please enter a valid number.\n")
    
    print(f"The difference is {total}.\n")

def multiply():
    total = 1
    i = 1
    while True:
        x = input(f"Enter the {i} number (or 'n' to stop): ")
        if x.lower() == 'n':
            break
        try:
            total *= float(x)
            i += 1
        except ValueError:
            print("Please enter a valid number.\n")
    
    print(f"The product is {total}.\n")

def divide():
    total = float(input("Enter the numerator: "))
    while True:
        x = input("Enter the denominator (or 'n' to stop): ")
        if x.lower() == 'n':
            break
        try:
            denom = float(x)
            if denom == 0:
                print("Cannot divide by zero.\n")
                continue
            total /= denom
        except ValueError:
            print("Please enter a valid number.\n")
    
    print(f"The result is {total}.\n")

def square_root():
    x = input("Enter a number to find the square root: ")
    try:
        result = math.sqrt(float(x))
        print(f"The square root is {result}.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def cube_root():
    x = input("Enter a number to find the cube root: ")
    try:
        result = float(x) ** (1/3)
        print(f"The cube root is {result}.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def exponent():
    base = float(input("Enter the base: "))
    exp = float(input("Enter the exponent: "))
    result = base ** exp
    print(f"The result is {result}.\n")

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Cube Root")
    print("7. Exponents")
    print("8. Exit\n")
    
    cmd = input("Enter your command: ")

    if cmd == "1":
        add()
    elif cmd == "2":
        subtract()
    elif cmd == "3":
        multiply()
    elif cmd == "4":
        divide()
    elif cmd == "5":
        square_root()
    elif cmd == "6":
        cube_root()
    elif cmd == "7":
        exponent()
    elif cmd == "8":
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid command. Please try again.\n")