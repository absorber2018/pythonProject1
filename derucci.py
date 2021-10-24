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

# operatPage = driver.find_element_by_css_selector('ul.el-menu>div.full-mode:nth-child(7)')
operatPage = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.el-menu>div.full-mode:nth-child(7)'))
)
operatPage.click()

# servicePage = driver.find_element_by_css_selector('ul.el-menu>div.full-mode:nth-child(7)>li>ul>div.nest-menu:nth-child(3)>a>li[tabindex="-1"]')
servicePage = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul.el-menu>div.full-mode:nth-child(7)>li>ul>div.nest-menu:nth-child(3)>a>li[tabindex="-1"]'))
)
servicePage.click()

buildPage = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "section.app-main>div>div>div.el-card__body>div:nth-child(2)>button:nth-child(1)"))
)
buildPage.click()

picSelect = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "i.el-icon-plus"))
)
picSelect.click()
# picSelect = driver.find_element_by_css_selector("i.el-icon-plus")
picSelect.send_keys('c:/Users/Daenerys/Pictures/1626057879376_nFPq.jpg')


# driver.close()