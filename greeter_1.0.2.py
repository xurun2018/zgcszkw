from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://192.168.143.221:3000")
try:
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"username"))
)
    driver.find_element_by_id("username").send_keys("13022902105")
    driver.find_element_by_id("password").send_keys("19860702")
    WebDriverWait(driver,10).until(
	EC.title_is(u'企业所得税智能汇算清缴暨风险防控系统')
)
finally:
    driver.quit()

