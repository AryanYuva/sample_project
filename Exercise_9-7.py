class users():
    """attempt to make a class of user"""
    def __init__(self,f_name,l_name,location):
        self.firstname = f_name
        self.lastname = l_name
        self.located = location
        self.login = 0
    
    def incriment_loginattempts(self,loginattemps):
        self.login += loginattemps
        print("Now your login attempt is"+" "+str(self.login))
    
    def reset_loginattempts(self):
        self.login = 0
        print("Now your login attempt is reset to"+" "+str(self.login))
    def describe_user(self):
         print("\nFirst name of user is"+" "+self.firstname)
         print("\nlast name of user is"+" "+self.lastname)
         print("\nLocation of user is"+" "+self.located)
    def greet_user(self):
        print("Hello"+" "+self.firstname+" "+self.lastname+",how are you today")
user_info = users('Aryan','dubey','ranchi')
user_info.describe_user()      
user_info.greet_user()
user_info.incriment_loginattempts(1)
user_info.incriment_loginattempts(1)
user_info.incriment_loginattempts(1)
user_info.reset_loginattempts()

user_info_1 = users('nihu','pandey','dhurwa')
user_info_1.describe_user()
user_info_1.greet_user()

user_info_2 = users('allu','arjun','vijayvada')
user_info_2.describe_user()
user_info_2.greet_user()

class admin(users):
    def __init__(self, f_name, l_name, location):
        super().__init__(f_name, l_name, location)
        self.privillages = ['can add post','can delete post','can add user']

    def describe_user(self):
         print("\nFirst name of user is"+" "+self.firstname)
         print("\nlast name of user is"+" "+self.lastname)
         print("\nLocation of user is"+" "+self.located)

    def show_privillages(self):
        print("All the privillages are as follows")
        for privillage in self.privillages:
            print(privillage)
            
admin_1 = admin('Aryan','Dubey','Ranchi')
admin_1.describe_user()
admin_1.show_privillages()