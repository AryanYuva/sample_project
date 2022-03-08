# n1 = int(input("enter no 1\n"))
# n2 = int(input("enter no 2\n"))
# n3 = int(input("enter no 3\n"))
# n4 = int(input("enter no 4\n"))
# if(n1>n2 and n1>n3 and n1>n4):
#     print("n1 is greater")
# elif(n2>n1 and n2>n3 and n2>n4):
#     print("n2 is greater")
# elif(n3>n1 and n3>n2 and n3>n4):
#     print("n3 is greater")
# else:
#     print("n4 is greater")
n1 = int(input("enter no 1\n"))
n2 = int(input("enter no 2\n"))
n3 = int(input("enter no 3\n"))
n4 = int(input("enter no 4\n"))
if(n1>n4):
    f1 = n1
else:
    f1 = n4
if(n2>n3):
    f2 = n2
else:
    f2 = n3
if(f1>f2):
    print(str(f1)+ " is greatest")
else:
    print(str(f2)+ " is greatest")

