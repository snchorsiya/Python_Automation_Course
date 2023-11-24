from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)

service = ChromeService(
    executable_path="D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Mobile")
driver.find_element(By.ID, "nav-search-submit-button").click()

image = driver.find_elements(By.CLASS_NAME, "s-image")
print(len(image))

for i in image:
    print(i.get_property("alt"))

driver.close()
