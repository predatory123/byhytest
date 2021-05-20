class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name  = last_name
    def describe_user(self):
        print('His name is '+ self.first_name +  self.last_name)
    def greet_user(self):
        print('Hello! '+ self.first_name +self.last_name + ' Welcome.')

aaa = User('tom','smith')
aaa.describe_user()
aaa.greet_user()
print('\n')
bbb =User('bob','alick')
bbb.describe_user()
bbb.greet_user()
print('\n')
ccc = User('taylor','swift')
ccc.describe_user()
ccc.greet_user()