from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("http://test-login.derucci.smart")
# assert "登录" in driver.title
login = driver.find_element_by_name("username")
login.clear()
login.send_keys("15191897268")
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

time.sleep(5)
#request 仅支持2M以下，jpg，png格式的二维码图片
picSelect = driver.find_element_by_css_selector(".is-required input.el-upload__input")
picSelect.send_keys(r'C:\Users\daenerysLi\Pictures\src=http___editor-img.888ban.com_ips_templ_preview_d6_1f_71_lg_44345_1612348615_601a7cc7eff16.jpg!w280_png_auth_key=2249395200-0-0-d00c70e2caf193d8ed673dd775fd0a9e&refer=http___editor-img.888ban.jpg')
# picSelect.send_keys(r'C:\Users\Daenerys\Pictures\1626057879376_nFPq.jpg')
# time.sleep(10)
sickName = "tt"
sickNameIn = driver.find_element_by_css_selector(".is-required[placeholder]>div>div>input")
sickNameIn.send_keys(sickName)
time.sleep(5)

openStatus = driver.find_element_by_css_selector("div.el-input--medium>input[placeholder]")
openStatus.click()

opStatus = driver.find_element_by_css_selector('script[type]+div>div>div>ul>[class="el-select-dropdown__item"]')
opStatus.click()

saveButton = driver.find_element_by_css_selector('[class="el-button ms-btn ms-btn-dark item el-button--primary el-button--medium"]')

# test
findSick = driver.find_element_by_css_selector(".el-form-item__content>div>input").send_keys(sickName)
findButton = driver.find_element_by_css_selector('[class="el-button ms-btn ms-btn-dark el-button--primary el-button--small"]')
findOn = driver.find_element_by_css_selector('.el-table_1_column_2 >div[class="cell el-tooltip"]')
sendTimes = driver.find_element_by_css_selector('.el-table_1_column_4>div[class="cell el-tooltip"]')
assert (sickName in findOn.text) && ("0" in sendTimes.text)
# driver.close()