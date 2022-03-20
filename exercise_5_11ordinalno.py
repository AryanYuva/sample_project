print("exercise 5-11 ordinal ending no,book python crash course")
nolist = [1,2,3,4,5,6,7,8,9]
for no in nolist:
    if no == 1:
        print(str(no) + "st")
    elif no == 2:
        print(str(no) + 'nd')
    elif no == 3:
        print(str(no) + "rd")
    else:
        print(str(no) + "th")
