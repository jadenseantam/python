import pickle
import time

print("Login System - Workspace Version\n")
admin_accounts = {}

def save_accounts():
    with open("admin_accounts.pkl", "wb") as file:
        pickle.dump(admin_accounts, file)
    print("Admin accounts saved successfully.\n")

def load_accounts():
    global admin_accounts
    try:
        with open("admin_accounts.pkl", "rb") as file:
            admin_accounts = pickle.load(file)
        print("Admin accounts loaded successfully.\n")
    except FileNotFoundError:
        pass

def add_admin_acc():
    admin_username = input("Create admin username: ")
    admin_password = input("Create admin password: ")
    
    if admin_username in admin_accounts:
        print("Admin username already exists. Please choose another.\n")
        return

    admin_accounts[admin_username] = {
        'password': admin_password,
        'users': {}
    }
    print(f"Admin account '{admin_username}' created successfully.\n")

def add_user():
    signinAdmin = input("Enter your admin account username: ")
    signinPassAdmin = input("Enter your admin account password: ")

    if (signinAdmin in admin_accounts) and (signinPassAdmin == admin_accounts[signinAdmin]['password']):
        username = input("Enter new username: ")
        password = input("Enter new password: ")

        if username in admin_accounts[signinAdmin]['users']:
            print("User username already exists. Please choose another.\n")
        else:
            admin_accounts[signinAdmin]['users'][username] = password
            print(f"User '{username}' added successfully under admin '{signinAdmin}'.\n")
    else:
        print("Invalid admin username or password.\n")

def sign_in():
    pass  # You can implement the sign-in functionality here

# Load accounts at the start of the program
print("Loading accounts...")
time.sleep(2)
load_accounts()

# Main Loop
while True:
    print("1. Add admin accounts\n2. Add user to admin accounts\n3. Save accounts\n4. Exit\n")
    command = input("Enter your choice\n>> ")

    if command == "1":
        add_admin_acc()
    elif command == "2":
        add_user()
    elif command == "3":
        save_accounts()
    elif command == "cls" or command == "4":
        print("Exiting the system.")
        break
    elif command == "s":
        print(admin_accounts)
    else:
        print("Invalid choice. Please try again.\n")