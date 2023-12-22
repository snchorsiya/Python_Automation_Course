from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

# chr_option = Options()
# chr_option.add_experimental_option("detach", True)
# prefs = {"download.default_directory": "D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\PythonAutomationCode\FileDownload"}
# chr_option.add_experimental_option("prefs", prefs)
# service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service, options=chr_option)

edg_option = webdriver.EdgeOptions()  # Correct initialization of EdgeOptions

# Set preferences for file download location
prefs = {'download.default_directory': 'D:\\Automation\\PythonAutomation\\Chromedriver-webdrivermanger\\PythonAutomationCode\\FileDownload'}
edg_option.add_experimental_option("prefs", prefs)
edg_option.add_experimental_option("detach", True)

# Ensure you have specified the correct path for the Microsoft Edge driver
# Specify the path to the msedgedriver executable
edge_driver_path = r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\msedgedriver.exe"

# Initialize EdgeService
service = webdriver.EdgeService(executable_path=edge_driver_path)

# Start the Edge browser with configured options and service
driver = webdriver.Edge(service=service, options=edg_option)

driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()
title = driver.title
print(title)

driver.find_element(By.LINK_TEXT, "upload.png").click()

# driver.quit()