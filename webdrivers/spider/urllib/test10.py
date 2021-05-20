from urllib import request,error

if __name__ == '__main__':
    url = 'http://www.baidu.com'

    # 1.设置代理地址
    proxy = {'http':'117.191.11.73:80'}
    # 2.创建ProxyHandler
    proxy_header = request.ProxyHandler(proxy)
    # 3.创建Opener
    opener = request.build_opener(proxy_header)
    # 4.安装Opener
    request.install_opener(opener)

    #  使用代理服务器，访问百度
    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except error.HTTPError as e:
        print(e)
    except Exception as e:
        print(e)