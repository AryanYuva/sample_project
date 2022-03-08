with open ("sample.txt") as f:
    content = f.read()

content = content.replace("donkey","s@sssss%")

with open ("sample.txt", 'w') as f:
    content = f.write(content)