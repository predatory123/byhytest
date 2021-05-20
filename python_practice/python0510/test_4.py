# 创建一个10以内数字的立方列表
numbers = []
for value in range(1,11):
    number = value**3
    numbers.append(number)
print(numbers)

#  使用列表解析，生成1到10的立方列表
number1 =[values**3 for values in range(1,11)]
print(number1)

