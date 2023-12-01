import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chr_option = Options()
chr_option.add_experimental_option("detach", True)

service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(20)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

title = driver.title
print(title)

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")

# wait = WebDriverWait(driver, 15)
# wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

img = driver.find_element(By.XPATH, "//img[@alt='client brand banner']").is_displayed()
print(img)

# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='My Info']")))
driver.find_element(By.XPATH, "//*[text()='My Info']").click()
time.sleep(10)
name = driver.find_element(By.XPATH, "(//h6[@class='oxd-text oxd-text--h6 --strong'])").text
print(name)
driver.quit()