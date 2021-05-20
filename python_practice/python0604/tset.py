try:
    with open('ca.txt') as cat:
        print(cat.read())
    with open('dogs.txt') as dog:
        print(dog.read())
except FileNotFoundError:
    # print('对不起没有找到文件')
    pass
