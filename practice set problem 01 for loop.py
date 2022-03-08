#multiplication table of a no
n = int(input("enter the no for which you want multiplication table"))
for i in range(11):
    # print(str(n)  +  "X"  +  str(i)  +  "="  +  str(i*n))
    # how to use f string
    print(f"{n}*{i}={n*i}")