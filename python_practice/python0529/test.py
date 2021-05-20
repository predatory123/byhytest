class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.yaer = year
        self.odometer_raeding = 0

    def get_discriptive_name(self):
        long_name = str(self.yaer) + ' '+ self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+ str(self.odometer_raeding)+ ' miles on it.')

    def update_odometer(self,mileage):
        if mileage >= self.odometer_raeding:
            self.odometer_raeding =  mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_raeding += miles

class Battery():
    '''一次模拟电动汽车电瓶的简简单尝试'''
    def __init__(self, battery_size =70):
        '''初始化电瓶的属性'''
        self.battery_size= battery_size

    def describe_battery(self):
        print('This car has a '+ str(self.battery_size)+ '-kmh battery.')

    def get_range(self):
        if self.battery_size == 70:
            range =240
        elif self.battery_size == 85:
            range =270

        message = 'This car can go approximately '+ str(range)
        message += 'miles on a full charge.'
        print(message)

    def upgrade_battery(self):
        """检查电瓶容量"""
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla','model s',2019)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


