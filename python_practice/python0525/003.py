'''一，直接修改属性的值'''
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
#调用类和方法
my_new_car = car('Audi','RS7',2019)
print(my_new_car.get_desciptive_name())
my_new_car.odometer_reading = 5000
my_new_car.road_odometer()