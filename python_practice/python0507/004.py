namelist = ['冯宝宝','张楚岚','徐三','王也']
message = namelist[0]   + ', '+'期待与你共进晚餐.'
message1= namelist[1]    + ', '+'期待与你共进晚餐.'
message2= namelist[2]    + '  , '+'期待与你共进晚餐.'
print(message)
print(message1)
print(message2)
print(namelist)
len(namelist)

print('\n因为徐三先生因开会无法赴约\n')
namelist[2] = '吕梁'
message =namelist[0]   + ', '+'期待与你共进晚餐.'
message1= namelist[1]    + ', '+'期待与你共进晚餐.'
message2= namelist[2]    + '  , '+'期待与你共进晚餐.'
print(message)
print(message1)
print(message2)

print('\n因为场地变大了，再邀请3位嘉宾\n')




namelist.insert(0,'夏禾')
namelist.append('陆玲珑')
namelist.insert(3,'王震球')
len(namelist)
print(namelist)


for name  in namelist:
    print( name+','+'期待与你共进晚餐.\n')

print('\n\n因为场地有限，只能邀请两位嘉宾\n')
name_list=namelist.pop()
print(name_list +','+ '很抱歉，无法与你共进晚餐')
name_list=namelist.pop()
print(name_list+',' + '很抱歉，无法与你共进晚餐')
name_list=namelist.pop()
print(name_list+',' + '很抱歉，无法与你共进晚餐')
name_list=namelist.pop()
print(name_list +','+ '很抱歉，无法与你共进晚餐')
name_list=namelist.pop()
print(name_list +','+ '很抱歉，无法与你共进晚餐\n')

print(namelist)

for name  in namelist:
    print( name+','+'期待与你共进晚餐.\n')

del namelist[0]
print(namelist)
del namelist[0]
print(namelist)
len(name_list)
print('最后，今晚和'+ name+'一起吃饭')



