import pytest
from selenium import webdriver

@pytest.fixture
def driver():

    # Open the browser
    driver = webdriver.Chrome()

    #Hand the driver to the test; teardown runs after it finishes
    yield driver

    #Teardown, Close the driver
    driver.quit()