 # 1. Selenium默认为Firefox。验证
from selenium import webdriver

driver = webdriver.Firefox()
 # 将控制的webdriver的Firefox赋值给driver；获得了浏览器对象才可以启动浏览器，打开网址，操作页面

driver.get("http://www.baidu.com")
 # 获得浏览器对象后，通过get()方法，可以向浏览器发送网址

driver.find_element_by_id('kw').send_keys('hello')
driver.click()
# 这里通过 id = kw 定位到搜索框，并通过键盘方法send_keys向输入框里输入'hello'

driver.find_element_by_link_text('_百度百科')
driver .click()
# driver.close()