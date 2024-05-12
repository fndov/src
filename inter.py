from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(executable_path="chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://iusearchbtw.com")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "xterm-helper-textarea")))

input_element = driver.find_element(By.CLASS_NAME, "xterm-helper-textarea")
input_element.clear()
time.sleep(1)
input_element.send_keys(Keys.CONTROL + Keys.SHIFT + "v")
time.sleep(2)
input_element.send_keys(Keys.ENTER)

time.sleep(60 * 3)

driver.quit()