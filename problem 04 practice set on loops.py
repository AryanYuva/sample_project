n = int(input("enter any no\n"))
prime = True
for i in range(2, n):
    if(n%i == 0):
        prime = False
        break
    
if prime:
        print("this is prime")
else:
        print("this number is not prime")
