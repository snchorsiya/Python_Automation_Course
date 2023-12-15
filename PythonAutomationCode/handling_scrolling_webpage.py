import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(10)

driver.get("https://www.gsmarena.com/makers.php3")
# driver.maximize_window()

title = driver.title
print(title)

# driver.execute_script("window.scrollBy(0, 500);")
#
# print(driver.execute_script("return window.pageYOffset;"))
#
# driver.execute_script("window.scrollBy(0, 700);")
# print(driver.execute_script("return window.pageYOffset;"))
#
# time.sleep(5)
# driver.execute_script("window.scrollBy(0, -500);")
# print(driver.execute_script("return window.pageYOffset;"))

# element = driver.find_element(By.XPATH, "//table/tbody/tr[40]/td[1]")
# driver.execute_script("arguments[0].scrollIntoView();", element)

time.sleep(7)

# element1 = driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[1]")
# driver.execute_script("arguments[0].scrollIntoView();", element1)

driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

time.sleep(5)

driver.execute_script("window.scrollBy(0, -document.body.scrollHeight);")


# driver.close()