class Restuarant():
    def __init__(self,restuarnt_name,cuisine_type):
# 定义类的属性
        self.restuarant_name = restuarnt_name
        self.cuisine_type = cuisine_type
# 增加属性number_saved，并且设置默认值 0
        self.number_served = 0
# 增加属性people_served,并且设置默认值 0
        self.people_served = 0
# 定义类的方法
    def decsribe_restuarant(self):
        print('The '+self.restuarant_name +'restuarant have '+self.cuisine_type + ' list.')
    def open_restuarant(self):
        print('This restuarant is opening')
# 定义函数people，并打印number_saved的值
    def people(self):
        print('There have '+ str(self.number_served) + ' people comed.')
# 修改 number_saved 属性的值
    def people_new(self,values):
        self.number_served = values
# 设置一个就餐人数
    def set_people(self):
        print('There hava ' + str(self.people_served) + ' eatting.')
# 改变就餐人数的值
    def set_number_served(self,numbers):
        self.people_served = numbers
# 添加时就餐人数递增的方法
    def increment_number_served(self,value):
        self.people_served += value


my_restuarant = Restuarant('俏江南','江南style')
my_restuarant.people_new(200)
my_restuarant.people()
my_restuarant.set_number_served(20)
print('\n')
your_restuarant = Restuarant('小南国','south')
your_restuarant.increment_number_served(250)
your_restuarant.set_people()


