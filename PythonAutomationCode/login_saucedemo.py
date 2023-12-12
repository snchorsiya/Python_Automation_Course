from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("excludeSwitches", ["enable-logging"])
chr_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_option)

driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
title = driver.title
print(title)

assert 'Swag Labs' in title
print("TEST 0: `title` test passed")

driver.find_element(By.NAME, "user-name").send_keys("standard_user")
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
driver.find_element(By.NAME, "login-button").click()

text = driver.find_element(By.CLASS_NAME, "title").text
print(text)

assert 'products' in text.lower()
print("TEST PASSED: LOGIN SUCCESSFUL")

add_to_cart_btn = driver.find_elements(By.CLASS_NAME, "btn_inventory")

for btn in add_to_cart_btn[:3]:
    btn.click()

cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

assert "3" in cart_value.text
print("TEST PASSED : ADD TO CART", "\n")

# print("testing remove from cart")
# remove_btn = driver.find_elements(By.CLASS_NAME, "btn_inventory")
#
# for rem_btn in remove_btn[:2]:
#     rem_btn.click()
#
# assert "1" in cart_value.text
# print("TEST PASSED : REMOVE FROM CART", "\n")

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

item_price = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

add = 0
for price in item_price:
    pri = price.text
    print(pri)
    float_pri = pri.strip().lstrip("$")
    print(float_pri)
    add = add + float(float_pri)
print("The total amount of:", "$", add)

driver.find_element(By.CLASS_NAME, "checkout_button ").click()

driver.find_element(By.ID, "first-name").send_keys("qa")
driver.find_element(By.ID, "last-name").send_keys("test")
driver.find_element(By.ID, "postal-code").send_keys("123456")
driver.find_element(By.ID, "continue").click()

item_total = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
tax = driver.find_element(By.CLASS_NAME, "summary_tax_label").text
# it_total = item_total.split("$")
it_total = item_total.split("$")[1].strip().split(" ")[0]
print(it_total)
ta = tax.split("$")[1].strip().split(" ")[0]
print(ta)

assert it_total > ta

total_add = 0
total = total_add + float(it_total) + float(ta)
print("After add the tax the total of amount: ", total)

sub_total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
all_total = sub_total.split("$")[1].strip().split(" ")[0]

# all_total = sub_total.split("$")
assert float(total) == float(all_total)

driver.find_element(By.ID, "finish").click()

message = driver.find_element(By.CLASS_NAME, "complete-header").text
print(message)

driver.quit()

