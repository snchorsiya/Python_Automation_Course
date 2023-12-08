from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(5)
driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()

title = driver.title
print(title)

driver.find_element(By.ID, "myTextInput").send_keys("Sheetal")
pre_filled = driver.find_element(By.ID, "myTextInput2")
print(pre_filled.get_attribute("value"))
pre_filled.clear()
pre_filled.send_keys("QA Tester")

placeholder = driver.find_element(By.ID, "placeholderText")
print(placeholder.get_attribute("placeholder"))
placeholder.send_keys("Manager")