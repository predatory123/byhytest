yuyan ='reason.txt'
with open('reason.txt','w') as file_object:
    while True:
        reason = input('你为什么喜欢编程？---- ')
        if reason =='':
            break
        file_object.write('\n'+reason)

with open('reason.txt') as file_object:
    opop = file_object.read()
    print(opop)
