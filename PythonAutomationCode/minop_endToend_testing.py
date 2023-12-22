import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import minop_excel_utility

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

file = "C:\\Users\\Sheetal.Chorsiya\\Downloads\\Test_Data_Minop.xlsx"

driver.implicitly_wait(10)

driver.get("http://192.168.6.15:8082/")
driver.maximize_window()

title = driver.title
print(title)

rows = minop_excel_utility.get_row_count(file, "Sheet1")

for ro in range(2, rows+1):
    clickLogin = driver.find_element(By.XPATH, "//span[normalize-space()='Login']")
    act = ActionChains(driver)
    act.move_to_element(clickLogin).perform()
    driver.find_element(By.CLASS_NAME, "sign_in_menu_box").click()
    user_name = minop_excel_utility.read_data(file, "Sheet1", ro, 1)
    password = minop_excel_utility.read_data(file, "Sheet1", ro, 2)
    company_name = minop_excel_utility.read_data(file, "Sheet1", ro, 3)
    company_email = minop_excel_utility.read_data(file, "Sheet1", ro, 4)
    company_contact = minop_excel_utility.read_data(file, "Sheet1", ro, 5)
    company_address = minop_excel_utility.read_data(file, "Sheet1", ro, 6)

    # passing test data in app
    driver.find_element(By.NAME, "UserEmail").send_keys(user_name)
    driver.find_element(By.NAME, "Password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit' or @class='login_btn']").click()
    driver.find_element(By.XPATH, "(//a[@class='nav-link nav-toggle'])[3]").click()
    driver.find_element(By.XPATH, "//a[@href='/MasterData/CompanyMaster']").click()
    driver.find_element(By.XPATH, "//a[@id='Add']").click()
    driver.find_element(By.NAME, "CompanyName").send_keys("dem1o"+company_name)
    driver.find_element(By.NAME, "CompanyEmail").send_keys("dem1o"+company_email)
    driver.find_element(By.NAME, "CompanyContact").send_keys(company_contact)
    driver.find_element(By.NAME, "CompanyAddress").send_keys(company_address)
    driver.find_element(By.ID, "btncompany").click()
    print(driver.find_element(By.CLASS_NAME, "toast-message").text)
    # wait = WebDriverWait(driver, 20)
    # wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "fa-angle-down")))
    time.sleep(10)
    driver.find_element(By.CLASS_NAME, "fa-angle-down").click()


    # wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-default']")))
    drp = driver.find_element(By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-default']")
    drp.find_element(By.ID, "logoff").click()
    # select_drp = Select(drp)
    # select_drp.select_by_visible_text("Log Out")


# driver.close()
