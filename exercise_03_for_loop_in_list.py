print("exercise 03 for loop in list, python crash course book")
millionlist = list(range(1,10000001))
print(min(millionlist))
print(max(millionlist))
print(sum(millionlist))
oddnumbers = list(range(1,21,2))
for oddnumber in oddnumbers:
    print(oddnumber)
multiples = []
for i in range(3,31):
    mult = 3 * i
    multiples.append(mult)
for multiple in multiples:
    print(multiple)
cubes = [values**3 for values in range(1,11)] #list comprehension method
print(cubes)