marks = int(input("enter the marks"))
if(marks>=90 ):
   grade="EX"
elif(marks>=80 ):
   grade= "A" 
elif(marks>=70 ):
   grade= "B"
elif(marks>=60 ):
   grade= "C"
elif(marks>=50 ):
    grade="D"
else:
    grade="F"
print("your grade is" + grade)
     