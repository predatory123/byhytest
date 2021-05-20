#定义一个汽车类
class car():
    def __init__(self,make,model,year):
# 描述汽车的3个属性
        self.make = make
        self.model = model
        self.year = year
#定义一个汇总信息的方法
    def get_desciptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
#调用类和方法
class new_car(car):
    def __init__(self,make,model,year):
        super.__init__(make,model,year)
my_new_car = car('Audi','RS3',2019)
print(my_new_car.get_desciptive_name())

