from  selenium import webdriver

driver= webdriver.Chrome()

driver.get("file:///C:/Users/rahul/Desktop/test.html")
driver.maximize_window()
driver.implicitly_wait(30)

# ele = driver.find_elements_by_xpath("//*[@id='emp']/thead/tr/th")
# print(len(ele))

# ele = driver.find_elements_by_xpath("//*[@id='emp']//tr")
# print(len(ele))

ele = driver.find_elements_by_xpath("//*[@id='emp']//th")
print(len(ele))


# First_part = "//*[@id='emp']/thead/tr/th["
# Second_part = "]"
#
# First_part+i+Second_part

driver.close()