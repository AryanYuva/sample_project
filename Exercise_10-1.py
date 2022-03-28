print("Exercise 10-1,book python crash course")
with open('python.txt') as file_object:
    content = file_object.read()
    print(content)
    print(content.replace('ara','rohtash'))

with open('python.txt') as file_object:
    for line in file_object:
       print(line.rstrip())

with open('python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)
    