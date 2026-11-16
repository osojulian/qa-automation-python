from selenium.webdriver.common.by import By
from pages.checkout_page import CheckoutPage

class CartPage:

    # Locators
    NAME_PRODUCT = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    CHECKOUT_PRODUCT = (By.CSS_SELECTOR, "[data-test='secret_sauce']")

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    def get_product_names(self):

        products = self.driver.find_elements(*self.NAME_PRODUCT)

        return [product.text for product in products]

    def go_to_checkout(self):
        self.driver.find_element(*self.CHECKOUT_PRODUCT).click
        return CheckoutPage(self.driver)
