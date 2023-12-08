from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import uuid

chr_options = Options()
chr_options.add_experimental_option("detach", True)
service = ChromeService(
    executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_options)


def generate_random_email_uuid():
    domain = "@yopmail.com"
    unique_id = str(uuid.uuid4()).replace("_", "")[:10]
    return unique_id + domain


driver.implicitly_wait(5)
driver.get("https://demo.nopcommerce.com/login")
driver.maximize_window()

title = driver.title
print(title)

login_name = driver.find_element(By.CSS_SELECTOR, "div[class='page-title'] h1").text
print(login_name)

random_email = generate_random_email_uuid()
print(random_email)

email = driver.find_element(By.NAME, "Email")
email.send_keys(random_email)

click_on_login = driver.find_element(By.CSS_SELECTOR, ".button-1.login-button")
print("Login Button name:-", click_on_login.text)
click_on_login.click()

emailText = driver.find_element(By.NAME, "Email")
print(emailText.get_attribute("value"))

validationMessage = driver.find_element(By.CSS_SELECTOR, ".message-error.validation-summary-errors").text
print(validationMessage)

driver.quit()
