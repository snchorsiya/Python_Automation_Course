from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/context_menu")
driver.maximize_window()

title = driver.title
print(title)

right_click = driver.find_element(By.ID, "hot-spot")

act = ActionChains(driver)
act.context_click(right_click).perform()
alert = driver.switch_to.alert
name = alert.text
print(name)
alert.accept()

driver.quit()