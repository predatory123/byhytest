car = input('What car do you want? :  ')
print('Let me see if i can find you a '+ car)


people = int(input('请问你们有几位用餐？----：'))
if people > 8:
    print('不好意思，没有空位了')
else:
    print('这边请')

number = int(input('请输入一个数字哦：'))
if number %10 ==0:
    print('这是10的整数倍')
else:
    print('这不是10的倍数')
