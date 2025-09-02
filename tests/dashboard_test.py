from pages.borrow_books_page import BorrowBooksPage
import time


def test_borrow_books_link(driver):
    borrow_books_page = BorrowBooksPage()
    assert borrow_books_page.borrow_books_link.is_displayed(), "Borrowing Books link is not visible "
    assert borrow_books_page.borrow_books_link.is_enabled(), "Borrowing Books Link is not enabled"
    borrow_books_page.borrow_books_link.click()
    time.sleep(3)


"""
Test Case: Verify that borrow books link is visible and clickable
     Step 1: User is already on the homepage
     Step 2: Assert that the Borrowing Books Link is visible
     Step 3: Assert that the Borrowing Books Link is enabled
     Step 4: Click the Borrowing Books Link

     Here is the xpath for locating the Borrowing Books Link element:
     //a[@href='borrowing-books
"""