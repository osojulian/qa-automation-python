from selenium.webdriver.common.by import By
from pages.cart_page import CartPage
from pages.base_page import BasePage


class InventoryPage(BasePage):

    # Locators
    BADGE_CART = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def add_product_to_cart(self, product):

        add_cart = (By.CSS_SELECTOR, f"[data-test='add-to-cart-{product}']")
        self.click(add_cart)

    def get_cart_count(self):

        badges = self.driver.find_elements(*self.BADGE_CART)

        if len(badges) == 0:

            return 0
        else:
            return int(badges[0].text)

    def remove_product_from_cart(self, product):
        remove_cart = (By.CSS_SELECTOR, f"[data-test='remove-{product}']")
        self.click(remove_cart)


    def go_to_cart(self):

        self.click(self.CART_LINK)
        return CartPage(self.driver)
