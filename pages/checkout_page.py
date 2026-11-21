from selenium.webdriver.common.by import By
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    # locators
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def fill_information(self, first_name, last_name, postal_code):

        self.type(self.FIRST_NAME, first_name)

        self.type(self.LAST_NAME, last_name)

        self.type(self.POSTAL_CODE, postal_code)

    def get_error_message(self):

        return self.get_text(self.ERROR_MESSAGE)

    def click_continue(self):

        self.click(self.CONTINUE_BUTTON)

        return CheckoutOverviewPage(self.driver)
