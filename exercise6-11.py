print("exercise 6-11 dictionary nesting dictionary,book python crash course")
city_info = {
'ranchi':{
'population':'200000','country':'india','fact':'good climate'
},
'jamsedhpur':{
'population':'3000000','country':'india','fact':'industrial area'
}
}
for city,information in city_info.items():
    print("for" + " " + city + " "  + "the information stored is as follows")
    population = (information['population'])
    city = (information['country'])
    fact = (information['fact'])
    print(population)
    print(city)
    print(fact)
