from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://login.derucci-smart.com/dashboard")
# assert "登录" in driver.title
login = driver.find_element_by_name("username")
login.clear()
login.send_keys("15609263915")
login = driver.find_element_by_name("password")
login.clear()
login.send_keys("111111")
login = driver.find_element_by_xpath("//button[@class='el-button ms-submit el-button--primary el-button--medium']")

#get current page handle name
current_window = driver.current_window_handle
#login to baskboard
login.send_keys(Keys.ENTER)
#inter the page of dashboard
assert "No results found." not in driver.page_source
#focus on current page
all_window = driver.window_handles
for window in all_window:
    if window != current_window:
        driver.switch_to.window(window)
#get current page handle name
current_window = driver.current_window_handle
elem = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]')
# print(elem)
elem.click()
# elem = driver.find_elements_by_css_selector("div.xh-highlight")
# ActionChainsDriver = ActionChains(driver).click(elem)
# ActionChainsDriver.perform()
# driver.close()