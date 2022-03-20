print("exercise 02 python crash course book,for loop in list ")
mypizzas = ['chesse pizza','chicken pizza','panner pizza']
animals = ['dog','cat','cow']
for pizzaname in mypizzas:
    print("i like" + " " + pizzaname)
for animal in animals:
    print("i would like to pet a" + " " + animal)
print("all off these are domectic animal")
friendpizzas = mypizzas[ : ]
print(mypizzas)
print(friendpizzas)
mypizzas.append('tigga pizza')
friendpizzas.append('chicken chesse pizza')
print(mypizzas)
print(friendpizzas)
