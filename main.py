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



print(password_check("234"))