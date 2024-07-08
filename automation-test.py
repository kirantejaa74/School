from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Google login page
driver.get("https://accounts.google.com/signin")

# Explicit wait for the email field
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
)
email_field.send_keys("raghu.py77@gmail.com")
email_field.send_keys(Keys.RETURN)

# Explicit wait for the password field
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@name="password"]'))
)
password_field.send_keys("Soccer@12")
password_field.send_keys(Keys.RETURN)

# Optionally, wait a few seconds to see the result
time.sleep(5)

# Close the browser
driver.quit()
