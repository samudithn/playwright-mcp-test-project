import pytest
from pages.login_page import LoginPage
from config.config import VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD, LOCKED_USERNAME


class TestLogin:
    """Test cases for login functionality"""

    def test_successful_login(self, page):
        """Positive: Successful login with valid credentials"""
        login_page = LoginPage(page)
        login_page.navigate_to_login()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        # Verify login success
        assert login_page.is_login_successful(), "Login should be successful"
        assert "inventory" in page.url, "Should redirect to inventory page"

    def test_invalid_username_login(self, page):
        """Negative: Login with invalid username"""
        login_page = LoginPage(page)
        login_page.navigate_to_login()
        login_page.login(INVALID_USERNAME, VALID_PASSWORD)

        # Verify error message
        assert login_page.is_error_visible(), "Error message should be visible"
        assert "Username and password do not match" in login_page.get_error_message()

    def test_invalid_password_login(self, page):
        """Negative: Login with invalid password"""
        login_page = LoginPage(page)
        login_page.navigate_to_login()
        login_page.login(VALID_USERNAME, INVALID_PASSWORD)

        # Verify error message
        assert login_page.is_error_visible(), "Error message should be visible"
        assert "Username and password do not match" in login_page.get_error_message()

    def test_locked_user_login(self, page):
        """Negative: Login with locked out user"""
        login_page = LoginPage(page)
        login_page.navigate_to_login()
        login_page.login(LOCKED_USERNAME, VALID_PASSWORD)

        # Verify locked user error
        assert login_page.is_error_visible(), "Error message should be visible"
        assert "Sorry, this user has been locked out" in login_page.get_error_message()

    def test_empty_credentials_login(self, page):
        """Negative: Login with empty credentials"""
        login_page = LoginPage(page)
        login_page.navigate_to_login()
        login_page.login("", "")

        # Verify error message for empty username
        assert login_page.is_error_visible(), "Error message should be visible"
        assert "Username is required" in login_page.get_error_message()

    def test_empty_password_login(self, page):
        """Negative: Login with empty password"""
        login_page = LoginPage(page)
        login_page.navigate_to_login()
        login_page.login(VALID_USERNAME, "")

        # Verify error message for empty password
        assert login_page.is_error_visible(), "Error message should be visible"
        assert "Password is required" in login_page.get_error_message()
