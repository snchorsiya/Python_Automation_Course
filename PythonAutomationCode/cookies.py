from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(10)

driver.get("https://www.google.com/")

driver.maximize_window()

title = driver.title
print(title)

# fetch all cookies
all_cookies = driver.get_cookies()
print("Number of cookies present:", len(all_cookies))
cookie = {'name': 'mycookie', 'value': 'myvalue'}
driver.add_cookie(cookie)
all_cookies = driver.get_cookies()
print("Number of cookies present:", len(all_cookies))
print(driver.get_cookie('mycookie'))
driver.delete_cookie('mycookie')
all_cookies = driver.get_cookies()
print("Number of cookies present:", len(all_cookies))
# for c in all_cookies:
#     print(c)
#     print(c.get('name'))  # print all attribute of name value
#     print(c.get("value"))

driver.delete_all_cookies()
all_cookies = driver.get_cookies()
print("Number of cookies present:", len(all_cookies))
driver.close()