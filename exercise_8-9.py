def show_magicians(magicians):
    for magician in magicians:
        print(magician)
magicians = ['gogiya sarkar','vijay lakra','jack king']
show_magicians(magicians)

#Exercise 8-10 modify list

# def make_great(magicians):
#     while magicians:
#       new = magicians.pop()
#       print("Great"+" "+new)
# make_great(magicians)
# show_magicians(magicians)

#exercise 8-11 functions unchanged list

mew_magicians = magicians[:]
def make_great(new_magicians):
    while new_magicians:
        new = new_magicians.pop()
        print("great"+" "+new)
make_great(magicians[:])
show_magicians(magicians)
      
