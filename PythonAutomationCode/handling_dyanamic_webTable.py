from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
chr_option.add_experimental_option("excludeSwitches", ["enable-logging"])
service = ChromeService(
    executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

print("Testing Started")
driver.implicitly_wait(5)
driver.get("https://www.livecoinwatch.com/")
driver.maximize_window()

title = driver.title
print(title)

# Print the number of row
row = driver.find_elements(By.XPATH, "//table[@class='lcw-table layout-fixed']/tbody/tr")
row_count = len(row)
print("Number of row is:-", row_count)

# Print the number of column
column = driver.find_elements(By.XPATH, "//table[@class='lcw-table layout-fixed']//th")
column_count = len(column)
print("Number of column is:-", column_count)

# Print specific data in table
count_coin = 0
for r in range(2, row_count+1):
    specific_data = driver.find_element(By.XPATH, "//table[@class='lcw-table layout-fixed']/tbody/tr["+str(r)+"]/td[8]/span").text
    print("percent change is:", specific_data)

    if "%" in specific_data:
        percent_float = float(specific_data.strip("%"))
        print("percent in float format:", percent_float)
    else:
        percent_float = float(specific_data)
        print("percent in float format in:", percent_float)

    if percent_float > 0.05:
        count_coin = count_coin+1
        coin_name = driver.find_element(By.XPATH, "//table[@class='lcw-table layout-fixed']/tbody/tr["+str(r)+"]/td[2]").text
        print("name of coin which is changed more then 0.05% is:", coin_name)
        print("Change in percent for 1hr:", percent_float)
        print(" ")
print("Total number of coins having change in 1hr more than 0.05 %:", count_coin)


# Print all data in table
# for ro in range(2, row_count+1): for col in range(2, column_count+1): data = driver.find_element(By.XPATH,
# "//table[@class='lcw-table layout-fixed']/tbody/tr["+str(ro)+"]/td["+str(col)+"]").text print(data, end=" ") print(
# " ")

driver.quit()
