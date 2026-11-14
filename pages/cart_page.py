from selenium.webdriver.common.by import By

class CartPage:

    # Locators
    NAME_PRODUCT = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")

    # Constructor
    def __init__(self, driver):
        self.driver = driver
    
    def get_product_names(self):

        products = self.driver.find_elements(*self.NAME_PRODUCT)

        product_names = []
        for product in products:
            product_names.append(product.text())

        return product_names