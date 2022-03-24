class restraurants():
    """A simple attempt"""
    def __init__(self,name,type):
      self.name = name
      self.type = type
    def describe_restaurant(self):
      print("Name of the restaurant is"+" "+self.name)
      print("type of the cuisine is"+" "+self.type)
    def restaurant_open(self):
      print("Restaurant is open or closed")


restaurant_1 = restraurants('angithi','a1 class')
print(restaurant_1.name)
print(restaurant_1.type)
restaurant_1.describe_restaurant()
restaurant_1.restaurant_open()

#Exercise 9-2 make 3 more intances from the class restaurants

restaurant_2 = restraurants('sheetal agni','not good enough')
restaurant_2.describe_restaurant()

restaurant_3 = restraurants('kaveri','average good')
restaurant_3.describe_restaurant()