from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ---------- CONFIG ----------
URL = "https://the-internet.herokuapp.com/login"   # sample login site
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"

# ---------- SETUP ----------
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    # ---------- OPEN LOGIN PAGE ----------
    driver.get(URL)
    time.sleep(2)

    # ---------- LOGIN ----------
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    login_button.click()
    time.sleep(2)

    # ---------- EXTRACT DATA ----------
    message = driver.find_element(By.ID, "flash").text
    print("Login Result:", message.strip())

    # Example: navigate to a table page & extract data
    driver.get("https://the-internet.herokuapp.com/tables")
    time.sleep(2)

    rows = driver.find_elements(By.XPATH, "//table[1]/tbody/tr")
    print("\nExtracted Table Data:")
    for row in rows:
        print(row.text)

finally:
    # ---------- CLEANUP ----------
    time.sleep(3)
    driver.quit()
