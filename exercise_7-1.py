print("exercise 7-1 input function,book python crash course")
car = input("enter the rental car you are searching for")
print("Let me see if i can find you a" + " " + car)

#ecercise 7-2

no_people = int(input("please say how many people are there in your dinner group: "))
if no_people > 8:
    print("you have to wait")
else:
    print("your table is ready")

#Exercise 7-3

no_check = int(input("Enter a no i will tell you whether the no is multiple of ten or not"))
if no_check % 10 == 0:
    print("no is multible of ten")
else:
    print("no is not a multiple of ten")