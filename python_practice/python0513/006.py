message ='请输入您的年龄：'
while message != 'quit':
    year = input(message)
    if year == 'quit':
        break
    else:
        if int(year) >12:
            print('门票15美元/人')
        elif 3<=  int(year) <=12:
            print('门票10美元/人')
        else:
            print('门票免费')




