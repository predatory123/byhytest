#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.douban.com")
driver.find_element_by_partial_link_text('密码登录')
driver.click()
# 输入账号密码
driver.find_element_by_name("form_email").send_keys("158xxxxxxxx")
driver.find_element_by_name("form_password").send_keys("zhxxxxxxxx")

# 模拟点击登录
driver.find_element_by_xpath("//input[@class='bn-submit']").click()

# 等待3秒
time.sleep(3)

# 生成登陆后快照
driver.save_screenshot(u"douban.png")

driver.quit()