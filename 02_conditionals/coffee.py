order_size=input("enter the size of coffee (small,meduim or large):")
coffee_shot=input("enter if you need an expresso shot(yes/no):")
if coffee_shot=='yes':
    coffee=order_size+"with extra shot of expresso"
else:
    coffee=order_size+"coffee"
print(coffee)
