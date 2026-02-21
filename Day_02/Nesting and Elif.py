print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("what is your age"))

if height >= 120:
    print("You can ride the rollercoaster")
    if age >= 18:
        print("you have to pay 12$.")
    elif age <= 14:
        print("you have to pay 7$.")
    elif age >= 30:
        print ("you have to pay 15$.")
    else:
        print("you have to pay 9$.")
else:
    print("Sorry you have to grow taller before you can ride.")
