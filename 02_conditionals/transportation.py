d=int(input("enter the distance"))
if d<3:
    print("walk",d)
elif d>=3 and d<15:
    print("bike",d)
else:
    print("car",d)