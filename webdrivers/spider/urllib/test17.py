from urllib import request
import ssl

#利用非认证的上下文环境替换认证下文的环境
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.12306.cn/index/'
req = request.urlopen(url)
html = req.read().decode()
print(html)