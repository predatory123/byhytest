# 定义一个类
class Restuarant():
    def __init__(self,restuarnt_name,cuisine_type):
# 定义类的属性
        self.restuarant_name = restuarnt_name
        self.cuisine_type = cuisine_type
# 定义类的方法
    def decsribe_restuarant(self):
        print('The '+self.restuarant_name +'restuarant have '+self.cuisine_type + ' list.')
    def open_restuarant(self):
        print('This restuarant is opening')

my_restuarant = Restuarant('俏江南','江南style')
print('This is '+ my_restuarant.restuarant_name + '. This is his list: '+my_restuarant.cuisine_type)
my_restuarant.decsribe_restuarant()
my_restuarant.open_restuarant()
print('\n')
your_restuarant = Restuarant('小南国','south style')
print('This is '+ your_restuarant.restuarant_name + '. This is his list: '+your_restuarant.cuisine_type)
your_restuarant.decsribe_restuarant()
# your_restuarant.open_restuarant()
print('\n')
his_restuarant = Restuarant('湘粤情','gold style')
print('This is '+ his_restuarant.restuarant_name + '. This is his list: '+his_restuarant.cuisine_type)
his_restuarant.decsribe_restuarant()
# his_restuarant.open_restuarant()