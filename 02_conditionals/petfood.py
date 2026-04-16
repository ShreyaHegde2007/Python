pet=input("enter the type of pet(cat or dog):")
age=int(input("enter the age of the pet"))
if pet=="dog":
    if age<2:
        print("puppy food")
    elif age>2 and age<=5:
        print("adult dog food")
    else:
        print("senior dog food")
elif pet=="cat":
    if age<2:
        print("kitten food")
    elif age>2 and age<=5:
        print("adult cat food")
    else:
        print("senior cat food")