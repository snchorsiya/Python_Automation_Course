from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://phptravels.com/demo/")
driver.maximize_window()

title = driver.find_element(By.XPATH, "//h3[text()='Can I save content?']")
print(title.is_displayed())