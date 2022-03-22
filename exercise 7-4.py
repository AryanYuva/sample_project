print("Enter the 7-4 while loop pizza toppings,book python crash course")
message = " "
active = True
while active:
    message = input("Enter the toppings youn want in your pizza\n")
    if message != 'quit':
        print("We are adding" + " " + message + " " + "toppings on your pizza")
    elif message == 'quit':
        active = False
