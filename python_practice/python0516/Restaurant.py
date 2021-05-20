class Restaurant():  #定义一个  饭店 类
    def __init__(self,restaurant_name,cuisine_type):   # 初始化属性 name 和 type，定义一个方法
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):       #定义其中一个方法
        print('This restaurant\'s name is ' +self.restaurant_name.title()+','+'and they have '+self.cuisine_type)
    def open_restaurant(self):           # 定义另一个方法
        print('The'+self.restaurant_name +'is opening.')
# 调用 饭店 类
my_restaurant = Restaurant('俏江南','biue list')
print('这是一个好饭店啊！他的名字是 '+ my_restaurant.restaurant_name.title() +'.'+'他的菜单是: '+my_restaurant.cuisine_type )
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_resturant= Restaurant('Small South','gold')
print('这是一个好饭店啊！他的名字是 '+ your_resturant.restaurant_name.title() +'.'+'他的菜单是: '+ your_resturant.cuisine_type )
your_resturant.describe_restaurant()
your_resturant.open_restaurant()
