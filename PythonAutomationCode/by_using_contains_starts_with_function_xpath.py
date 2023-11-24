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

userName = driver.find_element(By.XPATH, "//input[contains(@placeholder,'Usern')]")
userName.send_keys("standard_user")
passWord = driver.find_element(By.XPATH, "//input[contains(@data-test,'password')]")
passWord.send_keys("secret_sauce")

# Start-with() function

submitBtn = driver.find_element(By.XPATH, "//input[starts-with(@id,'login')]")
submitBtn.click()

title = driver.title
print(title)

driver.quit()