from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(5)
driver.get("https://www.dezlearn.com/nested-iframes-example/")
driver.maximize_window()

title = driver.title
print(title)

tex_print = driver.find_element(By.TAG_NAME, "h2")
print(tex_print.text)

driver.switch_to.frame("parent_iframe")
parents_text = driver.find_element(By.TAG_NAME, "h4")
print(parents_text.text)

driver.find_element(By.ID, "u_5_5").click()

parent_text = driver.find_element(By.ID, "processing")
print(parent_text.text)

# driver.switch_to.default_content()

driver.switch_to.frame("iframe1")
iframe_text = driver.find_element(By.TAG_NAME, "h4")
print(iframe_text.text)

driver.find_element(By.ID, "u_5_6").click()

ifrm_text = driver.find_element(By.ID, "processing")
print(ifrm_text.text)

driver.quit()