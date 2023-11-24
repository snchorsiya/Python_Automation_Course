from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_options = Options()
chr_options.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_options)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
title = driver.title
print("The title name is:- ", title)

expected_title = "Swag Labs"

if title == expected_title:
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    title = driver.title
    print("After login display title:-", title)
else:
    print(f"Title verify failed, Expected title '{expected_title}', but got '{title}'")
