from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_Admin_Page:   #👉 Defines a Page Object Model (POM) class for the Admin Login page.
    username_xpath = "//input[@id='user-name']"  #👉 Stores the XPath locator for the username (email) input field.
    password_xpath = "//input[@id='password']" #👉 Stores the XPath locator for the password input field.
    login_xpath = "//input[@id='login-button']"
    burger_btn_xpath = "//button[@id='react-burger-menu-btn']"
    logout_btn_xpath = "//a[@id='logout_sidebar_link']"

    def __init__(self, driver):  #👉 Constructor method that runs when the class object is created.
        self.driver = driver  #👉 Assigns the WebDriver instance to the class so all methods can use it.

    def enter_username(self,username): #👉 Defines a method to enter username into the login form.
        self.driver.find_element(By.XPATH ,self.username_xpath).clear() #👉 Finds the username field using XPath and clears existing text.
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username) #👉 Types the provided username into the username field.

    def enter_password(self, password):  #👉 Defines a method to enter password.
        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)


    def click_login(self):  #👉 Defines a method to click the login button.
        self.driver.find_element(By.XPATH ,self.login_xpath).click()  #👉 Finds the login button and clicks it.

    def click_burger_btn(self):
        self.driver.find_element(By.XPATH,self.burger_btn_xpath).click()

    def logout(self):
        self.driver.find_element(By.XPATH,self.logout_btn_xpath).click()




