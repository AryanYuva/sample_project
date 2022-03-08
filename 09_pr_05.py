def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()
this = "    aryan is a good     "
n = remove_and_split(this,"aryan")
print(n)
# print(this)
# print(this.strip())
