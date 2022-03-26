print("Exercise 9-8 class as an atribute,book python crash course")
class priviliges():
    def __init__(self,privilages):
        self.privilage = privilages
    # def change_privilage(self,privilages):
    #     self.privilage = privilages
    def show_privilages(self):
        print("All the privillages admin have are as follows:")
        for privilage in self.privilage:
            print(privilage)
my_privilage = priviliges(privilages=['can add user','can remove user','can ban user'])
# my_privilage.change_privilage(privilages=['can ban user'])
my_privilage.show_privilages()

class admin():
    def __init__(self, f_name, l_name, location):
          self.firstname = f_name
          self.lastname = l_name
          self.located = location
          self.privilige = priviliges(privilages=['can report user'])

    def describe_user(self):
         print("\nFirst name of user is"+" "+self.firstname)
         print("\nlast name of user is"+" "+self.lastname)
         print("\nLocation of user is"+" "+self.located)


    # def show_privillages(self):
    #     print("All the privillages are as follows")
    #     for privillage in self.privillages:
    #         print(privillage)
            
admin_1 = admin('Aryan','Dubey','Ranchi')
admin_1.describe_user()
admin_1.privilige.show_privilages()
