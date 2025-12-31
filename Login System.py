from LoginSystemModules import *

print("Login System\n")
loadAcc()

# Main loop
while True:
    print("1. Sign Up\n2. Log in\n3. Delete Account\n4. View Accounts (Admin use only)\n5. Save Accounts (Admin use only)\n\n")
    command = input("Enter command: ")

    if command == "1":
        addUser()
    elif command == "2":
        login()
    elif command == "3":
        deleteAcc()
    elif command == "4":
        viewAcc()
    elif command == "5":
        saveAcc()
    else:
        print("Invalid command.\n\n")