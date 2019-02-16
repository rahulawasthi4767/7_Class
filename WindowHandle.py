import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://phptravels.com/")
browser.maximize_window()
browser.implicitly_wait(30)
browser.delete_all_cookies()
current_window_id = browser.current_window_handle
print(current_window_id)
time.sleep(10)
browser.find_element_by_xpath("//span[text()='Login']").click()
time.sleep(5)
window_ids = browser.window_handles
print(type(window_ids))
for handle in window_ids:
    print(handle)
    if handle != current_window_id:
        browser.switch_to.window(handle)
        browser.find_element_by_name("username").send_keys("hello")
#browser.close()
browser.quit()