from urllib import request,error

if __name__ == '__main__':
    url = 'http://www.baidu.com'

    try:
        # 1.使用head方法模拟UA
        # headers = {}
        # headers['User-Agent'] = 'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'
        # req = request.Request(url,headers=headers)

        # 2.使用add_herders方法
        req = request.Request(url)
        req.add_header('User-Sgent','Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5')

        #正常访问
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)

    except error.URLError as e:
        print(e)

    except Exception as e:
        print(e)

print("Done.......................")
