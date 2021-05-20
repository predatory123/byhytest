from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
element = browser.find_element_by_id('kw').send_keys('zto')

driver.switch_to.window(handle)
element1= browser.find_element_by_tag_name('a').click()
# element = browser.find_element_by_partial_link_text('首页- 中通快递').click()