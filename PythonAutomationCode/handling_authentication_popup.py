from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()

title = driver.title
print(title)

driver.find_element(By.LINK_TEXT, "Basic Auth").click()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

test = driver.find_element(By.TAG_NAME, "p")
print(test.text)

driver.quit()

