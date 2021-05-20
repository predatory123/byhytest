while True:
    year = input("请输入您的年龄：")
    if year != 'quit':
        if int(year) > 12:
            print('门票15美元/人')
        elif 3 < int(year) <= 12:
            print('门票10美元/人')
        else:
            print('门票免费')
    else:
        break
