# exercise 7-9
print("exercise 7-8 while loop in list,book python crash course")
ordered_sandwiches = ['salad sandwich','pastrami','potato sandwich','brown bread sandwich','pastrami','pastrami']
finished_sandwiches = []
while 'pastrami' in ordered_sandwiches:
    ordered_sandwiches.remove('pastrami')
print("We have ran out of pastrami")
print(ordered_sandwiches)
#exercise 7-8
#while ordered_sandwhiches
#     laudu = ordered_sandwiches.pop()
#     print("We have made your" + " " + laudu + " sandwhich")
#     finished_sandwiches.append(laudu)
# print(finished_sandwiches)