print("exercise on if else,book python crash course")
age = int(input("enter your age\n"))
if  age < 2:
    print("person is a baby")
elif age == 2 and age < 4:
    print("person is toddler")
elif age == 4 and age < 13:
    print("person is kid")
elif age == 13 and age < 20:
    print("person is a tennager")
elif age == 20 and age < 65:
    print("person is an adult")
else:
    print("person is older")
