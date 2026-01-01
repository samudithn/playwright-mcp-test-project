from .base_page import BasePage


class CheckoutPage(BasePage):
    """Page object for SauceDemo checkout pages"""

    # Step One Locators
    FIRST_NAME_INPUT = "[data-test='firstName']"
    LAST_NAME_INPUT = "[data-test='lastName']"
    POSTAL_CODE_INPUT = "[data-test='postalCode']"
    CONTINUE_BUTTON = "[data-test='continue']"
    CANCEL_BUTTON = "[data-test='cancel']"

    # Step Two Locators
    CHECKOUT_SUMMARY = ".checkout_summary_container"
    FINISH_BUTTON = "[data-test='finish']"
    ITEM_TOTAL = ".summary_subtotal_label"
    TAX = ".summary_tax_label"
    TOTAL = ".summary_total_label"

    # Complete Locators
    COMPLETE_HEADER = ".complete-header"
    BACK_HOME_BUTTON = "[data-test='back-to-products']"

    def __init__(self, page):
        super().__init__(page)

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        """Fill checkout information form"""
        self.fill_input(self.FIRST_NAME_INPUT, first_name)
        self.fill_input(self.LAST_NAME_INPUT, last_name)
        self.fill_input(self.POSTAL_CODE_INPUT, postal_code)
        self.click_element(self.CONTINUE_BUTTON)

    def get_item_total(self) -> str:
        """Get item total from summary"""
        return self.get_text(self.ITEM_TOTAL)

    def get_tax(self) -> str:
        """Get tax amount from summary"""
        return self.get_text(self.TAX)

    def get_total(self) -> str:
        """Get total amount from summary"""
        return self.get_text(self.TOTAL)

    def finish_checkout(self):
        """Complete the checkout process"""
        self.click_element(self.FINISH_BUTTON)

    def is_checkout_complete(self) -> bool:
        """Check if checkout is completed successfully"""
        return self.is_element_visible(self.COMPLETE_HEADER)

    def get_complete_message(self) -> str:
        """Get completion message"""
        return self.get_text(self.COMPLETE_HEADER)

    def back_to_home(self):
        """Return to products page"""
        self.click_element(self.BACK_HOME_BUTTON)

    def cancel_checkout(self):
        """Cancel checkout process"""
        self.click_element(self.CANCEL_BUTTON)

    def is_error_visible(self) -> bool:
        """Check if error message is visible (for missing info)"""
        return self.page.locator("[data-test='error']").is_visible()
