'''通过方法对属性的值进行递增'''
class Car():
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
    def read_odometer(self):
        print('This car has '+str(self.odometer_reading) +' miles on it.' )
#指定里程的值
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
#对里程增加指定的量
    def incrment_odometer(self,miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + 'kwh battery')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += "miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery= Battery()


my_audi = ElectricCar('audi','a8',2019)
my_audi.battery.get_range()
my_audi.battery.upgrade_battery()
my_audi.battery.get_range()

