# from selenium import webdriver
#
# driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
#
# driver.get('http://www.python3.vip/doc/tutorial/selenium/code/sample2.html')
#
# # 先根据name属性值 'innerFrame'，切换到iframe中
# driver.switch_to.frame('innerFrame')
#
# # 根据 class name 选择元素，返回的是 一个列表
# elements = driver.find_elements_by_class_name('animal')
#
# for element in elements:
#     print(element.text)


from selenium import webdriver


driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
driver.implicitly_wait(10)

driver.get('http://www.python3.vip/doc/tutorial/selenium/code/sample3.html')

# 点击打开新窗口的链接
link = driver.find_element_by_tag_name("a")
link.click()

for handle in driver.window_handles:
    # 先切换到该窗口
    driver.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if '必应' in driver.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break


# driver.title属性是当前窗口的标题栏 文本
print(driver.title)