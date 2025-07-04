def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("users.txt", "a") as f:
        f.write(username + "," + password + "\n")
    print("Registered successfully!\n")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("users.txt", "r") as f:
        users = f.readlines()
        for user in users:
            u, p = user.strip().split(",")
            if u == username and p == password:
                print("Login Successful!\n")
                return
    print("Invalid Credentials!\n")

while True:
    print("1. Register\n2. Login\n3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid Option\n")
