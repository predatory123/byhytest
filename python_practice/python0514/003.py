list = {}
place = True
while place :
    name = input('你叫什么名字?____')
    paly = input('你心中的度假胜地是哪里？___')
    list[name] = paly
    replace = input('还有其他人需要调查吗？(yse or no)____')
    if replace =='no':
        place = False
        break
print('\n调查结果如下：')
for name,paly in list.items():
    print(name+' 心中的度假胜地是：'+paly)