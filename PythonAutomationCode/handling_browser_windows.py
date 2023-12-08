from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

title = driver.title
print(title)
# windowId = driver.current_window_handle  # return window id of current page
# print(windowId)
# driver.switch_to.window(windowId)
driver.find_element(By.XPATH, "//a[@href='https://www.linkedin.com/company/orangehrm/mycompany/']").click()
driver.find_element(By.XPATH, "//a[@href='https://twitter.com/orangehrm?lang=en']").click()
driver.find_element(By.XPATH, "//a[@href='https://www.youtube.com/c/OrangeHRMInc']").click()
windowId = driver.window_handles  # return window id of current page
print("Parent window:", windowId[0], "\nChild window:", windowId[1], "\nnewChild window:", windowId[2],
      "\nYouChild window:", windowId[3])

# print("Parent page title:", driver.title)
# driver.switch_to.window(windowId[1])
# print("child page title:", driver.title)
# driver.switch_to.window(windowId[0])
# driver.close()

for win_id in windowId:
    driver.switch_to.window(win_id)
    if driver.title == "OrangeHRM" or driver.title == "Blocked site" or driver.title == " ":
        driver.close()

# driver.close()

