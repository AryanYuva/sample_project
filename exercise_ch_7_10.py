print("exercise 7-10 while loop in dictionary,book python crash course\n")
responses = {}
poll_active = True
while poll_active:
    name = input("What is your name\n")
    response = input("Enter a place where you want to go\n")
    responses[name] = response
    message = input("is any other person want to enter there response?(yes/no)\n")
    if message == 'no':
        poll_active = False
# for name,response in responses.items():
print(responses)
