from urllib import request, parse
from http import cookiejar

'''创建配置文件'''
# 1.创建cookiejar的实例
cookie = cookiejar.MozillaCookieJar()

cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
# 2.生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 3.创建http请求管理器
http_handler = request.HTTPHandler()
# 4.生成https管理器
https_handler = request.HTTPHandler()
# 5.创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

# 创建登陆函数
# def login():
#
#     url = 'https://login.taobao.com/member/login.jhtml?from=taobaoindex&f=top&style=&sub=true&redirect_url=https%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm%3Fspm%3Da21bo.2017.754894437.3.5af911d9dRt3Pt%26ad_id%3D%26am_id%3D%26cm_id%3D%26pm_id%3D1501036000a02c5c3739'
#
#     data = {
#         'TPL_username':'demon琅琊',
#         'TPL_password':'wyj810278777'
#     }
#
#     data = parse.urlencode(data)
#
#     req = request.Request(url,data=data.encode('utf-8'))
#
#     rsp = opener.open(req)

def getHomePage():
    url = 'https://i.taobao.com/my_taobao.htm?spm=a21bo.2017.1997525045.1.473411d9bvdqbD'

    rsp = opener.open(url)

    html = rsp.read().decode('UTF-8','ignore')

    with open('login.html','w',encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    # login()
    getHomePage()


