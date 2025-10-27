from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def login(u, p):
    wait = WebDriverWait(driver, timeout=2)

    username = driver.find_element(By.NAME, "username")
    wait.until(lambda _: username.is_displayed())
    username.click()
    username.send_keys(u)

    password = driver.find_element(By.NAME, "password")
    wait.until(lambda _: password.is_displayed())
    password.click()
    password.send_keys(p)

    button = driver.find_element(By.XPATH, "//button//div[contains(text(), 'Log in')]")
    button.click()
    # username.clear()
    # data = username.get_attribute("value")
    # assert data == ""

import time

PATH = r"C:\Program Files\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(PATH))

driver.get('https://www.instagram.com')

u = input("Enter Username: ")
p = input("Enter Password: ")
login(u, p)

time.sleep(12)

driver.quit()


