import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(
    executable_path=r"E:\Python_Automation_Course-master\Python_Automation_Course-master\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(5)

driver.get("https://www.livecoinwatch.com/")
driver.maximize_window()

title = driver.title
print(title)

# print number of row and column

row = driver.find_elements(By.XPATH, "//table[@class='lcw-table layout-fixed']/tbody/tr")
number_row = len(row)
print("Number of row is:", number_row)

column = driver.find_elements(By.XPATH, "//table[@class='lcw-table layout-fixed']//th")
number_column = len(column)
print("Number of column is:", number_column)

# Print specific 1h data
time.sleep(6)

count_coin = 0
for ro in range(2, number_row+1):
    specific_data = driver.find_element(By.XPATH, "//table[@class='lcw-table layout-fixed']/tbody/tr["+str(ro)+"]/td[8]/span").text
    print("percent change is:", specific_data)

    if "%" in specific_data:
        percent_float = float(specific_data.strip("%")) # 0.06
        # print("percent in float format:", percent_float)
    else:
        percent_float = float(specific_data)
        # print("percent in float format:", percent_float)

    if percent_float > 0.05:
        count_coin = count_coin + 1
        coin_name = driver.find_element(By.XPATH, "//table[@class='lcw-table layout-fixed']/tbody/tr["+str(ro)+"]/td[2]").text
        print("name of coin which is changed more then 0.05 % is:", coin_name)
        print("Change in percent for 1hr:", percent_float)
        print(" ")
print("Total number of coins having change in 1hr more than 0.05 %:", count_coin)

driver.close()



# Print all data in table

# for r in range(2, len(row) + 1):
#     for c in range(1, len(column) + 1):
#         data = driver.find_element(By.XPATH,
#                                    "//table[@class='lcw-table layout-fixed']/tbody/tr[" + str(r) + "]/td[" + str(
#                                        c) + "]").text
#         print(data, end=" ")
#     print(" ")
