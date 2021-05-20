class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name  = last_name
    def describe_user(self):
        print('His name is '+ self.first_name +  self.last_name)
    def greet_user(self):
        print('Hello! '+ self.first_name +self.last_name + ' Welcome.')

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privilages = Privileges()

class Privileges():
        def __init__(self):
            self.privileges = ['can add post', 'can del post', 'can ban user']

        def show_privilages(self):
            for admin in self.privileges:
                print('Admin could: ' + admin)
Admin1 = Admin('Taylor','swift')
Admin1.privilages.show_privilages()





