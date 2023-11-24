from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ch_option = Options()
ch_option.add_experimental_option("detach", True)

service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=ch_option)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

user_name = (driver.find_element(By.XPATH, "//input[@placeholder='Username' or @id='user-name']"))
user_name.send_keys("standard_user")

driver.refresh()

submit_btn = driver.find_element(By.XPATH, "//input[@type='submit' and @id='login-button']")
submit_btn.click()

driver.quit()
