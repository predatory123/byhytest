from urllib import request

if __name__ == '__main__':

    url = "https://search.jd.com/Search?keyword=iphone&enc=utf-8&wq=iphone"
    # 打开网页并返回结果
    value = request.urlopen(url)
    # 读取出来的内容为bytes  需要解码
    html = value.read()
    print(type(html))

    html = html.decode()
    print(html)