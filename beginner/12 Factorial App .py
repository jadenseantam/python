from math import factorial

while True:
    print("***** FACTORIAL APP *****\n")

    try:
        x = int(input("Enter a non-negative integer\n>> "))
        if x < 0:
            print("Enter a non-negative integer!\n")
        elif x > 1000:  # Set a reasonable limit
            print("Input is too large to compute the factorial.\n")
        else:
            result = factorial(x)
            print(f"The factorial of {x} is {result}.\n")
    except ValueError:
        print("ValueError: Please enter a valid integer.\n")
    except OverflowError:
        print("OverflowError: The result is too large to compute.\n")