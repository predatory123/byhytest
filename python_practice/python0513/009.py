message ='请输入您的年龄：'
while message != 'quit':
    year = input(message)
    if year == 'quit':
       break
    else:
        year=int(year)
        if year >12:
            print('门票15美元/人')
        elif 3 < year <= 12:
            print('门票10美元/人')
        elif year < 3:
            print('门票免费')