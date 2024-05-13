from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set headless mode switch
headless_mode = False # Set to True for headless mode, False otherwise

# Set Chrome options for headless mode
chrome_options = Options()
if headless_mode:
    chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(executable_path="chromedriver", log_path="chromedriver.log")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://iusearchbtw.com")
print("Page loaded successfully.")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "xterm-helper-textarea")))
print("Found input element.")

input_element = driver.find_element(By.CLASS_NAME, "xterm-helper-textarea")
input_element.clear()
print("Input element cleared.")
time.sleep(1)
input_element.send_keys(Keys.CONTROL + Keys.SHIFT + "v")
print("Pasted content into input element.")
time.sleep(2)
input_element.send_keys(Keys.ENTER)
print("Pressed ENTER.")

time.sleep(60 * 3)
print("Waiting for 3 minutes...")

driver.quit()
print("Driver quit successfully.")


