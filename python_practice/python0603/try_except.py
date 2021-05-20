with open('cats.txt') as file_object:
    try:
        name = file_object.read()
        print(name)
    except FileNotFoundError:
        print('小伙子，你的文件不见啦')