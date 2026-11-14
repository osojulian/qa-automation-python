from selenium.webdriver.common.by import By

class InventoryPage:

    # Locators
    BADGE_CART = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product):

        add_cart = (By.CSS_SELECTOR, f"[data-test='add-to-cart-{product}']")
        self.driver.find_element(*add_cart).click()

    def get_cart_count(self):

        badges = self.driver.find_elements(*self.BADGE_CART)

        if len(badges) == 0:

            return 0
        else:
            return int(badges[0].text)

    def remove_product_from_cart(self, product):
        remove_cart = (By.CSS_SELECTOR, f"[data-test='remove-{product}']")
        self.driver.find_element(*remove_cart).click()


    def go_to_cart(self):

        self.driver.find_element(*self.CART_LINK).click()



    
