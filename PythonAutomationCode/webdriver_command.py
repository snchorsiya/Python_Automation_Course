from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

# to keep the browser
ch_option = Options()
ch_option.add_experimental_option("detach", True)
#
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=ch_option)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

title = driver.title
print("THe page of title is:-", title)

url = driver.current_url
print("Current url is:-", url)

web_source = driver.page_source
print("Page source is:-", web_source)
