marital_status = input("Enter marital status married or unmarried: ").lower()

if marital_status == "married":
    print("Driver is insured.")
else:
    gender = input("Enter gender male or female: ").lower()
    age = int(input("Enter age: "))

    if gender == "male" and age > 30:
        print("Driver is insured.")
    elif gender == "female" and age > 25:
        print("Driver is insured.")
    else:
        print("Driver is not insured.")