from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://maoyan.com/query?kw=功夫熊猫')

rsp = browser.find_element_by_class_name('channel-detail movie-item-title')
print(rsp)

