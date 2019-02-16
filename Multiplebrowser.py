import time

from selenium import webdriver

#driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get("http://facebook.com")
time.sleep(4)
driver.quit()