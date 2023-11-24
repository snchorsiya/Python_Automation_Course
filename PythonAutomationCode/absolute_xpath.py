from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path="D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.get("https://www.saucedemo.com/")

driver.maximize_window()

driver.find_element(By.XPATH, "html/body/div[1]/div/div[2]/div/div/div/form/div[1]/input").send_keys("standard_user")
driver.find_element(By.XPATH, "html/body/div[1]/div/div[2]/div/div/div/form/div[2]/input").send_keys("secret_sauce")

driver.find_element(By.XPATH, "html/body/div[1]/div/div[2]/div/div/div/form/input").click()

title = driver.title
print(title)

driver.quit()