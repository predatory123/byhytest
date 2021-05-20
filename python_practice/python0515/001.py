def make_album(singer,song,numbers=''):
    if numbers:   #如果numbers有值，就返回如下结果
        print({'message_singer': singer, 'message_song': song, 'message_number': numbers})
        # print({'message_singer':singer,'message_song':song})
    else:        #numbers无值的情况下
        print({'message_singer': singer, 'message_song': song})

# message_singer = input('请输入你最喜欢的歌手：')
# message_song   = input('请输入歌手的专辑名称；')
while True:
    print('输入quit可退出')
    message_singer = input('请输入你最喜欢的歌手：')
    if message_singer =='quit':
        break
    message_song = input('请输入歌手的专辑名称；')
    if message_song =='quit':
        break


