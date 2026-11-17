from selenium.webdriver.common.by import By

class CheckoutOverviewPage:

    # Locators
    NAME_PRODUCT = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    def get_product_names(self):

        products = self.driver.find_elements(*self.NAME_PRODUCT)

        return [product.text for product in products]

