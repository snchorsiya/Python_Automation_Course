from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(5)
driver.get("https://qavbox.github.io/demo/webtable/")
driver.maximize_window()

title = driver.title
print(title)

# 1. print count of row and columns

row = driver.find_elements(By.XPATH, "//table[@id='table02']/tbody/tr")
number_row = len(row)
print("Number of the row count of table:", number_row)

column = driver.find_elements(By.XPATH, "//table[@id='table02']//th")
number_column = len(column)
print("Number of column of table:", number_column)

# 2. printing specific row and column data

location_data = driver.find_element(By.XPATH, "//table[@id='table02']/tbody/tr[4]/td[3]")
print("office location of cedric is", location_data.text)

age_user = driver.find_element(By.XPATH, " //table[@id='table02']/tbody/tr[18]/td[4]")
print("THe age of Gloria Little is", age_user.text)

salary = driver.find_element(By.XPATH, "  //table[@id='table02']/tbody/tr[20]/td[6]")
print("THe salary of Dai Rios is", salary.text)

# # Print all data from table
#
# for r in range(1, len(row)+1):
#     for c in range(1, len(column)+1):
#         data = driver.find_element(By.XPATH, "//table[@id='table02']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data, end=" ")
#     print(" ")

# 4. Print names of employees having office of Tokyo

for ro in range(1, len(row)+1):
    location_value = driver.find_element(By.XPATH, " //table[@id='table02']/tbody/tr["+str(ro)+"]/td[3]").text
    if location_value == "Tokyo":
        name = driver.find_element(By.XPATH, " //table[@id='table02']/tbody/tr["+str(ro)+"]/td[1]").text
        print(name)
        salary_user = driver.find_element(By.XPATH, " //table[@id='table02']/tbody/tr["+str(ro)+"]/td[6]").text
        print(salary_user)


driver.quit()