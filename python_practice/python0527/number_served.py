class User():
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name  = last_name
        self.age  = age
        # self.login_attpment = 1
    def describe_user(self):
        # print('This is '+ self.first_name.title() + ' '+self.last_name+'.'+"it\'s " + str(self.age) +" year's old.")
        # print(self.first_name.title() + ' '+self.last_name+'.' + str(self.age))
        long_name = self.first_name + ' ' + self.last_name + ' ' + str(self.age)
        return long_name.title()

    #def gerrt_user(self):
        #print('Hello  ' + self.first_name+self.last_name)
friends= User('tom','blank',18)
# print('This is '+ self.first_name.title() + ' '+self.last_name+'.'+"it\'s " + str(self.age) +" year's old.")
print( friends.describe_user())
# print( friends.describe_user() )
# friend.gerrt_user()
#     def old_login_attepment(self):
#         print('Now there have '+ str(self.login_attpment) + ' girl')
#     def increment_login_attpment(self,value):
#         self.login_attpment = value
#
#     def reset_login_attpment(self,values):
#         self.login_attpment -= values
# friend = User('tom','blauk',18)
# print(friend.describe_user())
# friend.describe_user()
# friend.gerrt_user()
# friend.increment_login_attpment(1)
# friend.old_login_attepment()
# friend.reset_login_attpment(1)
# friend.old_login_attepment()

#
# # print('\n')
# friend1 = User('许','嵩','25')
# print('\nV领没表V领  ')
# friend1.describe_user()
# friend1.gerrt_user()
#
# '''类的继承'''
# class motocar(User):
#     def __init__(self,first_name,last_name,age):
#         super().__init__(first_name,last_name,age)
#
# my_car = motocar('ducati','saten',1000)
# print(my_car.describe_user())

