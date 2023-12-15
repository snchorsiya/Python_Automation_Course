import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(10)

driver.get("https://onlinenotepad.org/notepad")
driver.maximize_window()

title = driver.title
print(title)

driver.switch_to.frame("editor_ifr")

driver.find_element(By.ID, "tinymce").send_keys("Welcome to qa automation")

act = ActionChains(driver)

# Select text ctrl + A
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

# Copy the text ctrl + C
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()

# Press right array keys
act.send_keys(Keys.ARROW_RIGHT)
act.send_keys(Keys.ENTER)

act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()

driver.quit()

