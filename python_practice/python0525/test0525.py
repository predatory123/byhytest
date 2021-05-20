class User():
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name  = last_name
        self.age  = age

    def describe_user(self):
        print('This is '+ self.first_name.title() + self.last_name+'.'+"it\'s " + str(self.age) +" year's old")

    def gerrt_user(self):
        print('Hello  ' + self.first_name+self.last_name)

friend = User('tom','blauk','18')
print(666)
friend.describe_user()
friend.gerrt_user()
# print('\n')
friend1 = User('许','嵩','25')
print('\nV领没表V领  ')
friend1.describe_user()
friend1.gerrt_user()