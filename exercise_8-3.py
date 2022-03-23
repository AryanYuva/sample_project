print("Exercise 8-3 functions,book python crash course")
def make_shirt(shirt_size ,print_on_shirt):
    print("you have ordered a shirt of size" + " " + shirt_size + " and your message to get printed on shirt is" + " " + print_on_shirt.title())
make_shirt(shirt_size = 'L' ,print_on_shirt = 'I Love Python')

#exercise 8-4 functions by default

def make_shirt(shirt_size = 'm' ,print_on_shirt = 'i am kid'):
    print("you have ordered a shirt of size" + " " + shirt_size + " and your message to get printed on shirt is" + " " + print_on_shirt.title())
make_shirt()

#exercise 8-5 functions describe city

def describe_city(city_name,country_name = 'india'):
    print(city_name + " " + "Is in" + " " + country_name)
describe_city('ranchi')
describe_city('jamsedhpur')
describe_city(city_name='laudu',country_name='bhitran pur')