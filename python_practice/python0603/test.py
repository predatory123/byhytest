with open('cats.txt', 'a') as file_object:
    print ('If you want to quit , please entert "q".')
    while True:
        cats_name = input('Please enter your cat\'s name:')
        if cats_name == 'q':
            break
        file_object.write(cats_name + '\n')

with open('dogs.txt', 'a') as file_object:
    print ('If you want to quit , please enter "q".')
    while True:
        dogs_name = input('Please enter your dog\'s name:')
        if dogs_name == 'q':
            break
        file_object.write(dogs_name + '\n')

def count_name(filename):
    """计算一个文件中包含多少个名字"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print ('Sorry , the file ' + filename + 'does not exist.')
    else:
        names = contents.split()
        count_name = len(names)
        print ('The file ' + filename + ' has about ' + str(count_name) + ' names.')

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    count_name(filename)
