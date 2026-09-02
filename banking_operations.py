import json
import random

def load_data_from_database():
    with open("customerdb.json") as f:
        db = json.load(f)
        return db

    
def register_new_user_to_database(data):
    db = load_data_from_database()
    db.append(data)
    with open("customerdb.json", "w") as f:
        json.dump(db, f)


def register():

    print("register...")

    while True:  # Regenerate account number until a new account number is not there for database
        acc_no = generate_acc_no()  #auto generate
        if not account_exist_in_db(acc_no):
            break


    name = input("name: ")
    while True:
        password = input("password:")
        print(password_check(password))

        if password_check(password) == "valid":
            break
    
    balance = 0

    register_new_user_to_database({
        "name" : name,  
        "account_number" : acc_no, 
        "password" : password,
        "balance" : balance
    }
)
    
    print("Registration Succesfull Account No = ", acc_no, "balance = ", balance)

def login():
    account_no = input("Account no: ")
    password = input("password:")

    if not account_exist_in_db(account_no):
        print("No Such Account Exists....")

    else:
        db = load_data_from_database()

        for i, user_data in enumerate(db):
            if user_data["account_number"] == account_no:
                if db[i]["password"] == password:
                    print("login to next window....")
                    user_access_window(account_no)

                else:
                    print("incorrect Password")

    
def home_window():
    print(3)
    print("----------APNA BANK---------")

    choice = input("""
    1 : Register
    2 : Login
    3 : Exit
    """)

    if choice == "1":
        register()


    elif choice == "2":
        login()

    else:
        exit()


def generate_acc_no():

    acc_no = "ab" + str(random.randint(100000, 999999))
    return acc_no

def account_exist_in_db(acc_no):
    db = load_data_from_database()

    for elem in db:
        if elem["account_number"] == acc_no:
            return True


def password_check(password):
    ulc = 0
    llc = 0
    slc = 0
    nc = 0
    sc = 0
    for elem in password:
        if elem.isupper():
            ulc += 1

        elif elem.islower():
            llc += 1

        elif elem.isdigit():
            nc += 1

        elif elem.isspace():
            sc += 1

        else:
            slc += 1

    if len(password) < 8:
        return "Password length should be greater than 8.."

    if ulc == 0:
        return "atleast one char should be in upper case"

    if llc == 0:
        return "atleast one char should be in lower case"

    if slc == 0:
        return "atleast one char should be in special char"

    if sc > 0:
        return "no space allowed in password"

    return "valid"

def check_balance(account_no):
    db = load_data_from_database()

    for user_data in db:
        if user_data["account_number"] == account_no:
            return user_data["balance"]


def deposit_balance(account_no):
    print("deposit money")

def withdraw_balance(account_no):
    user_current_balance = check_balance(account_no)

    try: 
        withdraw_amount = float(input("enter amount to withdraw: "))

        if withdraw_amount <= 0:
            print("negative balance can't be withdrwan...")

        elif withdraw_amount >= user_current_balance:
            print("insufficient fund balance...")

        else:
            print("money we will withdraw tomorrow...")
    except:
        print("invalid amount....")


def transfermoney(account_no):
    print("transfer money")

def update_password(account_no):
    print("update password")

def user_access_window(account_no):
    while True:
        choice = input("""
            1 : Check Balance
            2 : Withdraw
            3 : Deposit
            4 : Transfer Money
            5 : Password Update
            6 : Exit
            """)

        if choice == "1":
            print("Your current balance is ", check_balance(account_no))

        elif choice == "2":
            withdraw_balance(account_no)

        elif choice == "3":
            deposit_balance(account_no)

        elif choice == "4":
            transfermoney(account_no)

        elif choice == "5":
            update_password(account_no)

        elif choice == "6":
            break

        else:
            print("invalid choice try again...")