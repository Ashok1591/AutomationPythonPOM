from Locators_Folder.Locators import Locators

class Login_Page():

    def __init__(self,driver):
        self.driver = driver

        self.username_id = Locators.username_id
        self.password_id = Locators.password_id
        self.login_btn_id = Locators.login_btn_id


    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def click_on_login(self):
        self.driver.find_element_by_id(self.login_btn_id).click()

