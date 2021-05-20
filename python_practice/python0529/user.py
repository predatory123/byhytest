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


class Privileges():
    """docstring for Privileges"""

    def __init__(self):
        self.privileges = ['can add post', 'can ban user', 'can delete post']

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    """docstring for Admin"""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

    def show_privileges(self):
        self.privileges.show_privileges()


