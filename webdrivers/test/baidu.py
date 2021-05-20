from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu,com")
driver.find_element_by_id("kw").send_keys("华为")
driver.implicitly_wait(2)
driver.find_element_by_id("su").click()
time.sleep(5)
driver,quit()