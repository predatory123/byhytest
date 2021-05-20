# 读取文件中的字符个数
name = 'word.txt'
with open(name,'w') as file_object:
    file_object.write('The computer is very beautiful,the color is black,the chuliqi is core_i5 8500。')

with open('word.txt') as book:
    cindy = book.read()
    value = cindy.lower().count('the')
    print(value)

