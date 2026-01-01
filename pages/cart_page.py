from .base_page import BasePage


class CartPage(BasePage):
    """Page object for SauceDemo cart page"""

    # Locators
    CART_ITEM = ".cart_item"
    CHECKOUT_BUTTON = "[data-test='checkout']"
    CONTINUE_SHOPPING_BUTTON = "[data-test='continue-shopping']"
    REMOVE_BUTTON = "[data-test='remove-sauce-labs-backpack']"
    CART_QUANTITY = ".cart_quantity"

    def __init__(self, page):
        super().__init__(page)

    def get_cart_items_count(self) -> int:
        """Get number of items in cart"""
        return len(self.page.query_selector_all(self.CART_ITEM))

    def proceed_to_checkout(self):
        """Click checkout button"""
        self.click_element(self.CHECKOUT_BUTTON)

    def continue_shopping(self):
        """Click continue shopping button"""
        self.click_element(self.CONTINUE_SHOPPING_BUTTON)

    def remove_item(self, item_name: str = "sauce-labs-backpack"):
        """Remove specific item from cart"""
        button_selector = f"[data-test='remove-{item_name}']"
        self.click_element(button_selector)

    def get_item_quantity(self) -> str:
        """Get quantity of first item in cart"""
        return self.get_text(self.CART_QUANTITY)

    def is_cart_empty(self) -> bool:
        """Check if cart is empty"""
        return self.get_cart_items_count() == 0
