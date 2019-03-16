class LoginPage1:
    def __init__(self,driver):
        self.driver=driver
        self.un_locator='username'
        self.pwd_locator='pwd'

    def enter_un(self):
        self.driver.find_element_by_id(self.un_locator).send_keys("admin")

    def enter_pwd(self):
        self.driver.find_element_by_name(self.pwd_locator).send_keys("manager")

