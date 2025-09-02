from pages.home_page import HomePage
from pages.login_page import LoginPage
import pytest

@pytest.mark.smoke
def test_profile_name2(driver):
    assert HomePage().user_profile_link.is_displayed()
    assert "Student" not in HomePage().user_profile_link.text


def test_books_link2(driver):
    assert HomePage().books_link.is_displayed()
    assert HomePage().books_link.is_enabled()
