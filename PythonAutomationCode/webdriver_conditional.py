import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
text_display = driver.find_element(By.NAME, "show-hide").is_displayed()
print(text_display)

driver.find_element(By.CSS_SELECTOR, "#hide-textbox").click()
print(driver.find_element(By.NAME, "show-hide").is_displayed())

print("================Is_Enable============")

driver.get("https://rahulshettyacademy.com/angularpractice/")
radio_btn_enable = driver.find_element(By.NAME, "inlineRadioOptions").is_enabled()
print(radio_btn_enable)

print("===================Is_Selected==================")

radio_btn_selected = driver.find_element(By.ID, "inlineRadio1").is_selected()
print("before selecting the button", radio_btn_selected)
driver.find_element(By.ID, "inlineRadio1").click()
print("after selecting the button", driver.find_element(By.ID, "inlineRadio1").is_selected())

time.sleep(3)

driver.quit()