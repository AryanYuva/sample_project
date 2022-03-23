print("Exercise 8-6 functions with return values,book python crash course")
def city_country(city_name,country_name):
    message = city_name + ", " + country_name
    return message.title()
formatted = city_country('ranchi','india')
print(formatted)