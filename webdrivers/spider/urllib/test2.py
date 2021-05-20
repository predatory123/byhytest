import urllib.request
import chardet


'''利用request下载页面，使用chardet检测，自动检测页面是否出现乱码'''
if __name__ == '__main__':
    url = "https://search.jd.com/Search?keyword=iphone&enc=utf-8&wq=iphone"
    rsp = urllib.request.urlopen(url)
    html = rsp.read()

    # 利用 chardet检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    # 使用get取值保证不会出错
    html = html.decode(cs.get("encoding","utf-8"))
    print(html)