while True:
    number = input('请输入一个数字：')
    value = input('请在输入一个数字')
    try:
        result = int(number) + int(value)
        print(result)
        break

    except ValueError:
        print('你娃儿输错了哦')