'''通过方法对属性的值进行递增'''
class car():
    def __init__(self,make,model,year):
# 描述汽车的3个属性
        self.make = make
        self.model = model
        self.year = year
#新增一个属性,里程数
        self.odometer_reading = 0
#定义一个汇总信息的方法
    def get_desciptive_name(self):
        long_name = str(self.year) +  ' ' + self.make + ' ' + self.model
        return long_name.title()
#打印里程数信息
    def road_odometer(self):
        print('This car has '+str(self.odometer_reading) +' miles on it.' )
#指定里程的值
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
#对里程增加指定的量
    def incrment_odometer(self,miles):
        self.odometer_reading += miles

#调用类和方法
# my_new_car = car('Audi','RS7',2019)
# print(my_new_car.get_desciptive_name())
#
# my_new_car.update_odometer(1000)
# my_new_car.road_odometer()
#
# my_new_car.incrment_odometer(500)
# my_new_car.road_odometer()

# 继承类和方法
class new_car(car):
    def __init__(self,make,model,year):
        super.__init__(make,model,year)
my_new_car = car('Audi','RS3',2019)
print(my_new_car.get_desciptive_name())

