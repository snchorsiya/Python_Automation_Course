import os
import random
import string
import time
import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

user_name = "qaminop@yopmail.com"
password = "Minop@123"
N = 8
name = "".join(random.choices(string.ascii_letters, k=N))
emp_name = "Auto"+name

emp_code = "".join(random.choices(string.ascii_uppercase + str(random.randint(1, 9)), k=N))
punch_id = ''.join(str(random.randint(1, 9)) for _ in range(6))

driver.implicitly_wait(10)

driver.get("http://192.168.6.15:8082/")
driver.maximize_window()

title = driver.title
print(title)

clickLogin = driver.find_element(By.XPATH, "//span[normalize-space()='Login']")
act = ActionChains(driver)
act.move_to_element(clickLogin).perform()
driver.find_element(By.CLASS_NAME, "sign_in_menu_box").click()

driver.find_element(By.NAME, "UserEmail").send_keys(user_name)
driver.find_element(By.NAME, "Password").send_keys(password)
driver.find_element(By.XPATH, "//button[@type='submit' or @class='login_btn']").click()
driver.find_element(By.XPATH, "(//a[@class='nav-link nav-toggle'])[3]").click()
driver.find_element(By.XPATH, "//a[@href='/MasterData/EmployeeMaster']").click()
driver.find_element(By.XPATH, "//a[@id='AddEmployee']").click()

driver.find_element(By.ID, "Empcode").send_keys(emp_code)
driver.find_element(By.NAME, "EmpName").send_keys(emp_name)
driver.find_element(By.ID, "EmpDOB").send_keys("2004-12-16")
driver.find_element(By.ID, "Email").send_keys(emp_name+"@yopmail.com")
driver.find_element(By.ID, "frstNext").click()
driver.find_element(By.ID, "select2-PolicyId-container").click()
hrPolicy_list = driver.find_elements(By.XPATH, "//li[@class='select2-results__option']")
count_hrPolicy = len(hrPolicy_list)
print("Number of hr policy value is:", count_hrPolicy)

for hr in hrPolicy_list:
    # print(hr.text)
    if "HR Policy" in hr.text:
        hr.click()
        break

driver.find_element(By.ID, "EmpPunchID").send_keys(punch_id)
driver.find_element(By.ID, "EmpJoinDate").click()

exp_day = "29"
exp_year_month = "May 2020"

while True:
    year_month = driver.find_element(By.XPATH, "//div[@class='datepicker-days']//th[@class='datepicker-switch']").text
    # print(year_month)
    if year_month == exp_year_month:
        break
    else:
        driver.find_element(By.XPATH, "//div[@class='datepicker-days']//th[@class='prev']").click()

all_dates = driver.find_elements(By.XPATH, "//table/tbody/tr/td[@class='day']")

for date in all_dates:
    if date.text == exp_day:
        date.click()
        break

driver.find_element(By.ID, "SecondNext").click()

driver.find_element(By.ID, "select2-CompanyID-container").click()
all_company_list = driver.find_elements(By.XPATH, "//li[@class='select2-results__option']")
count_company = len(all_company_list)
print("Number of company list value is:", count_company)

for company in all_company_list:
    if "Mivnata" in company.text:
        company.click()
        break

try:
    number = 10
    input_value = "".join(random.choices(string.digits, k=number))
    # wait = WebDriverWait(driver, 30)
    time.sleep(5)
    # emp_Mno = wait.until(EC.presence_of_element_located((By.NAME, "EmpMNo")))
    emp_Mno = driver.find_element(By.NAME, "EmpMNo")
    emp_Mno.send_keys(input_value)
    # driver.execute_script("arguments[0].value = arguments[1]", emp_Mno, input_value)
except Exception as e:
    print(e)

driver.find_element(By.ID, "select2-BranchId-container").click()
all_branch_list = driver.find_elements(By.XPATH, "//li[@class='select2-results__option']")
count_branch = len(all_branch_list)
print("Number of branch list is:", count_branch)

for branch in all_branch_list:
    if "Mivnata" in branch.text:
        branch.click()
        break

