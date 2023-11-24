import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
service = ChromeService(executable_path="D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.get("http://192.168.6.15:8082/")
driver.maximize_window()
title = driver.title
print("The title name is: ", title)

driver.find_element(By.XPATH, "//span[normalize-space()='Login']").click()
time.sleep(5)

driver.find_element(By.XPATH, "(//span[contains(text(),'Sign In')])[1]").click()
time.sleep(2)

expected_title = "Cloud based time and Attendance Management - Real Time monitoring"
if title == expected_title:
    driver.find_element(By.XPATH, "//input[@id='UserEmail']").send_keys("qaminop@yopmail.com")
    driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("Minop@123")
    driver.find_element(By.XPATH, "//button[contains(text(),'Login​')]").click()
    time.sleep(3)

    title = driver.title
    print("After login display title:- ", title)

else:
    print(f"Title verify failed. Expected title '{expected_title}', but got '{title}'")

