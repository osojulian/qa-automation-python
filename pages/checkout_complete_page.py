from selenium.webdriver.common.by import By

class CheckoutCompletePage:

    # Locator
    HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    def get_confirmation_message(self):

        return self.driver.find_element(*self.HEADER).text
