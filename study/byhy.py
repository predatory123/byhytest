welcome = '''

    ########################################
    #                                      #
    #     白月黑羽 PyInstaller 演示程序    #
    #                                      #
    ########################################

'''

print(welcome)

while True:
    exp = input('\n\n请输入一个数学运算式 [输入quit退出]：')
    if exp == 'quit':
        break
    try:
        result = eval(exp)
    except:
        print('\n！！无效的运算式')
        continue

    print(f'结果为: {result}')