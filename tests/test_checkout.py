import pytest

@pytest.mark.parametrize('first_name, last_name, postal_code, expected_message', [
        ('', 'Test', '55439', 'Error: First Name is required'),
        ('Test', '', '55439', 'Error: Last Name is required'),
        ('Test', 'Test', '', 'Error: Postal Code is required'),
    ], ids=['empty_first_name', 'empty_last_name', 'empty_postal_code'])
def test_checkout_with_empty_info(inventory_page, first_name, last_name, postal_code, expected_message):

    # Add to Cart
    inventory_page.add_product_to_cart('sauce-labs-bike-light')

    inventory_page.add_product_to_cart('sauce-labs-bolt-t-shirt')

    cart_page = inventory_page.go_to_cart()

    checkout_page = cart_page.go_to_checkout()

    checkout_page.fill_information(first_name, last_name, postal_code)

    checkout_page.click_continue()

    assert checkout_page.get_error_message() == expected_message

def test_checkout_with_valid_info(inventory_page):

    # Add to Cart
    inventory_page.add_product_to_cart('sauce-labs-bike-light')

    inventory_page.add_product_to_cart('sauce-labs-bolt-t-shirt')

    cart_page = inventory_page.go_to_cart()

    checkout_page = cart_page.go_to_checkout()

    checkout_page.fill_information('Julian', 'Osorio', '98342432')

    overview_page = checkout_page.click_continue()

    assert overview_page.get_product_names() == ['Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt']

    complete_page = overview_page.click_finish()

    assert complete_page.get_confirmation_message() == 'Thank you for your order!'
