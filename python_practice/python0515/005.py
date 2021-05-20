# 使用位置实参和任意数量实参
def make_pizza(size,*toppings):
    print('\nMaking a'+str(size)+'-inch pizza with the following toppings:')
    for topping in toppings:
        print('-'+topping)

make_pizza(15,'bnanan')
make_pizza(16,'apple','cendy','rice')



