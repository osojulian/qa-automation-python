from selenium.webdriver.common.by import By

def test_login_logo_shows_swag_labs(driver):

    # Set the parameters for the tests
    URL = 'https://www.saucedemo.com/'

    # Go to the URL
    driver.get(URL)
    
    # Find the logo
    logo = driver.find_element(By.CLASS_NAME, "login_logo")

    # Verify the logo text
    assert "Swag Labs" in logo.text



