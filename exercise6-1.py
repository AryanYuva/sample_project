print("exercise 6-1 dictionary, book python crash course")
infodict_01 = {'first_name': 'mahesh' ,'last_name': 'babu','age': '18','city':'ranchi'}
infodict_02 = {'first_name':'prabhas','last_name':'gonda','age':'23','city':'jamsedhpur'}
people = [infodict_01,infodict_02]
for infodict in people:
    print(infodict['first_name'])
    print(infodict['last_name'])
    print(infodict['age'])
    print(infodict['city'])
favno = {'mahesh':'23','surya':'3','varun':'5','prabhas':'13','ranbeer':'21'}
print("favorite no of mahesh is"+" "+favno['mahesh'])
print("favorite no of surya is"+" "+favno['surya'])
print("favorite no of varun is"+" "+favno['varun'])
print("favorite no of prabhas is"+" "+favno['prabhas'])
print("favorite no of ranbeer is"+" "+favno['ranbeer'])