from .base_page import BasePage


class InventoryPage(BasePage):
    """Page object for SauceDemo inventory/products page"""

    # Locators
    INVENTORY_CONTAINER = ".inventory_list"
    INVENTORY_ITEM = ".inventory_item"
    ADD_TO_CART_BUTTON = "[data-test='add-to-cart-sauce-labs-backpack']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    SORT_DROPDOWN = "[data-test='product-sort-container']"

    def __init__(self, page):
        super().__init__(page)

    def is_inventory_loaded(self) -> bool:
        """Check if inventory page is loaded"""
        return self.is_element_visible(self.INVENTORY_CONTAINER)

    def get_inventory_items_count(self) -> int:
        """Get number of inventory items"""
        return len(self.page.query_selector_all(self.INVENTORY_ITEM))

    def add_item_to_cart(self, item_name: str = "sauce-labs-backpack"):
        """Add specific item to cart"""
        button_selector = f"[data-test='add-to-cart-{item_name}']"
        self.click_element(button_selector)

    def get_cart_badge_count(self) -> str:
        """Get cart badge count"""
        return self.get_text(self.CART_BADGE)

    def go_to_cart(self):
        """Navigate to cart page"""
        self.click_element(self.CART_LINK)

    def sort_products(self, sort_option: str):
        """Sort products by given option"""
        self.page.select_option(self.SORT_DROPDOWN, sort_option)

    def is_cart_badge_visible(self) -> bool:
        """Check if cart badge is visible"""
        return self.is_element_visible(self.CART_BADGE)
