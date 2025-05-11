import random

#======================== Admin Data Initialization ========================#
admins = {"name": "hamberan", "password": "venu"}
with open("bank_admins.txt", "w") as file:
    file.write(f"{admins['name']},{admins['password']}\n")

#======================== Create Account ========================#
def create_account():
    customer_name = input("Enter customer name: ")
    customer_address = input("Enter customer address: ")
    customer_password = input("Enter customer password: ")
    customer_account_number = random.randint(1000, 5000)
    initial_balance = int(input("Enter your first deposit amount: "))

    with open("customer_details.txt", "a") as file:
        file.write(f"{customer_account_number},{customer_name},{customer_address},{customer_password},{initial_balance}\n")

    print(f"Account created successfully! Your account number is: {customer_account_number}")

#======================== Deposit Money ========================#
def deposit():
    amount = int(input("Enter the amount to deposit: "))
    if amount <= 0:
        print("Invalid deposit amount.")
        return

    customer_id = input("Enter customer account number: ")

    updated_lines = []
    deposit_successful = False

    with open("customer_details.txt", "r") as file:
        for line in file:
            f = line.strip().split(",")
            if len(f) >= 5 and f[0].strip() == customer_id:
                balance = int(f[4].strip())
                balance += amount
                f[4] = str(balance)
                updated_line = ",".join(f)
                updated_lines.append(updated_line + "\n")
                deposit_successful = True

                with open("transactions.txt", "a") as t_file:
                    t_file.write(f"{customer_id},{amount},{balance}\n")

                print(f"Successfully deposited {amount}. New balance: {balance}")
            else:
                updated_lines.append(line)

    if deposit_successful:
        with open("customer_details.txt", "w") as file:
            file.writelines(updated_lines)
    else:
        print("Customer not found.")

#======================== Withdraw Money ========================#
def withdraw_money():
    amount = int(input("Enter your withdrawal amount: "))
    if amount <= 0:
        print("Invalid withdrawal amount.")
        return

    customer_id = input("Enter customer account number: ")

    updated_lines = []
    withdraw_successful = False

    with open("customer_details.txt", "r") as file:
        for line in file:
            f = line.strip().split(",")
            if len(f) >= 5 and f[0].strip() == customer_id:
                balance = int(f[4].strip())
                if balance < amount:
                    print("Insufficient balance.")
                    return
                balance -= amount
                f[4] = str(balance)
                updated_line = ",".join(f)
                updated_lines.append(updated_line + "\n")
                withdraw_successful = True

                with open("transactions.txt", "a") as t_file:
                    t_file.write(f"{customer_id},-{amount},{balance}\n")

                print(f"Successfully withdrew {amount}. New balance: {balance}")
            else:
                updated_lines.append(line)

    if withdraw_successful:
        with open("customer_details.txt", "w") as file:
            file.writelines(updated_lines)
    else:
        print("Customer not found.")

#======================== Transaction History ========================#
def transaction_history():
    with open("transactions.txt", "r") as file:
        for line in file:
            f = line.strip().split(",")
            if len(f) >= 3:
                acc_num, amount, balance = f[0], f[1], f[2]
                print(f"Account Number: {acc_num}, Transaction: {amount}, Balance: {balance}")

#======================== Admin Login ========================#
def admin_login():
    ad_name = input("Enter admin name: ")
    ad_password = input("Enter admin password: ")

    with open("bank_admins.txt", "r") as file:
        for line in file:
            f = line.strip().split(",")
            if len(f) >= 2:
                store_name, store_password = f[0].strip(), f[1].strip()

                if store_name == ad_name and store_password == ad_password:
                    print("Admin login successful.")
                    while True:
                        print("\n--- Admin Menu ---")
                        print("1. Create New Account")
                        print("2. View Customer Transaction History")
                        print("3. Exit")
                        choice = input("Enter your choice: ")

                        if choice == "1":
                            create_account()
                        elif choice == "2":
                            transaction_history()
                        elif choice == "3":
                            print("Exiting admin panel.")
                            break
                        else:
                            print("Invalid choice.")
                    return

    print("Invalid admin credentials.")

#======================== Customer Login ========================#
def customer_login():
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    with open("customer_details.txt", "r") as file:
        for line in file:
            f = line.strip().split(",")
            if len(f) >= 4:
                store_name, store_password = f[1].strip(), f[3].strip()

                if store_name == name and store_password == password:
                    print("Login successful!")
                    while True:
                        print("\n--- Customer Menu ---")
                        print("1. Deposit Money")
                        print("2. Withdraw Money")
                        print("3. View Transaction History")
                        print("4. Exit")
                        choice = input("Enter your choice: ")

                        if choice == "1":
                            deposit()
                        elif choice == "2":
                            withdraw_money()
                        elif choice == "3":
                            transaction_history()
                        elif choice == "4":
                            print("Logging out...")
                            return
                        else:
                            print("Invalid choice.")
                    return

    print("Invalid customer credentials.")

#======================== User Menu ========================#
def user_menu():
    while True:
        print("\n1. Admin")
        print("2. Customer")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_login()
        elif choice == "2":
            customer_login()
        elif choice == "3":
            print("Thank you for using Mini Bank App!")
            break
        else:
            print("Invalid choice.")

#======================== Main ========================#
def main_menu():
    print("--------- Welcome to Mini Bank App ---------")
    user_menu()

main_menu()
