import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"E:\Python_Automation_Course-master\Python_Automation_Course-master\drivers\chromedriver.exe")


preferences = {"download.default_directory":r"E:\Python_Automation_Course-master\Python_Automation_Course-master\download_file"}
my_options = webdriver.ChromeOptions()
my_options.add_experimental_option('prefs', preferences)

driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()

title = driver.title
print(title)

driver.find_element(By.XPATH, "//*[@id='content']/div/a[13]").click()
time.sleep(7)
