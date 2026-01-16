from selenium.webdriver.common.by import By

class Checkout_Your_Information:
    first_name_xpath = "//input[@id='first-name']"
    last_name_xpath = "//input[@id='last-name']"
    zip_xpath = "//input[@id='postal-code']"
    cancel_id = "cancel"
    continue_id = "continue"
    finish_id = "finish"
    back_to_product_id = "back-to-products"






    def __init__(self,driver):
        self.driver = driver


    def checkout_your_information(self,first_name,last_name,zip_id_no):
        self.driver.find_element(By.XPATH, self.first_name_xpath).send_keys(first_name)
        self.driver.find_element(By.XPATH, self.last_name_xpath).send_keys(last_name)
        self.driver.find_element(By.XPATH, self.zip_xpath).send_keys(zip_id_no)
        self.driver.find_element(By.ID, self.continue_id).click()
        self.driver.find_element(By.ID, self.finish_id).click()
        self.driver.find_element(By.ID, self.back_to_product_id).click()






