from selenium import webdriver

driver = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')

driver.get('http://www.python3.vip/doc/tutorial/selenium/code/sample1.html')

element = driver.find_element_by_css_selector('#searchtext')
element.send_keys('你好')



