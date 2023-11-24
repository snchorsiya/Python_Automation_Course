from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_options = Options()
chr_options.add_experimental_option("detach", True)

service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_options)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

title = driver.title
print(title)

driver.find_element(By.LINK_TEXT, "Log in").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "viewed products").click()
title = driver.title
print(title)
