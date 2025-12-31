import datetime

print("Expense Tracker\n")

budget = 0.00
transactions = []

def show_menu():
    print("1. Add income")
    print("2. Add expense")
    print("3. Clear")
    print("4. Save")
    print("5. View")
    print("6. Exit\n")

def add_income():
    global budget
    try:
        income = float(input("Enter income: "))
        if income < 0:
            print("Income cannot be negative. Adding failed!")
            return
        budget += income
        transactions.append(f"Income: ${income:.2f}")
        print("Income added")
    except ValueError:
        print("Invalid input, adding failed!")

def add_expenditure():
    global budget
    try:
        expense = float(input("Enter expense: "))
        if expense < 0:
            print("Expense cannot be negative. Adding failed!")
            return
        budget -= expense
        transactions.append(f"Expense: ${expense:.2f}")
        print("Expense added")
    except ValueError:
        print("Invalid input, adding failed!")

def clear():
    global budget, transactions
    budget = 0.00
    transactions.clear()
    print("Income and expenses cleared")

def save():
    with open("money.txt", "a") as file:
        date = datetime.datetime.now()
        file.write(f"Transactions as of {date}:\n")
        for transaction in transactions:
            file.write(transaction + "\n")
        file.write(f"Current balance: ${budget:.2f}\n\n")
    print("Income and expense saved")

def view():
    print(f"Current Income/Expense: ${budget:.2f}")
    if transactions:
        print("Transactions:")
        for transaction in transactions:
            print(transaction)
    else:
        print("No transactions recorded.")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_income()
    elif choice == "2":
        add_expenditure()
    elif choice == "3":
        clear()
    elif choice == "4":
        save()
    elif choice == "5":
        view()
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")