m1 = int(input("enter marks of 1 subject"))
m2 = int(input("enter marks of 2 subject"))
m3 = int(input("enter marks of 3 subject"))
if(m1<33 or m2<33 or m3<33):
    print("you are fail")
elif(m1+m2+m3)/3 <40:
    print("you are failed")
else:
    print("congratulations! you passed the exam")
