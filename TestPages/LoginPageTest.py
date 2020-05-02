from selenium import webdriver
import unittest
from Pages.LoginPage import Login_Page
from Pages.HomePage import Home_Page
#import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/BOND/PycharmProjects/SeleniumAutomation/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_value(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login = Login_Page(driver)

        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_on_login()

        homepage = Home_Page(driver)
        homepage.click_welcome()
        homepage.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")





