import urllib.request

'''利用request下载页面，使用chardet检测，自动检测页面是否出现乱码'''
if __name__ == '__main__':
    url = "https://baike.baidu.com/item/%E9%87%91%E4%B8%9D%E7%8C%B4/37026?fr=aladdin"
    rsp = urllib.request.urlopen(url)

    print(type(rsp))
    print(rsp)

    print("URL: {0}".format(rsp.geturl()))
    print("Info: {0}".format(rsp.info()))
    print("Code: {0}".format(rsp.getcode()))

    html = rsp.read()

    # 使用get取值保证不会出错
    # html = html.decode(rsp.get("encoding", "utf-8"))
    # print(html)