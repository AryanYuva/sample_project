print("Exercise 8-12 functions arbitrary arguments,book python crash course")
def make_sandwhiches(*topings): #here singe * makes a tuple variable which can hold many arguments
    print("we are adding following topings on your sandwhich")
    for topping in topings:
        print(topping)
make_sandwhiches('chesse','salad','memoies')

#Exercise 8-13 profile 

def build_profile(first_name,last_name,**user): #Here double ** makes a dictionary which can hold many arguments
    profile = {}
    profile['first'] = first_name
    profile['last'] = last_name
    for key,value in user.items():
        profile[key] = value
    return profile
comp = build_profile('albert','einstien',location='ranchi',age='34')
print(comp)

#exercise 8-14 cars

def make_car(manufacturer,model,**detail):   #Here double ** makes a dictionary which can hold many arguments
    make = {}
    make['manufacturer_name'] = manufacturer
    make['model_name'] = model
    for key,value in detail.items():
        make[key] = value
    return make
cars = make_car('audi','r8',colour='black',wheel='alloy wheel')
print(cars)
