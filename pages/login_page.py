from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utilities.config_reader import ConfigReader


class LoginPage(BasePage):

    def __init__(self):
        super().__init__()
        self.username_input_box = self.find_element(By.XPATH, "//input[@id='username']") # instance variables
        self.password_input_box = self.find_element(By.XPATH, "//input[@id='password']")
        self.sign_in_button = self.driver.find_element(By.XPATH, "//input[@id='loginFormSubmit']")

#static final USERNAME and PASSSWORD
    __USERNAME = ConfigReader.get_env("Lib-Student-User", "username")
    __PASSWORD = ConfigReader.get_env("Lib-Student-User", "password")

#username: str = __USERNAME)-> means value must be str. If its not set, by default it is __USERNAME
    def enter_username(self, username: str = __USERNAME): #default Username
        self.username_input_box.send_keys(username)

    def enter_password(self, password: str = __PASSWORD):
        self.password_input_box.send_keys(password)

    def login(self, username: str = __USERNAME, password: str = __PASSWORD):
        self.enter_username(username)
        self.enter_password(password)
        self.sign_in_button.click()
        WebDriverWait(self.driver, 5).until(EC.title_is("Library"))
        assert self.driver.title.strip() == "Library"
