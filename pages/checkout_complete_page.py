from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):

    # Locator
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def get_confirmation_message(self):

        return self.get_text(self.COMPLETE_HEADER)
