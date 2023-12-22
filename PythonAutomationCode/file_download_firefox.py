import os

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

fir_option=webdriver.FirefoxOptions()
# fir_option.set_preference("browser.download.folderList", 0)  # 0 desktop,
# fir_option.set_preference("browser.download.folderList", 1)  # 1: downloads,
fir_option.set_preference("browser.download.folderList", 2)  # 2: desired location
fir_option.set_preference("browser.download.dir",
                          "D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\PythonAutomationCode\FileDownload")

service=FireFoxService(
    executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\geckodriver.exe")
driver=webdriver.Firefox(service=service, options=fir_option)

driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()
title = driver.title
print(title)

driver.get_screenshot_as_file(
    os.getcwd() + "//ScreenShot//18demo.png")

driver.find_element(By.LINK_TEXT, "TP-link.jpg").click()
