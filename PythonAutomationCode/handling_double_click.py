from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

title = driver.title
print(title)

field1 = driver.find_element(By.ID, "field1")
field1.clear()
field1.send_keys("qaSheetal")

field2 = driver.find_element(By.ID, "field2")


copy_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")

act = ActionChains(driver)
act.double_click(copy_btn).perform()

print(field2.get_attribute("value"))
driver.quit()