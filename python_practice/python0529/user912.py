class User():
    """docstring for User"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_name(self):
        print("fitst_name :", self.first_name, " last_name: ", self.last_name)

    def greet_user(self):
        print("hello, ", self.first_name, " ", self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
