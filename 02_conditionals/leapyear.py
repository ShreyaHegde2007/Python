l=int(input("enter the year"))
if (l%400==0) or (l%100!=0 and l%4==0):
    print("l is a leap year")
else:
    print("l is not a leap year")