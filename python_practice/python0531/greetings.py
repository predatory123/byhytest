with open('guest_book.txt','a') as file_object:
    while True:
        name = input('请输入你的名字' + '\n'+'欢迎你的到来')
        if name =='quit':
            break
        file_object.write('\n'+ name)

with open('guest_book.txt') as file_object:
    value = file_object.read()
    print(value)