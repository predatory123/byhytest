vlaue = 'cats.txt'
with open(vlaue,'w') as file_object:
    file_object.write('jake\n')
    file_object.write('love\n')
    file_object.write('rose\n')

with open('cats.txt') as file_object:
    store = file_object.read()
    print(store)