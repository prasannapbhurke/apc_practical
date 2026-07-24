married = input("Enter marital status (married/unmarried): ").lower()

if married == "married":
    print("Driver is insured")
else:
    gender = input("Enter gender (male/female): ").lower()
    age = int(input("Enter age: "))

    if gender == "male" and age > 30:
        print("Driver is insured")
    elif gender == "female" and age > 25:
        print("Driver is insured")
    else:
        print("Driver is not insured")




