from asyncore import write
from re import A
from tkinter import W


print("Exercise 10_3")
with open('guest.txt','a') as file_object:
    file_object.write(input("enter your name\n"))
active_pool = True
with open('guest.txt','a') as file_object:
    while active_pool:
       file_object.write(input("enter your name\n"))
       message = input("do you want to enter more no of names(yes/no)\n")
       if message == 'no':
           active_pool = False
print("your respond is submitted")
