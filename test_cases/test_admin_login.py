import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_page.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalide_username = Read_Config.get_invalide_username()
    logger = Log_Maker.log_gen()




    def test_title_verification(self,setup):
        self.logger.info("*********************Test_01_Admin_Login_started**********************************")
        self.logger.info("*********************test_title_verification_started**********************************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "Swag Labs"
        if exp_title == act_title:
            self.logger.info("*********************test_title_verification_matched**********************************")
            assert True
            self.driver.close()
        else:
            self.logger.info("*********************test_title_verification_not_matched**********************************")
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.driver.close()
            assert False


    def test_valid_admin_login(self,setup):
        self.logger.info("*********************test_valid_admin_login_started**********************************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        act_dashboard_text = self.driver.find_element(By.XPATH,"//span[@class='title']").text
        print("text",act_dashboard_text)
        if act_dashboard_text == "Products":
            self.logger.info("*********************test_valid_admin_login_successfully**********************************")
            assert True
            self.driver.close()
        else:
            self.logger.info("*********************test_valid_admin_login_unsuccessfully**********************************")
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False

    def test_invalid_admin_login(self,setup):
        self.logger.info("*********************test_invalid_admin_login_started**********************************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalide_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        error_msg = self.driver.find_element(By.XPATH,"//h3[@data-test='error']").text
        if error_msg == "Epic sadface: Username and password do not match any user in this service":
            self.logger.info("*********************test_invalid_admin_login_successfully*******************************************")
            assert True
            self.driver.close()
        else:
            self.logger.info("*********************test_invalid_admin_login_unsuccessfully*******************************************")
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False


