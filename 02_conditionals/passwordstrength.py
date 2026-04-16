p=input("enter the number of characters:")
if len(p)<6:
    print("password is weak")
elif len(p)<10:
    print("password is medium")
elif len(p)>10:
    print("password is strong")