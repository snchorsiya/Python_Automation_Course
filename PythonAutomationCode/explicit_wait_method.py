import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chr_option = Options()
chr_option.add_experimental_option("detach", True)

service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

wait = WebDriverWait(driver, 20, ignored_exceptions=[Exception])  # declaration of explicit wait

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

title = driver.title
print(title)

username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
username_field.send_keys("Admin")

# driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
img = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='client brand banner']")))
im = img.is_displayed()
# img = driver.find_element(By.XPATH, "//img[@alt='client brand banner']").is_displayed()
print(im)

myinfo = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='My Info']")))
myinfo.click()
# driver.find_element(By.XPATH, "//*[text()='My Info']").click()

time.sleep(3)
wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='orangehrm-edit-employee-name']")))
name = driver.find_element(By.XPATH, "//div[@class='orangehrm-edit-employee-name']")
# name = driver.find_element(By.XPATH, "(//h6[@class='oxd-text oxd-text--h6 --strong'])").text
print(name.text)

admin = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Admin']")))
admin.click()

webTable = driver.find_elements(By.XPATH, "//div[@class = 'oxd-table-body']")
tableCount = len(webTable)
print(tableCount)

for web_table in webTable:
    username = web_table.text
    print(username)