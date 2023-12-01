from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(
    executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.get("https://demo.nopcommerce.com/login")
driver.maximize_window()

title = driver.title
print(title)
# driver.find_element()
# When locator is pointing to single web-element
email_filed = driver.find_element(By.ID, "Email")
email_filed.send_keys("demo@yopmail.com")

# When locator is pointing to multiple web-element
links = driver.find_elements(By.XPATH, "//div[@class='footer-upper']//a")
print(type(links))
print("===========================")
print(links[0].text)
print("=================================")
count = len(links)
print(count)

for link in links:
    name = link.text
    print(name, ":", link.get_property("href"))



# # When locator is not pointing to any web-element
# password_filed = driver.find_element(By.ID, "dfdfd")
# password_filed.send_keys("demo@yopmail.com")

print("=========================================")
# When locator is pointing to single web-element
password_filed = driver.find_elements(By.ID, "Password")
print(type(password_filed))
print(len(password_filed))
password_filed[0].send_keys("demo@yopmail.com")

driver.quit()
