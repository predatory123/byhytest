fox = 'guest_book.txt'

with open(fox,'w') as file_object:
    while True:
        name = input('请输入你的名字：')
        print('输入 quit 可退出')
        if name == 'quit':
            break
        file_object.write('\n'+ name)

with open('guest_book.txt') as file_object:
    value = file_object.read()
    print(value)