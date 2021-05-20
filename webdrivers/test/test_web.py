from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://sahitest.com/demo/linkTest.htm')

# test = browser.find_element_by_id('linkByHtml').click()
test = browser.find_element_by_link_text('link with return true').click()

