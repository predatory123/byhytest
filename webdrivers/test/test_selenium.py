from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
# browser = webdriver.Firefox()


browser.get('http://www.zto56.com')
assert 'baidu' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()