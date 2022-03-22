print("exercise 6-7 nesting dictionary in list, book python crash course")
print("exercise 6-1 dictionary, book python crash course")
infodict_01 = {'first_name': 'mahesh' ,'last_name': 'babu','age': '18','city':'ranchi'}
infodict_02 = {'first_name':'prabhas','last_name':'gonda','age':'23','city':'jamsedhpur'}
people = [infodict_01,infodict_02]
for infodict in people:
    print(infodict['first_name'])
    print(infodict['last_name'])
    print(infodict['age'])
    print(infodict['city'])
#exercise 6-8 nesting dictionary in list
jojo = {'animal_kind':'germanshephered dog','owners_name':'abhishekh tiwary'}
chunky = {'animal_kind':'pomerian bitch','owners_name':'anuj'}
pets = [jojo,chunky]
for pet in pets:
    print(pet['animal_kind'])
    print(pet['owners_name'])

#exercise 6-9 nesting  list in dictionary

favourate_places = {'mahesh':['ranchi','jamsedhpur','mumbai'],'allu':['vijayvada','andhra','bihar'],'prabhas':['mahismati','sultanpur']}
for name,places in favourate_places.items():
    print("information for" + " " + name + " " +  "is as folowing")
    for place in places:
        print(place)
#exercise 6-10 nesting list in dictionary
fav_no = {'ram':[1,2,3,4,5],'shyam':[6,7,8,9,10],'ghnshyam':[11,12,13,14,15]}
for nm,nos in fav_no.items():
    print("Favourate no for" + " " + name + " " + " is as following")
    for no in nos:
        print(no) 