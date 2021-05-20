# part1 定义一个函数，城市在国家前面，用逗号隔开
def city_country(city,country):
    print(city+','+country)
city_country('San Francisco','Amercian')
city_country('Sydney','Australia')
city_country('Chendu','China')

#part2 定义一个函数，包含歌手和专辑，输入一个包含歌手和专辑的字典。

def make_album(singer,song,numbers=''):
    if numbers:   #如果numbers有值，就返回如下结果
        print({'message_singer': singer, 'message_song': song, 'message_number': numbers})
        # print({'message_singer':singer,'message_song':song})
    else:        #numbers无值的情况下
        print({'message_singer': singer, 'message_song': song})
        # print({'message_singer':singer,'message_song':song,'message_number':numbers})


make_album('justin bob','baby',111)
make_album('taylor swift','22',2)
make_album('bob','光荣',)




