from urllib import request

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    rsp = request.urlopen(url)
    html = rsp.read().decode()
    with open('rsp.html','w',encoding='utf-8') as f:
        f.write(html)