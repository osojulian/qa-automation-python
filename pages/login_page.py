from selenium.webdriver.common.by import By

class LoginPage:

    # Page URL and locators
    URL = 'https://www.saucedemo.com/'
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):

        # 1. Find the username field and type the username
        self.driver.find_element(*self.USERNAME).send_keys(username)

        # 2. Find the password field and type the password
        self.driver.find_element(*self.PASSWORD).send_keys(password)

        # 3. Find the login button and click
        self.driver.find_element(*self.LOGIN_BUTTON).click()

