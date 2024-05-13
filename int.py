from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Comment this out if you want to see the browser window
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(executable_path="/home/miyu/src/chromedriver", log_path="chromedriver.log")
driver = webdriver.Chrome(service=service, options=chrome_options)

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
