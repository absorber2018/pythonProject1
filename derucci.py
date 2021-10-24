from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

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
login.send_keys(Keys.ENTER)
#inter the page of dashboard

jumpPage = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]'))
    )
jumpPage.click()

# sleepRange = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/ul/div[5]/li/div/div/span'))
# )
# sleepRange.click()
# assert "慕思智能云平台" in driver.page_source
# operatPage = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/ul/div[7]/li/div')
operatPage = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/ul/div[7]/li/div/i'))
)
operatPage.click()
# driver.quit()
#focus on current page
# all_window = driver.window_handles
# for window in all_window:
#     if window != current_window:
#         driver.switch_to.window(window)
# #get current page handle name
# current_window = driver.current_window_handle

# elem = driver.find_elements_by_css_selector("div.xh-highlight")
# ActionChainsDriver = ActionChains(driver).click(elem)
# ActionChainsDriver.perform()
# driver.close()