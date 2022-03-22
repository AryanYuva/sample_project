print('exercise 6-6 dictionary looping, book python crash course')
nm_dict = {'mahesh':'python','varun':'c','surya':'c++','prabhas':'java','aryan':'html'}
nm_list = ['ram','varun','allu']
for name in nm_list:
    if name in nm_dict:
        print("Hello" + " " + name + " " + "thanks for responding")
    else:
        print("Hello" + " " + name + " " + "please take a pool")