a=int(input("enter the number"))
if a<13:
    print("a is a child")
elif a>12 and a<20:
    print("a is a teenager")
elif a>19 and a<60:
    print("a is an adult")
else:
    print("a is a senior")