from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

chr_option = Options()
chr_option.add_experimental_option("detach", True)

service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
title = driver.title
print(title)

driver.get("https://rahulshettyacademy.com/angularpractice/")
title = driver.title
print(title)
driver.back()

title = driver.title
print(title)
driver.forward()

title = driver.title
print(title)
driver.refresh()

title = driver.title
print(title)

driver.quit()