from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(
    executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(10)
driver.get("https://www.minopcloud.com/")
# driver.switch_to.new_window('tab')
driver.switch_to.new_window("window")
driver.get("https://www.google.com/")
driver.maximize_window()

title = driver.title
print(title)


# driver.find_element(By.ID, "onesignal-slidedown-cancel-button").click()
#
# click_about = driver.find_element(By.LINK_TEXT, "About Us")
# # click_about.click()
#
# ctrl_enter = Keys.CONTROL + Keys.ENTER
# click_about.send_keys(ctrl_enter)
# driver.switch_to.window(driver.window_handles[1])
#
# title = driver.title
# print(title)

driver.quit()