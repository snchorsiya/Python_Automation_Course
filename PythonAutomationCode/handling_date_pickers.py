import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(10)

driver.get("https://jqueryui.com/datepicker/")

driver.maximize_window()

title = driver.title
print(title)

driver.switch_to.frame(0)
driver.find_element(By.ID, "datepicker").click()

exp_day = "20"
exp_month = "August"
exp_year = "2024"

while True:
    month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
    if month == exp_month and year == exp_year:
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

all_dates = driver.find_elements(By.XPATH, "//table/tbody/tr/td/a")

for dates in all_dates:
    if dates.text == exp_day:
        dates.click()





