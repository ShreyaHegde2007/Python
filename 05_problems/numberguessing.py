import random
guess_the_number=random.randint(1,100)
while True:
    guess=int(input("enter a number"))
    if guess>guess_the_number:
        print("its too high")
    elif guess<guess_the_number:
        print("its too low")
    else:
        print("congragulations")
        break