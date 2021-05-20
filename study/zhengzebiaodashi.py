content = '''
Python3 高级开发工程师 上海互教教育科技有限公司上海-浦东新区2万/月02-18满员
测试开发工程师（C++/python） 上海墨鹍数码科技有限公司上海-浦东新区2.5万/每月02-18未满员
Python3 开发工程师 上海德拓信息技术股份有限公司上海-徐汇区1.3万/每月02-18剩余11人
测试开发工程师（Python） 赫里普（上海）信息科技有限公司上海-浦东新区1.1万/每月02-18剩余5人
Python高级开发工程师 上海行动教育科技股份有限公司上海-闵行区2.8万/月02-18剩余255人
python开发工程师 上海优似腾软件开发有限公司上海-浦东新区2.5万/每月02-18满员
'''

import re
p = re.compile(r'([\d.]+)万/每{0,1}月')
for one in  p.findall(content):
    print(one)




content = '''苹果，是绿色的
橙子，是橙色的
香蕉，是黄色的
乌鸦，是黑色的
猴子，'''

import re
p = re.compile(r'，.*')
for one in  p.findall(content):
    print(one)

content = '''苹果.是绿色的
橙子.是橙色的
香蕉.是黄色的'''

import re
p = re.compile(r'.*\.')
for one in  p.findall(content):
    print(one)


names = '关羽; 张飞, 赵云,马超, 黄忠  李逵'
# 这时，最好使用正则表达式里面的 split 方法：

import re

names = '关羽; 张飞, 赵云,   马超, 黄忠  李逵'

namelist = re.split(r'[;,\s]\s*', names)
print(namelist)