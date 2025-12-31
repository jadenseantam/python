print("Interest Calculator\n")

while True:
    try:
        amount = float(input("Enter the amount of money: "))
        month = float(input("Enter the length of time in months: "))
        time = month / 12
        rate = float(input("Enter the rate (as a decimal, e.g., 0.05 for 5%): "))

        money = amount + (amount * time * rate)
        print(f"The money after calculating interest is: {money:.2f}")
        
        # Option to exit the loop
        continue_calculation = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if continue_calculation != 'yes':
            print("Exiting the calculator.")
            break

    except ValueError:
        print("Invalid input! Please enter numeric values.")