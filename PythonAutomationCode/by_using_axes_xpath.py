from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ch_option = Options()
ch_option.add_experimental_option("detach", True)

service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=ch_option)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# self: xpath axes
driver.find_element(By.XPATH, "//input[@name='email']/self::input").send_keys("sn@yopmail.com")

# following: xpath axes
driver.find_element(By.XPATH, "//input[@name='email']/following::input[1]").send_keys('Admin@123')
driver.find_element(By.XPATH, "//input[@name='email']/following::input[2]").click()
# driver.find_element(By.XPATH, "//input[@name='email']/following::input[3]").click()
driver.find_element(By.XPATH, "//input[@name='email']/following::input[4]").click()
driver.find_element(By.XPATH, "//input[@name='email']/following::input[6]").send_keys("23/11/2023")

# preceding: xpath axes
driver.find_element(By.XPATH, "//input[@name='email']/preceding::input").send_keys("Sheetal")