fruit=input("enter the type of fruit")
colour=input("enter the colour of the fruit")
if fruit=="banana":
    if colour=="green":
        print("the fruit is unripe")
    elif colour=="yellow":
        print("the fruit is ripe")
    else:
        print("the fruit is overripe")
else:
    print("NA")