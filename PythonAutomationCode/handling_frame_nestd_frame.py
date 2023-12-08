import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()

title = driver.title
print(title)

driver.find_element(By.LINK_TEXT, "Frames").click()
# driver.find_element(By.LINK_TEXT, "iFrame").click()
#
# driver.switch_to.frame("mce_0_ifr")
# driver.find_element(By.ID, "tinymce").clear()
# driver.find_element(By.ID, "tinymce").send_keys("Hello Sheetal")
#
# driver.switch_to.default_content()
# inside_fram = driver.find_element(By.TAG_NAME, "h3")
# print(inside_fram.text)

driver.find_element(By.LINK_TEXT, "Nested Frames").click()
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-middle")
midd = driver.find_element(By.ID, "content")
print(midd.text)
driver.switch_to.default_content()
time.sleep(5)
driver.switch_to.frame("frame-top")
right = driver.find_element(By.XPATH, "/html/frameset/frame[3]")
# driver.switch_to.frame("frame-right")
driver.switch_to.frame(right)
rig = driver.find_element(By.TAG_NAME, "body")
print(rig.text)

driver.quit()