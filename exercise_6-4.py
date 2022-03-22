print("exercise 6-4 glossary using for loop in dictionary,book python crash course")
gloss_dict = {'arms':'weapon','bold':'strong','chat':'talking','dig':'khodna','energy':'capability'}
for word, meaning in gloss_dict.items():
    print("word: " + word)
    print("meaning: " + meaning)
#three major river dictionary and looping exercise 6-5
rivr_dict = {'ganga':'india','indus':'pakistan','nile':'egypt'}
for river,country in rivr_dict.items():
    print("The" + " "+ river + " " + "flows through" + " " + country)
print("all river name participated in poll")
for river in rivr_dict.keys():
    print(river)
print("All the country taking part in pool")
for country in rivr_dict.values():
    print(country)
