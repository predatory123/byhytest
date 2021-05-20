class User():
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name  = last_name
        self.age  = age
        # self.login_attpment = 1

    def describe_user(self):
        print(  'This is '+ self.first_name.title() + ', '+self.last_name+'.'
                +"it\'s " + str(self.age) +" year's old" )
    def gerrt_user(self):
        print('Hello  ' + self.first_name+self.last_name)
    # def old_login_attepment(self):
    #     print('Now there have '+ str(self.login_attpment) + ' girl')
    # def increment_login_attpment(self,value):
    #     self.login_attpment = value
    #
    # def reset_login_attpment(self,values):
    #     self.login_attpment -= values
#
# my_car = User('ducati','saten','100')
# print(my_car.describe_user())
