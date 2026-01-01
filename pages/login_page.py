from .base_page import BasePage


class LoginPage(BasePage):
    """Page object for SauceDemo login page"""

    # Locators
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page):
        super().__init__(page)

    def navigate_to_login(self):
        """Navigate to login page"""
        self.navigate_to(self.base_url)

    def login(self, username: str, password: str):
        """Perform login with given credentials"""
        self.fill_input(self.USERNAME_INPUT, username)
        self.fill_input(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_visible(self) -> bool:
        """Check if error message is visible"""
        return self.is_element_visible(self.ERROR_MESSAGE)

    def is_login_successful(self) -> bool:
        """Check if login was successful by checking URL"""
        return "inventory" in self.page.url
