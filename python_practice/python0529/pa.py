from user912 import User
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

my_name = User('AA','BB')
my_name.describe_name()