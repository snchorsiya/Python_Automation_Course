from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Or
driver.find_element(By.XPATH, "//input[@placeholder='Username' or @id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@placeholder='Password' or @id='password']").send_keys("secret_sauce")


# And
driver.find_element(By.XPATH, "//input[@type='submit' and @id='login-button']").click()

title = driver.title
print(title)

driver.close()