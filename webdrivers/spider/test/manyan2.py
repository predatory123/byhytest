from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://maoyan.com/films/78535')

rsp = driver.find_element_by_class_name('movie-brief-container').text
print(rsp)
