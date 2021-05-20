class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name  = last_name
        self.login_attempts = 0
    def describe_user(self):
        print('His name is '+ self.first_name +  self.last_name)
    def greet_user(self):
        print('Hello! '+ self.first_name +self.last_name + ' Welcome.')
    def login_attpments(self):
        print('There have ' + str(self.login_attempts) + ' people is logined.')
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

tom = User('jake','rose')
tom.increment_login_attempts()
tom.login_attpments()
tom.reset_login_attempts()
tom.login_attpments()