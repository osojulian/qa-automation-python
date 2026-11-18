from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    # Page URL and locators
    URL = 'https://www.saucedemo.com/'
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):

        # 1. Find the username field and type the username
        self.type(self.USERNAME, username)

        # 2. Find the password field and type the password
        self.type(self.PASSWORD, password)

        # 3. Find the login button and click
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):

        return self.get_text(self.ERROR_MESSAGE)

