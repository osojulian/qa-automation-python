import pytest
from pages.login_page import LoginPage

def test_login_successful(driver):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login('standard_user', 'secret_sauce')

    assert 'inventory.html' in driver.current_url

# Define the arguments and Dataset as a list of tuples
@pytest.mark.parametrize('username, password, expected_message', [
    ('locked_out_user', 'secret_sauce', 'Epic sadface: Sorry, this user has been locked out.'),
    ('standard_user', 'Any word', 'Epic sadface: Username and password do not match any user in this service'),
    ('', 'secret_sauce', 'Epic sadface: Username is required'),

], ids=['locked_user', 'wrong_password', 'empty_username'])

def test_login_invalid(driver, username, password, expected_message):   

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(username, password)

    assert login_page.get_error_message() == expected_message
