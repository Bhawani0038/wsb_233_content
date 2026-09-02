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
    print("login...")

    
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


