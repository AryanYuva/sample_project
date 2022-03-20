print("exercise 5-8 list if statement,book python crash course")
current_user = ['mahesh','admin','surya','niel','michal']
new_user = ['varun','mahesh','vijay','bunny','surya']
for us in current_user:
        if us in new_user:
            print("username not available,plese enter another user name")
        else:
            print("username available")
