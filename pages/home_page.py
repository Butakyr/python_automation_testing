from selenium.webdriver.remote.webelement import WebElement

selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

#creating instance variables using Constructor
    def __init__(self):#constructor
        super().__init__() #inside the constructors
        self.user_profile_link = self.find_element(By.XPATH, "//a[@id='navbarDropdown']")
        self.books_link = self.find_element(By.XPATH, "//a[@href='#books']")


