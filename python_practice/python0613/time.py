# import time
# before = time.time()
# func1()
# after = time.time()
# print(f调用func1，花费时间{before-after}’)

from datetime import datetime
# asd = str(datetime.now().strftime('%Y-%m-%d ** %H:%M:%S'))
# time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
# print(asd)

aa= datetime.now()
print(aa)
# datetime.datetime(2018, 6, 30, 23, 3, 54, 238947)
# datetime.now().year
#

# 要计算出 2018年6月24日 是星期几
thatDay = "2019-6-13"
from datetime import datetime
# 先把字符串表示的日期转化为 datetime 对象
theDay = datetime.strptime(thatDay, "%Y-%m-%d")
#再获取星期几
a = theDay.weekday()
print(a)



thatDay = "2018-6-24"
from datetime import datetime,timedelta
theDay = datetime.strptime(thatDay, "%Y-%m-%d").date()

# 后推120天 就是 + timedelta(days=120)
target = theDay + timedelta(days=120)

print(target)
print(target.weekday())

# 前推120天 就是 - timedelta(days=120)
target = theDay - timedelta(days=120)

print(target)
print(target.weekday())


thatDay = "2018-6-20"
from datetime import datetime,timedelta
theDay = datetime.strptime(thatDay, "%Y-%m-%d").date()

# 这就是 2018-6-30 那一周的周一
weekMonday = theDay - timedelta(days=theDay.weekday())


from calendar import monthrange
# monthrange返回的是元组
# 第一个元素是指定月第一天是星期几
# 第二个元素是指定月有多少天
mr = monthrange(2019, 2)

# 得到2011年2月有多少天
print(mr[1])