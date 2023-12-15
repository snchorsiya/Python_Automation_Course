import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(
    executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(10)
driver.get("https://www.ibm.com/planetwide/select/selector.html")
driver.maximize_window()

title = driver.title
print(title)

date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print(date)

# driver.save_screenshot("D:\\Automation\\PythonAutomation\\Chromedriver-webdrivermanger\\ScreenShot\\homepage.png")
# driver.save_screenshot(os.getcwd()+"//ScreenShot//homepage1.png")

# driver.get_screenshot_as_file(os.getcwd()+"//ScreenShot//homepage1.png")

# driver.get_screenshot_as_base64()  # return image base64 encoded string format
# driver.get_screenshot_as_png()  # return image data a binary data.

# taking a screenshot of specific web element
button = driver.find_element(By.ID, "truste-consent-button")
button.screenshot(os.getcwd() + f"//ScreenShot//button_{date}.png")

driver.quit()
