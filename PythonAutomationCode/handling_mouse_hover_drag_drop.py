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
driver.get("https://demo.automationtesting.in/Static.html")
driver.maximize_window()

title = driver.title
print(title)

drag1 = driver.find_element(By.XPATH, "//img[@id='angular']")
drag2 = driver.find_element(By.XPATH, "//img[@id='mongo']")
drag3 = driver.find_element(By.XPATH, "//img[@id='node']")
drop = driver.find_element(By.XPATH, "//div[@id='droparea']")

act = ActionChains(driver)

act.drag_and_drop(drag1, drop).perform()
act.drag_and_drop(drag2, drop).perform()
act.drag_and_drop(drag3, drop).perform()

# driver.close()

driver.get("https://testautomationpractice.blogspot.com/")

dra = driver.find_element(By.ID, "draggable")
dro = driver.find_element(By.ID, "droppable")

act.drag_and_drop(dra, dro).perform()
print("drag and drop is completed")


driver.quit()