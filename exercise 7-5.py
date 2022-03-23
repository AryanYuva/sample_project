print("Exercise 7-5 while loop,book python crash course")
message = " "
active = True
while active:
    age = int(input("enter your age and i will tell you how much amount you have to pay\n"))
    if age <= 3:
        print("no need to pay")
    elif age >= 3 and age <= 12:
        print("you have to pay $10")
    elif age >= 12:
        print("you have to pay $15")
    message = input("If you dont want to continue enter quit otherwise press any key to continue\n")
    if message == 'quit':
       break