# 1.调用整个模块
import Function
name_message = Function.build_profile('angel','bob',ccc='de',funny='gh')
print(name_message)

# 2.调用模块中的函数
from Function import build_profile
name = build_profile('angel','bob',ccc='de',funny='gh')
print(name)

#3.给函数指定别名
from Function import build_profile as bp
name = bp('angel','bob',ccc='de',funny='gh')
print(name)

# 4.给模块指定别名
import Function as fu
name_message = fu.build_profile('angel','bob',ccc='de',funny='gh')
print(name_message)

#5.调用模块中的所有函数
from Function import *
name_message = build_profile('angel','bob',ccc='de',funny='gh')
print(name_message)



