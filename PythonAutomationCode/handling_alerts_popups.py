from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

title = driver.title
print(title)

driver.find_element(By.XPATH, "//button[normalize-space()='Alert']").click()

alert = driver.switch_to.alert
name = alert.text
print(name)
alert.accept()

driver.find_element(By.XPATH, "//button[normalize-space()='Confirm Box']").click()

alert_confirm = driver.switch_to.alert
text = alert_confirm.text
print(text)
alert.dismiss()
msg = driver.find_element(By.ID, "demo")
print(msg.text)

driver.find_element(By.XPATH, "//button[normalize-space()='Prompt']").click()

alert_prompt = driver.switch_to.alert
tex_meg = alert_prompt.text
print(tex_meg)
alert_prompt.send_keys("Sheetal")
# alert_prompt.accept()
alert_prompt.dismiss()
ms = driver.find_element(By.ID, "demo")
print(ms.text)


driver.quit()