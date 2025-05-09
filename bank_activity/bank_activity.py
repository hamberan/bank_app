import random

# admins["name:hamberan,age:22,address:vaddukoddai,password:venu"]
admins={"name":"hamberan", "password":"venu"}
with open("bank_admins", "w") as file:
    file.write(f"{admins['name']}, {admins['password']}\n") 

#=========================creat_peposit functation============================================================================#
def deposit():
    amount = int(input("Enter the amount to deposit: "))
    if amount <= 0:
        print("invalid deposit amount.")
        return

    customer_id = input("Enter customer ID: ") 
    updated_lines = []
    deposit_successful = False

    with open("customer_details", "r") as file:
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
        with open("customer_details", "a") as file:
            file.writelines(updated_lines)
    else:
        print("Customer not found.")
    

def check_balance():
    print(1)

def withdraw_money():
    amount=int(input("enter your withdraw amount"))
    if amount<=0:
        print("invalid withdraw amount")
        return

    customer_id= input("enter customer account_number:")
    updated_lines= []
    withdraw_successfull = False

    with open("customer_details","r") as file:
        for line in file:
            f=line.strip().split(",")
            if len(f) >= 5 and f[0].strip== customer_id:
                balance=int(f[4].strip())
                balance -= amount 
                f[4] =str(balance)
                updated_line=",".join(f)
                updated_lines.append(updated_line +"\n")
                withdraw_successfull = True

                with open("transactions.txt","a") as t_file:
                    t_file.write(f"{customer_id},{amount},{balance}\n")

                print(f"successfully withdrawal {amount}.new balance: {balance}")
            else:
                updated_lines.append(line)

    if withdraw_successfull:
        with open("customer_deatials","a") as file:
            file.writelines(updated_lines)
    else:
        print("customer not found.")                               


   
def transaction_history():
    with open("transactions.txt", "r") as file:
         for line in file:
            f = line.strip().split(",") 
            if len(f) >= 3:
                store_account_number, store_deposit, store_balance = f[0].strip(), f[1].strip(), f[2].strip()
                print(f"Account Number: {store_account_number}, Deposit Amount :{store_deposit}, Current Balance :{store_balance}")


def customer_details():
    with open("customer_details.txt","r") as file:
        for line in file:
            f=line.sprip().split(",")
            if len(f) >=5:
                store_account_number,store_name,store_address,store_password,store_balance=f[0].strip(),f[1].strip(),f[2].strip(),f[3].sprip()
                print(f"account number:{store_account_number},name:{store_name},address:{store_address},balance:{store_balance}")
                

def creat_account():
    customer_name=input("enter customer name  : ")
    customer_address=input("enter costomer address: ")
    customer_password=input("enter costomer password: ")
    customer_account_number=random.randint(1000,5000)
    initial_balance = int(input("Enter your first amount"))
    with open("customer_details", "w") as file:
        file.write(f"{customer_account_number},{customer_name},{customer_address},{customer_password},{initial_balance}\n")
    print(f"------crest new account successfully your account number is {customer_account_number}------")

def admins():
    ad_name=input("enter admin name: ")
    ad_password=input("enter your password: ")
    with open("bank_admins", "r") as file:
         for line in file:
            f = line.strip().split(",") 
            if len(f) >= 2:
                store_name, store_password = f[0].strip(), f[1].strip()
    if store_name==ad_name and store_password==ad_password:
        while True:
            print("---user menu----")
            print("1.create new account")
            print("2.customer transaction history")
            print("3.customer details")
            print("4.exit")
            choice=input("enter your choice: ")
            if choice=="1":
                creat_account()
            elif choice=="2":
                transaction_history()
            elif choice=="3":
                customer_details()
            elif choice=="4":
                print("thanks for using our app!")
                exit()
            else:
                print("invaild choice")
                
        
                        

def customers():
    name=input("enter your name: ")
    password=input("enter your password: ")
    with open("customer_details", "r") as file:
         for line in file:
            f = line.strip().split(",") 
            if len(f) >= 4:
                store_name, store_password = f[1].strip(), f[3].strip()
    if store_name==name and store_password==password:
        print("--------your login successfully!--------")
        print("----customer menu------")
        print("1.deposit money")
        print("2.withdraw money")
        print("3.cheak balance")
        print("4.transaction history")
        print("5.exit")
        choice=int(input("enter your choice: "))
        if choice==1:
            deposit()
        elif choice==2:
            withdraw_money()
        elif choice==3:
            check_balance()
        elif choice==4: 
            transaction_history()
        elif choice==5:
            main_menu()
        else:
            print("invalid function")
    else:
        ("test")

def user_menu():
    print("1.admin")
    print("2.customer")
    choice=int(input("enter your choice: "))
    if choice==1:
        admins()
    if choice==2:
        customers()    

         
def main_menu():
    print("---------wellcome ! to mini bank app---------")
    user_menu()


main_menu()  