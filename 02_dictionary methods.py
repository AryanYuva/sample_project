myDict = {
"fast": "in a quick manner",
"aryan": "a coder",
"marks":[1,2,5],
"anotherdict": {'aryan': 'player'},
1 : 2
}
print(myDict.keys()) #print the keys of the dictionary
print(myDict.values()) #print the values of dictionary
print(myDict.items()) # print the keys,values for all contents of dictionary
print(myDict)
updateDict = {
"lovish": "friend",
"divya": "friend",
"shubham":"friend",
"aryan": "a dancer"
}
myDict.update(updateDict) #updates the dictionary by adding key,value pairs from updatedict
print(myDict)
print(myDict.get("aryan2")) # returns none as harry 2 is not present in dictionary
#print(myDict["aryan2"]) # throws an error as aryan2 is not present in the dictionary