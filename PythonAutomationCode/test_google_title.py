from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

# options = webdriver.ChromeOptions()
# service = ChromeService(executable_path="D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service, options=options)

# options = webdriver.FirefoxOptions()
# service = FirefoxService(executable_path="D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\geckodriver.exe")
# driver = webdriver.Firefox(service=service, options=options)

options = webdriver.EdgeOptions()
service = EdgeService(executable_path="D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=options)

# driver = webdriver.Chrome()
driver.get("https://www.google.com")


expected_title = "Google"
actual_title = driver.title
print(actual_title)

if expected_title == actual_title:
    print("The test case pass")

else:
    print("The test case fail")
