from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://10.12.0.54/login/Login.jsp?gopage=&_rnd_=ff108b7b-5ddb-4c3b-ab52-81f1f13eac2d")
try:
    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(By.ID, "sfclsid")
    )
finally:
    driver.quit()