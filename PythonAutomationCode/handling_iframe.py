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

driver.switch_to.frame("myFrame2")
iframe_text = driver.find_element(By.TAG_NAME, "h4")
print(iframe_text.text)

driver.switch_to.default_content()
driver.switch_to.frame("frameName3")
click_checkbox = driver.find_element(By.ID, "checkBox6")
click_checkbox.click()
print(click_checkbox.is_selected())

driver.quit()
