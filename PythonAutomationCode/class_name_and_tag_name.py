from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)

service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))  # count of all links

for link in links:
    print(link.get_property("href"))

print("================Print Class Name====================")

Search = (driver.find_element(By.ID, "small-searchterms"))
Search.send_keys("Cell phones")

driver.find_element(By.XPATH, "(//button[@class='button-1 search-box-button'])[1]").click()

img = driver.find_elements(By.TAG_NAME, "img")
print(len(img))

for i in img:
    print(i.get_property("alt"))


driver.close()