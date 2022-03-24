class users():
    """attempt to make a class of user"""
    def __init__(self,f_name,l_name,location):
        self.firstname = f_name
        self.lastname = l_name
        self.located = location
    def describe_user(self):
         print("\nFirst name of user is"+" "+self.firstname)
         print("\nlast name of user is"+" "+self.lastname)
         print("\nLocation of user is"+" "+self.located)
    def greet_user(self):
        print("Hello"+" "+self.firstname+" "+self.lastname+",how are you today")
user_info = users('Aryan','dubey','ranchi')
user_info.describe_user()      
user_info.greet_user()

user_info_1 = users('nihu','pandey','dhurwa')
user_info_1.describe_user()
user_info_1.greet_user()

user_info_2 = users('allu','arjun','vijayvada')
user_info_2.describe_user()
user_info_2.greet_user()