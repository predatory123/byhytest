
#2.在函数中修改列表
#（1）.不使用函数
magsci_list = ['tom','jake','taylor']
new_magsic  = []
while magsci_list:
    magscian = magsci_list.pop()
    # print('New magsic: '+ magscian)
    new_magsic.append(str(magscian) + ' the Great')
for new_magsician in new_magsic:
    print('New magician is ' +new_magsician)

'''(2) .使用函数
'''
def show_mgsician(magic,complate):
    while magic:
        people = magic.pop()
        print('old '+ people)
        complate.append(str(people)+"the Graest")

def make_garat(complate):
    print('New magician is: ')
    for new_people in complate:
        print(new_people)

magic = ['bob','tom','alice']
complate = []

show_mgsician(magic,complate)
make_garat(complate)

