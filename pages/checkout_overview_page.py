from selenium.webdriver.common.by import By
from pages.checkout_complete_page import CheckoutCompletePage


class CheckoutOverviewPage:

    # Locators
    NAME_PRODUCT = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    FINISH_BUTTON = (By.ID, 'finish')

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    def get_product_names(self):

        products = self.driver.find_elements(*self.NAME_PRODUCT)

        return [product.text for product in products]

    def click_finish(self):

        self.driver.find_element(*self.FINISH_BUTTON).click()
        return CheckoutCompletePage(self.driver)

