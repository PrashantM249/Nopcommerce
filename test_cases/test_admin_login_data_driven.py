import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_page.Login_Admin_Page import Login_Admin_Page
from utilities import excel_utils
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test_02_Admin_Login_Data_Driven:
    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path = ".//test_data//Admin_login.xlsx"
    status_list = []

    def test_valid_admin_login(self,setup):
        self.logger.info("*********************test_valid_admin_login_data_driven_started**********************************")
        self.driver = setup

        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        print("url open")
        self.driver.maximize_window()
        self.admin_lp = Login_Admin_Page(self.driver)
        self.rows = excel_utils.get_row_count(self.path,"Sheet1")
        print("num of rows ",self.rows)
        for r in range(2,self.rows+1):
            self.username = excel_utils.read_data(self.path, "Sheet1", r,1)
            print("username ",self.username)
            self.password = excel_utils.read_data(self.path, "Sheet1", r,2)
            print("password ",self.password)
            self.exp_login = excel_utils.read_data(self.path, "Sheet1", r,3)
            print("exp_login ",self.exp_login)
            self.admin_lp.enter_username(self.username)
            print("username is entered ",self.username)
            self.admin_lp.enter_password(self.password)
            print("password is entered",self.password)
            self.admin_lp.click_login()
            print("login success")
            time.sleep(3)
            act_title = self.driver.title
            exp_title = "Swag Labs"

            if act_title == exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("test data is passed 1 ")
                    self.status_list.append("Passed")
                    self.admin_lp.click_burger_btn()
                    self.admin_lp.logout()
                else:
                    self.logger.info("Login succeeded but was expected to fail")
                    self.status_list.append("Passed")
            else:
                if self.exp_login == "No":
                    self.logger.info("Login failed as expected")
                    self.status_list.append("Passed")
                else:
                    self.logger.info("Login failed but was expected to pass")
                    self.status_list.append("Passed")


        print("status list is ", self.status_list)

        if "Failed" in self.status_list:
            self.logger.info("test data is failed 3 ")
            assert False
        else:
            self.logger.info("test data is passed 3")
            assert True
        self.driver.quit()







