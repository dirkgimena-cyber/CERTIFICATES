# Fantasy Guild Store ni OH C'mone
# Phase 1 and 2 - Account Creation and Core Logic



# -----------------------------
# MOCK USER DATA
# -----------------------------

users = {}

# -----------------------------
# ACCOUNT CREATION
# -----------------------------


def create_account():
    print()
    print("\033[95m===== CREATE ACCOUNT =====\033[0m")
    print()

    username = input("Create a username: ")
    password = input("Create a password: ")
    age = int(input("Enter your age: "))

    print()
    if username in users:
        print("\033[91mUsername already exists. Please choose a different username.\033[0m")
        return

    if age >= 18:
        status = "Adult"
        starting_money = 10000
    else:
        status = "Minor"
        starting_money = None

    users[username] = {
        "password": password,
        "age": age,
        "status": status,
        "starting_money": starting_money
    }

    print("\033[92mACCOUNT CREATED SUCCESSFULLY!\033[0m")
    print()

    print("\033[95m===== ACCOUNT DETAILS =====\033[0m")
    print()
    print("Username:", username)
    print("Password:", password)
    print("Age:", age)
    print("Status:", status)
    print()
    if status == "Adult":
        print("Starting Money: \033[92m₱10,000\033[0m")
    else:
        print("Starting Money: \033[92mUnlimited\033[0m")

    print()

    while True:
        choice = input("Press 2 to return to the main menu: ")

        if choice == "2":
            break
        else:
            print("\033[91mPlease press 2 to continue.\033[0m")
# -----------------------------
# LOGIN
# -----------------------------

def login_user():
    print()
    print("\033[95m===== LOGIN =====\033[0m")
    print()

    username = input("Username: ")
    password = input("Password: ")

    print()
    if username in users and users[username]["password"] == password:
        print("\033[92mLogin successful!\033[0m")
        print()
        print("\033[93mWelcome to the Fantasy Guild Store,", username + "!\033[0m")
        return username
        print()
    
    else:
        print("\033[91mIncorrect username or password. Please try again.\033[0m")
        return None


def display_products():
    print()
    print("\033[95m===== FANTASY GUILD STORE =====\033[0m")
    print()

    print("1. Health Potion - \033[92m₱50\033[0m")
    print("2. Mana Potion - \033[92m₱40\033[0m")
    print("3. Shield - \033[92m₱200\033[0m")
    print("4. Sword - \033[92m₱300\033[0m")


def shopping(username):
    products = {
        1: ["Health Potion", 50],
        2: ["Mana Potion", 40],
        3: ["Shield", 200],
        4: ["Sword", 300]}

    cart = []
    total = 0

    status = users[username]["status"]
    starting_money = users[username]["starting_money"]

    print("\033[95m===== SHOPPING =====\033[0m")
    print()

    if status == "Adult":
        print("Available Money: \033[92m₱10,000\033[0m")
    else:
        print("Available Money: \033[92mUnlimited\033[0m")

    while True:
        display_products()
        print("5. Checkout")

        choice = int(input("Choose an item: "))

        if choice == 5:
            break

        if choice not in products:
            print()
            print("Invalid choice. Please choose again.")
            continue

        quantity = int(input("Enter quantity: "))

        product_name = products[choice][0]
        product_price = products[choice][1]

        item_total = product_price * quantity

        if status == "Adult" and total + item_total > starting_money:
            print()
            print("\033[91mYou do not have enough money for this purchase.\033[0m")
        else:
            cart.append([product_name, quantity, item_total])

            total = total + item_total

            print()    
            print("\033[92mItem added to cart!\033[0m")
            print()
            print("Item:", product_name)
            print()
            print("Quantity:", quantity)
            print("Cost: \033[92m₱", item_total, "\033[0m")
            print()
            print("Current total: \033[92m₱", total, "\033[0m")
    
    print()
    print("\033[95m===== RECEIPT =====\033[0m")
    print()

    if len(cart) == 0:
        print()
        print("\033[91mYou did not purchase anything.\033[0m")
    else:
        for item in cart:
            print(item[0], "x", item[1], "- \033[92m₱", item[2], "\033[0m")

        print("-------------------------")
    print("Total: \033[92m₱", total, "\033[0m")
    if status == "Adult":
        print("Budget: \033[92m₱10,000\033[0m")
        print("Remaining Money: \033[92m₱", 10000 - total, "\033[0m")
    else:
        print("Budget: \033[92mUnlimited\033[0m")

    print()
    print("\033[93mThank you for shopping at the Fantasy Guild Store!\033[0m")


def main_menu(username):
    while True:
        print()
        print("\033[95m===== MAIN MENU =====\033[0m")
        print()

        print("Welcome,", username + "!")
        print("1. \033[92mStart Shopping\033[0m")
        print("2. \033[91mDetails\033[0m")
        print("3. \033[91mLogout\033[0m")

        print()
        choice = input("Choose one option: ")

        if choice == "1":
            shopping(username)

        elif choice == "2":
            print("\033[93mAccount Details:\033[0m")
            print("Username: ", username)
            print("Age: ", users[username]["age"])
            print("Status: ", users[username]["status"])
            
            if users[username]["status"] == "Adult":
                print("Starting Money: ₱10,000")
        elif choice == "3":
            print("\033[93mYou have been logged out.\033[0m")
            break

        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")


def main():
    while True:
        print("\033[95m==============================\033[0m")
        print("\033[95m     FANTASY GUILD STORE      \033[0m")
        print("\033[95m==============================\033[0m")
        print()
        print("1. \033[96mCreate Account\033[0m")
        print("2. \033[92mLogin\033[0m")
        print("3. \033[91mExit\033[0m")

        print()
        choice = input("Choose an option: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            username = login_user()

            if username is not None:
                main_menu(username)

        elif choice == "3":
            print()
            print("\033[93mThank you for using Fantasy Guild Store!\033[0m")
            break

        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")


main()

