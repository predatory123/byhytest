# 创建dog类

class Dog():
    '''一次模拟i雄安狗的操作'''
    def __init__(self,name,age):
        '''初始化小狗的属性'''
        self.name = name
        self.age = age
    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print(self.name.title() + ' is now sitting')
    def roll_over(self):
        '''模拟小狗被命令时打滚'''
        print(self.name.title() + ' rolled over')

my_dog =Dog('willie',6)
my_dog.sit()
my_dog.roll_over()
print("My dog's name is " + my_dog.name.title() +'.')
print('My dog is '+ str(my_dog.age) + 'years old.' )
your_dog =Dog('lucy',3)
your_dog.sit()
your_dog.roll_over()
print("Your dog's name is " + your_dog.name.title() +'.')
print('Your dog is '+ str(your_dog.age) + 'years old.' )