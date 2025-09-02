from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class DashboardPage(BasePage):

    def __init__(self):
        super().__init__()
        self.dashboard_link= self.find_element(By.XPATH, "//a[@id='headerMyAccountLink']")
