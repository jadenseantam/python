import datetime

print("Budget Tracker\n")

budget = 0.00

def show_menu():
    print("1. Add income")
    print("2. Add expenditure")
    print("3. Clear")
    print("4. Save")
    print("5. View")
    print("6. Exit\n")

def add_income():
    global budget
    try:
        income = float(input("Enter income: "))
        budget += income
        print("Income added")
    except ValueError:
        print("Invalid input, adding failed!")

def add_expenditure():
    global budget
    try:
        expenditure = float(input("Enter expenditure: "))
        budget -= expenditure
        print("Expenditure added")
    except ValueError:
        print("Invalid input, adding failed!")

def clear():
    global budget
    budget = 0.00
    print("Budget cleared")

def save():
    with open("money.txt", "a") as file:
        date = datetime.datetime.now()
        file.write(f"Budget as of {date}: {budget}\n")
    print("Budget saved")

def view():
    print(f"Current budget: {budget}")

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