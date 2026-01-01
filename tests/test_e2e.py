import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import VALID_USERNAME, VALID_PASSWORD


class TestE2E:
    """E2E test cases for complete user journey"""

    @pytest.fixture(autouse=True)
    def setup_login(self, page):
        """Login before each test"""
        login_page = LoginPage(page)
        login_page.navigate_to_login()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        assert login_page.is_login_successful()

    def test_add_to_cart_and_checkout(self, page):
        """Positive: Complete purchase flow"""
        inventory_page = InventoryPage(page)
        cart_page = CartPage(page)
        checkout_page = CheckoutPage(page)

        # Verify inventory page loaded
        assert inventory_page.is_inventory_loaded()
        assert inventory_page.get_inventory_items_count() > 0

        # Add item to cart
        inventory_page.add_item_to_cart()
        assert inventory_page.is_cart_badge_visible()
        assert inventory_page.get_cart_badge_count() == "1"

        # Go to cart
        inventory_page.go_to_cart()
        assert cart_page.get_cart_items_count() == 1

        # Proceed to checkout
        cart_page.proceed_to_checkout()

        # Fill checkout information
        checkout_page.fill_checkout_info("John", "Doe", "12345")

        # Verify checkout summary (optional)
        assert checkout_page.get_item_total() != ""

        # Complete checkout
        checkout_page.finish_checkout()

        # Verify completion
        assert checkout_page.is_checkout_complete()
        assert "Thank you for your order" in checkout_page.get_complete_message()

    def test_remove_item_from_cart(self, page):
        """Positive: Add item and then remove from cart"""
        inventory_page = InventoryPage(page)
        cart_page = CartPage(page)

        # Add item to cart
        inventory_page.add_item_to_cart()
        assert inventory_page.get_cart_badge_count() == "1"

        # Go to cart
        inventory_page.go_to_cart()
        assert cart_page.get_cart_items_count() == 1

        # Remove item
        cart_page.remove_item()
        assert cart_page.is_cart_empty()

    def test_checkout_with_missing_info(self, page):
        """Negative: Attempt checkout with missing information"""
        inventory_page = InventoryPage(page)
        cart_page = CartPage(page)
        checkout_page = CheckoutPage(page)

        # Add item and go to checkout
        inventory_page.add_item_to_cart()
        inventory_page.go_to_cart()
        cart_page.proceed_to_checkout()

        # Try to continue without filling info
        checkout_page.click_element(checkout_page.CONTINUE_BUTTON)

        # Should show error
        assert checkout_page.is_error_visible()

    def test_continue_shopping_from_cart(self, page):
        """Positive: Continue shopping from cart"""
        inventory_page = InventoryPage(page)
        cart_page = CartPage(page)

        # Go to cart (empty)
        inventory_page.go_to_cart()
        assert cart_page.is_cart_empty()

        # Continue shopping
        cart_page.continue_shopping()

        # Should be back to inventory
        assert inventory_page.is_inventory_loaded()

    def test_sort_products(self, page):
        """Positive: Sort products by price"""
        inventory_page = InventoryPage(page)

        # Sort by price low to high
        inventory_page.sort_products("lohi")

        # Verify products are loaded (basic check)
        assert inventory_page.get_inventory_items_count() > 0
