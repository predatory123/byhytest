# # pre1创建一个列表，使用函数传递该列表
# def show_mgsician(magic):
#     for magician in magic:
#          print('hello ' +magician)
# magician = ['bob','tom','alice']
# show_mgsician(magician)
# print('\n')
# # 1.使用函数修改列表的值，在每个值的后面加上“the Graet”
# def show_mgsicians(magics,complates):
#     while magics:
#         people = magics.pop()
#         print('old '+ people)
#         complates.append(str(people)+" the Graest")
# print('\n')
# def make_garat(complates):
#     print('New magician is: ')
#     for new_people in complates:
#         print(new_people)
# print('\n')
# magics = ['bob','tom','alice']
# complates = []
# show_mgsicians(magics,complates)
# make_garat(complates)
# print('\n')
# print('原来的列表')
# show_mgsician(magics)
# print('\n')
# show_mgsician(complates)
# 3.传递一个副本，并带入show_magician（）函数，查看列表是否被更改
def show_mgsician(magic):
    for magician in magic:
         print('hello ' +magician)
def show_mgsicians(magics,complates):
    while magics:
        people = magics.pop()
        print('old '+ people)
        complates.append(str(people)+" the Graest")
print('\n')
def make_garat(complates):
    print('New magician is: ')
    for new_people in complates:
        print(new_people)
print('\n')
magics = ['bob','tom','alice']
complates = []
show_mgsicians(magics[:],complates)
make_garat(complates)
print('\n')
print('原来的列表')
show_mgsician(magics)
print('\n')
show_mgsician(complates)