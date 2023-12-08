from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(
    executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(5)
driver.get("https://www.ironspider.ca/forms/dropdowns.htm")
driver.maximize_window()

title = driver.title
print(title)

# coffee_name = driver.find_element(By.NAME, "coffee")
# coffee = Select(coffee_name)
# # coffee_name.select_by_value("sugar")
# all_opt = coffee.options
# print(len(all_opt))
#
# # for a in all_opt:
# #     print(a.text)
#
# for i in all_opt:
#     if i.text == "With sugar":
#         i.click()
#         break

print("===========Without select method=============")

all_coffee = driver.find_elements(By.XPATH, "//*[@name='coffee']/option")
print(len(all_coffee))

for cof in all_coffee:
    print(cof.text)
    if cof.text == "With sugar":
        cof.click()
        break


all_drink = driver.find_element(By.XPATH, "//*[@name='coffee2']")
drink = Select(all_drink)
drink.select_by_value("cream")
drink.select_by_index(7)
drink.select_by_visible_text("Sugar")

dropdown = driver.find_element(By.XPATH, "//*[@name='coffee2']")
if dropdown.get_attribute("multiple"):
    print("multiple select option can be chosen")

else:
    print("Only one select option can be chosen")

driver.quit()