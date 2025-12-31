print("TEMPERATURE CONVERTER\n")

while True:
    print("1. F to C")
    print("2. C to F")
    print("3. K to C")
    print("4. C to K")
    print("5. K to F")
    print("6. F to K")
    print("7. Exit\n")  # Option to exit the loop

    cmd = input("Enter your command: ")

    if cmd == "7":
        print("Exiting the converter. Goodbye!")
        break

    try:
        if cmd == "1":
            convert = float(input("Enter Fahrenheit: "))
            converted = (convert - 32) * 5 / 9
            print(f"Converted: {converted:.2f} °C\n")
        elif cmd == "2":
            convert = float(input("Enter Celsius: "))
            converted = convert * (9 / 5) + 32
            print(f"Converted: {converted:.2f} °F\n")
        elif cmd == "3":
            convert = float(input("Enter Kelvin: "))
            converted = convert - 273.15
            print(f"Converted: {converted:.2f} °C\n")
        elif cmd == "4":
            convert = float(input("Enter Celsius: "))
            converted = convert + 273.15
            print(f"Converted: {converted:.2f} K\n")
        elif cmd == "5":
            convert = float(input("Enter Kelvin: "))
            converted = (convert - 273.15) * 9 / 5 + 32
            print(f"Converted: {converted:.2f} °F\n")
        elif cmd == "6":
            convert = float(input("Enter Fahrenheit: "))
            converted = (convert - 32) * 5 / 9 + 273.15
            print(f"Converted: {converted:.2f} K\n")
        else:
            print("Invalid command.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")