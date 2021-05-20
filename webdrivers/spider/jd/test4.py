from urllib import request, parse

if __name__ == '__main__':
    url = "https://www.baidu.com/s?"
    wd = input("Please input your value: ")

    #要使用dete，需要使用字典构造
    qs = {"wd": wd}
    #转换url编码
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    rsp = request.urlopen(fullurl)

    html = rsp.read()
    html = html.decode()
    print(html)


