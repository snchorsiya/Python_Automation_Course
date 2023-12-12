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
driver.get("https://www.globalsqa.com/demoSite/practice/slider/range.html")
driver.maximize_window()

title = driver.title
print(title)

assert "Selenium Practice Slider - Range slider" in title

min_slider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
max_slider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")

# finding_location
min_location = min_slider.location
max_location = max_slider.location
print("location of min slider element before moving is:", min_location)
print("location of max slider element before moving is:", max_location)

# location of min slider element is: {'x': 202, 'y': 46}
# location of max slider element is: {'x': 808, 'y': 46}
price_range = driver.find_element(By.XPATH, "//input[@id='amount']").get_attribute("readonly")
print("Before Price:", price_range)
act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider, "200", "0").perform()
act.drag_and_drop_by_offset(max_slider, "-200", "0").perform()

min_location = min_slider.location
max_location = max_slider.location
print("location of min slider element after moving is:", min_location)
print("location of max slider element after moving is:", max_location)
print("After Price:", price_range)

driver.quit()