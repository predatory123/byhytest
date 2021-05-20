# import unittest
# from selenium import webdriver
#
# class GoogleTestCase(unittest.TestCase):
#
#     def setUp(self):
#         self.browser = webdriver.Firefox()
#         self.addCleanup(self.browser.quit)
#
#     def testPageTitle(self):
#         self.browser.get('http://www.google.com')
#         self.assertIn('Google', self.browser.title)
#
# # if __name__ == '__main__':
# #     unittest.main(verbosity=2)


from selenium import webdriver

from time import sleep
#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
browser = webdriver.Firefox()

#2.通过浏览器向服务器发送URL请求
browser.get("https://www.baidu.com/")

sleep(3)

#3.刷新浏览器
browser.refresh()

#4.设置浏览器的大小
browser.set_window_size(1400,800)

#5.设置链接内容
element=browser.find_element_by_link_text("新闻")
element.click()

element=browser.find_element_by_link_text("互联网")
element.click()
