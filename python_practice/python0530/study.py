with open('learn.txt') as file_object:
    contents = file_object.read()
    print('第一次打印')
    print(contents)

with open('learn.txt') as file_object:
    print('第二次打印')
    for line in file_object:
        print(line.rstrip())

with open('learn.txt') as file_object:
    lines = file_object.readlines()
print('第三次打印')
for value in lines:
    print(value.strip())

