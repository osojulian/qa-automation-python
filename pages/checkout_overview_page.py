from selenium.webdriver.common.by import By
from pages.checkout_complete_page import CheckoutCompletePage
from pages.base_page import BasePage

class CheckoutOverviewPage(BasePage):

    # Locators
    NAME_PRODUCT = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    FINISH_BUTTON = (By.ID, "finish")

    def get_product_names(self):

        products = self.driver.find_elements(*self.NAME_PRODUCT)

        return [product.text for product in products]

    def click_finish(self):

        self.click(self.FINISH_BUTTON)

        return CheckoutCompletePage(self.driver)

