
value = input('请输入一个数字：')
value1 = input('请输入另一个数字：')
# number = int(value) + int(value1)
# print(number)
try:
    number = int(value) + int(value1)
    print(number)
except ValueError:
    print('无法计算结果，请输入数字哦，亲！')

