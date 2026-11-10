import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def driver():

    # Open the browser
    driver = webdriver.Chrome()

    # Hand the driver to the test; teardown runs after it finishes
    yield driver

    # Teardown, Close the driver
    driver.quit()

@pytest.fixture
def inventory_page(driver):

    login_page = LoginPage(driver)
    
    login_page.open()
    
    login_page.login('standard_user', 'secret_sauce')

    return InventoryPage(driver)