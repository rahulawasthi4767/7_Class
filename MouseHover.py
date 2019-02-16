from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# from  selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://flipkart.com")
driver.maximize_window()
driver.implicitly_wait(30)

element = driver.find_element_by_xpath("//span[text()='Men']")

webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
# action = ActionChains(driver)
# action.click(element)
driver.quit()
