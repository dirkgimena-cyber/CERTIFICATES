# Fantasy Guild  Store
# Phase 2 - Account Creation And Core Logic



# -----------------------------
# MOCK USER DATA
# -----------------------------

users = {}


# -----------------------------
# ACCOUNT CREATION
# -----------------------------

def create_account():
    print("===== CREATE ACCOUNT =====")

    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if username in users:
        print("Username already exists. Please choose a different username.")
        return

    users[username] = password
    print("Account created successfully.")


# -----------------------------
# LOGIN
# -----------------------------

def login():
    print("===== LOGIN =====")

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login successful.")
        print("Welcome to the Fantasy Guild Store!")
        return True
    else:
        print("Invalid username or password.")
        return False
