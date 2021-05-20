with open("guest_book.txt", "a") as file_object:
   while True:
      name = input("Please enter your name:\nEnter 'quit' to quit at any time.")
      if name == "quit":
         break
      print("Hello " + name.title() + "!")
      file_object.write(name.title() + "\n")
with open('guest_book.txt') as file_object:
    aaa = file_object.read()
    print('这个文档里面有：')
    print(aaa)
# # while True:
# message = '请输入用户名：'
# # value = '你好: ' + message + ' 欢迎你的到来'
# # print(value)
# #     if message == '':
# #         break
#
# with open('guest_book.txt', 'a') as file_object:
#         file_object.write(input(message))
#
#         # file_object.write(input(value))
#
# with open('guest_book.txt') as file_object:
#     aaa = file_object.read()
#     print('这个文档里面有：')
#     print(aaa)