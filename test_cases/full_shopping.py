import time

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page.Checkout_Your_Information import Checkout_Your_Information
from base_page.Item_shopping_page import Item_shopping
from utilities import excel_utils
from utilities import read_properties
from utilities import custom_logger
from base_page.Login_Admin_Page import Login_Admin_Page
from utilities.custom_logger import Log_Maker
from utilities.read_properties import Read_Config


class Test_03_FullShopping():
    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path = ".//test_data//Admin_login.xlsx"
    status_list = []
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    firstname = "Prashant"
    lastname = "Mahadik"
    Zip_code = "411038"

    @pytest.mark.regression
    def test_full_shopping(self, setup):
        self.logger.info("****************test_full_shopping************")
        self.driver = setup

        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        print("url open")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.admin_lp = Login_Admin_Page(self.driver)

        # Wait for login fields and enter credentials
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.admin_lp.username_xpath)))
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_lp.login_xpath))).click()

        print("login success")
        self.title = self.driver.title
        if self.title == "Swag Labs":
            print("title is equal to Swag Labs ")
            self.logger.info(" ****************test_full_shopping Login success ***************")
        else:
            print("title is equal to Swag Labs")
            self.logger.info(" ****************test_full_shopping Login unsuccess ***************")

        self.shopping_cart = Item_shopping(self.driver)
        self.shopping_cart.Add_to_cart()
        self.logger.info(" ****************test_full_shopping add to cart success ***************")
        self.shopping_cart.cart_btn()
        print("product added to cart success")
        self.logger.info(" ****************test_full_shopping cart button click success ***************")
        self.shopping_cart.checkout_btn()
        print("product checkout success")
        self.checkout_info = Checkout_Your_Information(self.driver)
        self.checkout_info.checkout_your_information(self.firstname, self.lastname, self.Zip_code)
        print("product checkout info success")
        print("shopping done for regression ")
        self.driver.quit()
        self.logger.info("******************shopping done *************")

    def test_full_shopping111(self, setup):
        self.logger.info("****************test_full_shopping************")
        self.driver = setup

        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        print("url open")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.admin_lp = Login_Admin_Page(self.driver)

        # Wait for login fields and enter credentials
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.admin_lp.username_xpath)))
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_lp.login_xpath))).click()

        print("login success 111111")
        self.title = self.driver.title
        if self.title == "Swag Labs":
            print("title is equal to Swag Labs 1111111")
            self.logger.info(" ****************test_full_shopping Login success ***************")
        else:
            print("title is equal to Swag Labs")
            self.logger.info(" ****************test_full_shopping Login unsuccess ***************")

        self.shopping_cart = Item_shopping(self.driver)
        self.shopping_cart.Add_to_cart()
        self.logger.info(" ****************test_full_shopping add to cart success ***************")
        self.shopping_cart.cart_btn()
        print("product added to cart success")
        self.logger.info(" ****************test_full_shopping cart button click success ***************")
        self.shopping_cart.checkout_btn()
        print("product checkout success")
        self.checkout_info = Checkout_Your_Information(self.driver)
        self.checkout_info.checkout_your_information(self.firstname, self.lastname, self.Zip_code)
        print("product checkout info success")
        print("shopping done")
        self.driver.quit()
        self.logger.info("******************shopping done *************")

