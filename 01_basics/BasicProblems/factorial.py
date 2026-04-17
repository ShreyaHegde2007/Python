num=int(input("enter a number"))
factorial=1
if num<0:
    print("factorial doesnt exist")
elif num==0:
    print("factorial is 1")
else:
    for i in range(1,num+1):
        factorial*=i
    print("factorial is",factorial)