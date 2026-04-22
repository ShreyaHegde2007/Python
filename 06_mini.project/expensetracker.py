print("Welcome to the Expense Tracker")
while True:
    print("1. Add Expense")
    print("2. View  all Expenses")
    print("3. View total Expenses")
    print("4. Exit")
    break
choice=int(input("Enter your choice:"))
for i in range(1,5):
    if choice==i:
        break   
if choice==1:
    expense_name=input("Enter the name of the expense:")
    expense_amount=int(input("Enter the amount of the expense:"))
    print("Expense added successfully")
elif choice==2:
    print("All expenses:")
    print("1. Food: 10/-")
    print("2. Transport: 20/-")
    print("3. Entertainment: 30/-")
elif choice==3:
    print("Total expenses: 60/-")
else: 
    print("Exiting the Expense Tracker")