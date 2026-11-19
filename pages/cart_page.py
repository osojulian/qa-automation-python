from selenium.webdriver.common.by import By
from pages.checkout_page import CheckoutPage
from pages.base_page import BasePage

class CartPage(BasePage):

    # Locators
    NAME_PRODUCT = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")

    def get_product_names(self):

        products = self.driver.find_elements(*self.NAME_PRODUCT)

        return [product.text for product in products]

    def go_to_checkout(self):

        self.click(self.CHECKOUT_BUTTON)

        return CheckoutPage(self.driver)
