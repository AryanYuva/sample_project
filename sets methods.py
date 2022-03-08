b = set()
print(b)
print(type(b))
#Adding values to an empty set
b.add(4)
b.add(5)
b.add((4,5,6))#tuple can be added to sets
#b.add({4:5})#cannot add list or dictionary to sets
b.remove(5) # Removes 5 from the set b
#b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(b)
print(b.pop())
