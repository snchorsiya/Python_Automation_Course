import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(10)

driver.get("https://www.ibm.com/planetwide/select/selector.html")
driver.maximize_window()

title = driver.title
print(title)

# url = driver.find_element(By.NAME, "url")
# drp = Select(url)
# drp.select_by_value("http://www.ibm.com/aw/en/")

driver.find_element(By.ID, "truste-consent-button").click()

driver.find_element(By.ID, "select2-ibm_select-container").click()
country_list = driver.find_elements(By.XPATH, "//li[@class='select2-results__option']")
count_country = len(country_list)
print("Number of country list:", count_country)

for country in country_list:
    # print(country.text)
    if "India" in country.text:
        country.click()
        break

driver.quit()
