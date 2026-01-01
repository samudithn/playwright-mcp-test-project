from playwright.sync_api import Page
from config.config import BASE_URL, PAGE_LOAD_TIMEOUT, ELEMENT_WAIT_TIMEOUT


class BasePage:
    """Base class for all page objects"""

    def __init__(self, page: Page):
        self.page = page
        self.base_url = BASE_URL
        self.page.set_default_timeout(ELEMENT_WAIT_TIMEOUT)

    def navigate_to(self, url: str):
        """Navigate to a specific URL"""
        self.page.goto(url)

    def wait_for_load(self):
        """Wait for page to load"""
        self.page.wait_for_load_state("networkidle")

    def get_title(self) -> str:
        """Get page title"""
        return self.page.title()

    def take_screenshot(self, name: str):
        """Take a screenshot"""
        self.page.screenshot(path=f"screenshots/{name}.png")

    def click_element(self, selector: str):
        """Click an element by selector"""
        self.page.click(selector)

    def fill_input(self, selector: str, text: str):
        """Fill an input field"""
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        """Get text from an element"""
        return self.page.text_content(selector)

    # def is_element_visible(self, selector: str) -> bool:
    #    """Check if element is visible"""
    #    return self.page.is_visible(selector)
