from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import openpyxl
import utility

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(
    executable_path=r"D:\Automation\PythonAutomation\Chromedriver-webdrivermanger\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.get("https://homeloans.sbi/calculators")
driver.maximize_window()

title = driver.title
print(title)

driver.execute_script("window.scrollBy(0,300);")

file = "C:\\Users\\Sheetal.Chorsiya\\Downloads\\Test_Data_Home_Loan.xlsx"

rows = utility.get_row_count(file, "Sheet1")

for ro in range(2, rows+1):
    # fetching data from sheet
    loan_amount = utility.read_data(file, "Sheet1", ro, 1)
    tenure = utility.read_data(file, "Sheet1", ro, 2)
    interest_rate = utility.read_data(file, "Sheet1", ro, 3)
    exp_emi = utility.read_data(file, "Sheet1", ro, 4)

    # passing test data to app
    home_loan = driver.find_element(By.ID, "loanamount_DEFAULTEMICAL")
    home_loan.clear()
    home_loan.send_keys(loan_amount)

    loan_tenure = driver.find_element(By.ID, "loanTenureValue_DEFAULTEMICAL")
    loan_tenure.clear()
    loan_tenure.send_keys(tenure)

    loan_interest = driver.find_element(By.ID, "loanInterestRate_DEFAULTEMICAL")
    loan_interest.clear()
    loan_interest.send_keys(interest_rate)

    actual_emi = driver.find_element(By.ID, "totalEmiDef").text
    new_actual_emi = actual_emi.replace("₹", " ").strip()

    # validation
    if int(exp_emi) == int(new_actual_emi):
        utility.write_data(file, "Sheet1", ro, 6, "Passed")
        utility.fill_green(file, "Sheet1", ro, 6)
    else:
        utility.write_data(file, "Sheet1", ro, 6, "Failed")
        utility.fill_red(file, "Sheet1", ro, 6)


driver.close()