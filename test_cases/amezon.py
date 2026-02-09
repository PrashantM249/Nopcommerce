import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page.Login_Admin_Page import Login_Admin_Page
from utilities import excel_utils
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker




driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://google.com")

email_field = driver.find_element(By.XPATH,"//input[@id='login_email']")
email_field.clear()
email_field.send_keys("receptionist1@gmail.com")

password_field = driver.find_element(By.XPATH,"//input[@id='login_password']")
password_field.clear()
password_field.send_keys("test@1234#")

driver.find_element(By.XPATH,"//button[@type='submit']").click()

wait = WebDriverWait(driver, 15)
# Wait for the page to load by checking for the body element
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
print("Page Title after login:", driver.title)





# driver.get("https://www.amazon.in/s?k=iphone&crid=2687QC7PAZUYB&sprefix=iphone%2Caps%2C379&ref=nb_sb_noss_2")

# products = driver.find_elements(By.XPATH,"//div[@data-component-type='s-search-result']")
# iphone_prices = []

# for product in products:
#     try:
#         title = product.find_element(By.XPATH, ".//h2//span").text
#         price = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").text

#         # Clean price (remove commas)
#         price = int(price.replace(",", ""))

#         if "iphone" in title.lower():
#             iphone_prices.append((title, price))
#             print(f"{title}  ---> ₹{price}")

#     except:
#         continue

# # Find lowest price
# lowest_iphone = min(iphone_prices, key=lambda x: x[1])

# print("\n✅ Lowest Priced iPhone:")
# print(f"{lowest_iphone[0]}  ---> ₹{lowest_iphone[1]}")

driver.quit()