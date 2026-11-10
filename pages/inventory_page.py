from selenium.webdriver.common.by import By

class InventoryPage:

    #Locators
    BADGE_CART = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")


    #Constructor
    def __init__(self, driver):
        self.driver = driver


    def add_product_to_cart(self, product):

        add_cart = (By.CSS_SELECTOR, f"[data-test='add-to-cart-sauce-{product}']")
        self.driver.find_element(*add_cart).click()

    def get_cart_count(self):

        return self.driver.find_element(*self.BADGE_CART).text
    
