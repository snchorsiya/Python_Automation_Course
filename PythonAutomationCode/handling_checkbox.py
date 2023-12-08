from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(
    executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=service, options=chr_option)

driver.get("https://www.ironspider.ca/forms/checkradio.htm")
driver.maximize_window()

title = driver.title
print(title)

print("======:Click on Single checkbox:======")
single_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='red']")
single_checkbox.click()
print(single_checkbox.is_selected())
single_checkbox.click()
print(single_checkbox.is_selected())

print("======:Click on all checkbox:======")
all_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print("Number of checkbox", len(all_checkboxes))

for checkbox in all_checkboxes:
    checkbox.click()
    print(checkbox.get_attribute("value"), ":", checkbox.is_selected())
    checkbox.click()
    print(checkbox.is_selected())

print("======:Click on multiple checkbox based on choice:======")

for ele in all_checkboxes:
    value = ele.get_attribute("value")
    if (value == "yellow") or (value == "orange") or (value == "purple"):
        ele.click()
        print(ele.is_selected())
        ele.click()
        print("After unchecked checkbox", ele.is_selected())

print("======:Click on last 2 checkbox:======")
for i in range(len(all_checkboxes)-2, len(all_checkboxes)):
    all_checkboxes[i].click()
    print(all_checkboxes[i].is_selected())
    all_checkboxes[i].click()
    print(all_checkboxes[i].is_selected())

print("======:Click on first 2 checkbox:======")
for j in range(len(all_checkboxes)):
    if j < 2:
        all_checkboxes[j].click()
        print(all_checkboxes[j].is_selected())
        all_checkboxes[j].click()
        print(all_checkboxes[j].is_selected())

print("======:Click on uncheck checkbox:======")
for el in all_checkboxes:
    if el.is_selected():
        el.click()
    print(el.is_selected())


driver.quit()
