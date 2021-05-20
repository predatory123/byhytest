from urllib import request, parse
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

if __name__ == '__main__':

    # 百度搜索请求头信息
    url = 'http://www.baidu.com/s?'
    wd = input('Input your keyword: ')

    # 要想使用data,需使用字典结构
    qs = {'wd': wd}

    # 将输入的字典qs转换为url编码
    # 可以将打印出来的和百度搜索访问结果图片43_4中进行对比，发现url编码是一样的
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    # 访问的网址必须转换为url编码，直接访问会报错
    # fullurl = 'http://www.baidu.com/s?wd=大熊猫'
    rsp = request.urlopen(fullurl)

    html = rsp.read()
    html = html.decode()
    print(html)
# ---------------------
# 作者：夏树柏
# 来源：CSDN
# 原文：https://blog.csdn.net/u011318077/article/details/86510682
# 版权声明：本文为博主原创文章，转载请附上博文链接！