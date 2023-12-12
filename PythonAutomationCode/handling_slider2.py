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
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

title = driver.title
print(title)

slider = driver.find_element(By.XPATH, "//div[@id='slider']/span")

slider_location = slider.location
print("Slider before:", slider_location)

act = ActionChains(driver)
act.drag_and_drop_by_offset(slider, "150", "0").perform()

slider_location = slider.location
print("Slider after:", slider_location)

driver.quit()