driver.find_element(By.ID, "select2-DepartmentId-container").click()
all_department_list = driver.find_elements(By.XPATH, "//li[@class='select2-results__option']")
count_department = len(all_department_list)
print("Number of department list is:", count_department)

for department in all_department_list:
    if "HR" in department.text:
        department.click()
        break

driver.find_element(By.ID, "select2-RoleId-container").click()
all_role_list = driver.find_elements(By.XPATH, "//li[@class='select2-results__option']")
count_role = len(all_role_list)
print("Number of role list is:", count_role)

for role in all_role_list:
    if "HR" in role.text:
        role.click()
        break

driver.find_element(By.ID, "select2-ShiftId-container").click()
all_shift_list = driver.find_elements(By.XPATH, "//li[@class='select2-results__option']")
count_shift = len(all_shift_list)
print("Number of shift list is:", count_shift)

for shift in all_shift_list:
    if "General" in shift.text:
        shift.click()
        break

driver.find_element(By.ID, "ThirdNext").click()

driver.find_element(By.ID, "btnsubmit1").click()
print(driver.find_element(By.CLASS_NAME, "toast-message").text)

date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
driver.get_screenshot_as_file(os.getcwd()+ f"//ScreenShot//success_{date}.png")

# time.sleep(5)
try:
    wait = WebDriverWait(driver, 20, ignored_exceptions=[Exception])
    search = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='search']")))
    search.send_keys(emp_name)
except Exception as e:
    print(e)

print(driver.find_element(By.ID, "tblEmployee_info").text)
time.sleep(5)
driver.find_element(By.XPATH, "//input[@type='search']").clear()
driver.refresh()

# Handling web table
# print number of row and column
#
# column = driver.find_elements(By.XPATH, "//table[@id='tblEmployee']/thead/tr/th")
# count_column = len(column)
# print("Number of column is:", count_column)
#
# rows = driver.find_elements(By.XPATH, "//table[@id='tblEmployee']/tbody/tr")
# count_row = len(rows)
# print("Number of rows in current page:", count_row)
#
# for row in range(1, count_row + 1):
#     for col in range(1, count_column + 1):
#         data = driver.find_element(By.XPATH, f"//table[@id='tblEmployee']/tbody/tr[{row}]/td[{col}]").text
#         print(data, end=" ")
#     print()
#
# while True:
#     driver.execute_script("window.scrollBy(0, 500);")
#     next_page_button = driver.find_element(By.XPATH, "//a[@title='Next']")
#     if next_page_button.is_enabled():
#         next_page_button.click()
#         WebDriverWait(driver, 10).until(
#                      EC.presence_of_element_located((By.XPATH, "//table[@id='tblEmployee']/tbody/tr[1]")))
#
#     else:
#         print("No more pages available")
#         break

total_pages = 400
current_page = 1
while current_page <= total_pages:
    print(f"Processing page {current_page}")
    # next_page_button = driver.find_element(By.XPATH, "//a[@title='Next']")
    driver.execute_script("window.scrollBy(0, 500);")
    specific_page = driver.find_element(By.XPATH, f"//a[@title='Next']")
    specific_page.click()
    if specific_page.is_enabled():
        specific_page.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[@id='tblEmployee']/tbody/tr[1]"))
        )
        current_page += 1

        # Process and print data for the current page after it's loaded
        column = driver.find_elements(By.XPATH, "//table[@id='tblEmployee']/thead/tr/th")
        count_column = len(column)
        print("Number of column is:", count_column)
        rows = driver.find_elements(By.XPATH, "//table[@id='tblEmployee']/tbody/tr")
        count_row = len(rows)
        print("Number of rows in current page:", count_row)

        for row in range(2, count_row + 1):
            for col in range(1, count_column + 1):
                data = driver.find_element(By.XPATH, f"//table[@id='tblEmployee']/tbody/tr[{row}]/td[{col}]").text
                print(data, end=" ")
            print()
    else:
        print("No more pages available")
        break

driver.find_element(By.CLASS_NAME, "fa-angle-down").click()
drp = driver.find_element(By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-default']")
drp.find_element(By.ID, "logoff").click()

driver.close()



