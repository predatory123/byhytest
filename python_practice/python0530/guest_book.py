message = input('请输入用户名：')
value = 'guest_book.txt'
with open(value,'w') as file_object:
    file_object.write(message)
with open('guest_book.txt') as file_object:
    aaa = file_object.read()
    print('这个文档里面有：')
    print(aaa)