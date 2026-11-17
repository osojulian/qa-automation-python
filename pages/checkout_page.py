from selenium.webdriver.common.by import By

class CheckoutPage:

    # locators
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    def fill_information(self, first_name, last_name, postal_code):

        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)

        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)

        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def click_continue(self):

        self.driver.find_element(*self.CONTINUE_BUTTON).click()
