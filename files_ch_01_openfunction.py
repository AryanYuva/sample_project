#use open function to read the content of a file!
f = open('sample.txt', 'r') # by default open function read
data = f.read(5) #first 5 character of file
data= f.readline() #read the line of file
print(data)
f.close()