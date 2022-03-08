myDict = {
"pankha": "fan",
"kursi": "table",
"kalam": "pen",
"kitab": "book",
}
print("options are",myDict.keys())
a = input("enter the hindi word\n")
print("the meaning of your word is:",myDict.get(a))
