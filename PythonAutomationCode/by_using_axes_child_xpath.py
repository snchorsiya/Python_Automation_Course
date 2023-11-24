from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeSrvice
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ch_options = Options()
ch_options.add_experimental_option("detach", True)
service = ChromeSrvice(
    executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=ch_options)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# child: xpath axes
links = driver.find_elements(By.XPATH, "//ul[@class='list']/child::li/a")
num = len(links)
for i in links:
    print(i.get_attribute("href"))

print("total of link number: ", num)

print("============Parent xpath axes==================")

# parent: xpath axes
parentTag = driver.find_elements(By.XPATH, "//*[text()='About us']/parent::li/parent::ul/child::li")
print("Count of links present inside Information section:", parentTag.__len__())

print("============Ancestor xpath axes==================")

# ancestor: cpath axes
ancestorTag = driver.find_elements(By.XPATH, "//*[text()='Blog']/ancestor::ul/child::li")
print("Count of link ancestor inside information section:", ancestorTag.__len__())

driver.find_element(By.XPATH, "//*[@id='poll-block-1']/descendant::input[3]").click()