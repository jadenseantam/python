key = {}

def addUser():
    newUsername = input("Enter username: ")
    newpassword = input("Enter password: ")
    key[newUsername] = newpassword
    print("Signed Up!\n\n")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in key:
        if key[username] == password:
            print("Logged In!\n\n")
        else:
            print("Incorrect password!\n\n")
    else:
        print("Username not found!\n\n")

def deleteAcc():
    deluser = input("Enter the username to delete: ")
    delpass = input("Enter the password to delete: ")
    if deluser in key and key[deluser] == delpass:
        del key[deluser]
        print("Account Deleted!\n\n")
    else:
        print("Invalid input!\n\n")

def viewAcc():
    global admin_username
    global admin_password
    admin_username = "admin"
    admin_password = "1077"
    inadmin_u = input("Enter admin username: ")
    inadmin_p = input("Enter admin password: ")
    if inadmin_u == admin_username and inadmin_p == admin_password:
        print(key + "\n\n")
    else: 
        print("Invalid username or password.\n\n")    

def saveAcc():
    inadmin_u = input("Enter admin username: ")
    inadmin_p = input("Enter admin password: ")
    if inadmin_u == admin_username and inadmin_p == admin_password:
        with open("key.txt", "w") as file:
            for username, password in key.items():
                file.write(f"{username}:{password}\n")
        print("Accounts saved!\n\n")
    else: 
        print("Invalid username or password.\n\n") 

def loadAcc():
    try:
        with open("key.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(':')
                key[username] = password
        print("Accounts loaded!\n\n")
    except FileNotFoundError:
        pass
    except Exception as e:
        pass