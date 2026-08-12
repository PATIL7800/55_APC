password = input("Enter password: ")

if (len(password) >= 8 and
    any(ch.isupper() for ch in password) and
    any(ch.islower() for ch in password) and
    any(ch.isdigit() for ch in password) and
    any(not ch.isalnum() for ch in password)):

    print("Valid Password")
else:
    print("Invalid Password")