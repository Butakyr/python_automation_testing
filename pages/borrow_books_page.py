from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class BorrowBooksPage(BasePage):

    def __init__(self):
        super().__init__()
        self.borrow_books_link=self.find_element(By.XPATH, "//a[@href='https://catalog.wakegov.com/MyAccount/Home']")
