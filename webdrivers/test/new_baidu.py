from selenium import webdriver

driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

# 设置最大等待时长为 10秒
driver.implicitly_wait(10)

driver.get('https://www.baidu.com')

element = driver.find_element_by_id('kw')

element.send_keys('中通快运\n')

# 等待 2 秒
from time import sleep
sleep(3)

# 2 秒 过后，再去搜索
element = driver.find_element_by_id('1')

# 打印出 第一个搜索结果的文本字符串
print (element.text)