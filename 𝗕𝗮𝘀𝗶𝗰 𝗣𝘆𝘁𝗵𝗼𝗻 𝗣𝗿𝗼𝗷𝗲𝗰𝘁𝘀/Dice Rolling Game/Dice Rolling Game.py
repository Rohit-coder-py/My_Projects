import random

a = [1,2,3,4,5,6]
b= [1,2,3,4,5,6]

first = random.choice(a)
second = random.choice(b)
while True:
    print("Please enter 'yes' or 'no'")
    choose=input('Do you want to roll the dice:')

    if choose.lower()=="yes":
        print("Dice Rolled....")
        print(f"Result:({first},{second})")
    elif choose.lower()=="no":
        print("Thanks for playing")
    else:
        print("Invaild Choice! Please Enter only Yes OR NO ")
