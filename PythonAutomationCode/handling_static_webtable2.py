from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
title = driver.title
print(title)

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

driver.find_element(By.XPATH, "//*[text()='Admin']").click()

row = driver.find_elements(By.XPATH, "(//div[@class='oxd-table-body' or @role='rowgroup'])[2]/div")
row_count = len(row)
print("Number of row Count is:", row_count)

column = driver.find_elements(By.XPATH, "//div[@role='columnheader']")
column_count = len(column)
print("Number of column is:", column_count)

for r in range(1, len(row)+1):
    for c in range(2, len(column)+1):
        # xpath = "(//div[@class='oxd-table-body' or @role='rowgroup'])[2]/div[{}]//div[{}]".format(str(r), str(c))
        xpath = "//div[@class='oxd-table-body' or @role='rowgroup'][2]/div["+str(r)+"]//div["+str(c)+"]"
        data = driver.find_element(By.XPATH, xpath).text
        print(data, end=" ")
    print(" ")
