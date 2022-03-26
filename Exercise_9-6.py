print("Exercise 9-6 classes and inheritance")
class restraurants():
    """A simple attempt"""
    def __init__(self,name,type):
      self.name = name
      self.type = type
      self.number_served = 0

    def set_number_served(self,new_no):
      self.number_served = new_no
      print("The no of customers served by this restauranrt is"+" "+str(self.number_served))
    
    def increment_no_served(self,new_no):
        self.number_served += new_no
        print("The no of customers served by this restauranrt in two days is"+" "+str(self.number_served))
    
    def describe_restaurant(self):
      print("Name of the restaurant is"+" "+self.name)
      print("type of the cuisine is"+" "+self.type)
    #   print("the no of customer restsurant serve is"+" "+str(self.number_served))
    def restaurant_open(self):
      print("Restaurant is open or closed")

restaurant_1 = restraurants('angithi','a1 class')
restaurant_1.describe_restaurant()
restaurant_1.set_number_served(23)
restaurant_1.increment_no_served(23)

#child class from parent class named restaurants

class ice_cream_stand(restraurants):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavour = ['chocolate','mango','orange','vanilla','stawberry']
    def  describe_restaurant(self):
        print("Name of ice cream is"+" "+self.name)
        print("Type of the ice cream is"+" "+self.type)
    def describe_flavour(self):
        print("the flavour of ice creams available are as follows:"+" ")
        for flavour in self.flavour:
            print(flavour)
my_icecream_1 = ice_cream_stand('chocolate','bowl')
my_icecream_1.describe_restaurant()
my_icecream_1.describe_flavour()
