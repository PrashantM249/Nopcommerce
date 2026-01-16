
from selenium.webdriver.common.by import By



class Item_shopping:
    add_to_cart_xpath = "//button[@id='add-to-cart-sauce-labs-backpack']"
    cart_xpath = "//a[@class='shopping_cart_link']"
    remove_from_cart_id = "remove-sauce-labs-backpack"
    checkout_id = "//button[@id='checkout']"

    def __init__(self,driver):
        self.driver = driver


    def Add_to_cart(self):
        self.driver.find_element(By.XPATH,self.add_to_cart_xpath).click()


    def Remove_from_cart(self):
        self.driver.find_element(By.ID, self.remove_from_cart_id).click()



    def cart_btn(self):
        self.driver.find_element(By.XPATH, self.cart_xpath).click()

    def checkout_btn(self):
        self.driver.find_element(By.XPATH, self.checkout_id).click()




