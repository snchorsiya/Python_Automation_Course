import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome(executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome()



def verify_title():
    driver.maximize_window()
    driver.get("https://www.google.com/")
    # driver.get("http://127.0.0.1:8000/")

    title = driver.title
    print(title)

    name = "Selenium with"

    expected_title = "Google"
    if title == expected_title:
        print("Title Verify Successfully")
        time.sleep(5)
        driver.find_element(By.NAME,"q").send_keys(name,' ',"Python")
        time.sleep(5)
        driver.find_element(By.NAME, 'btnK').send_keys(Keys.RETURN)
        title=driver.title
        print("After Click on Search box:",title)


    else:
        print(f"Title verify failed. Expected title '{expected_title}', but got '{title}")

    driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    verify_title()

# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
