def test_checkout_with_valid_info(inventory_page):

    # Add to Cart
    inventory_page.add_product_to_cart('sauce-labs-bike-light')

    inventory_page.add_product_to_cart('sauce-labs-bolt-t-shirt')

    cart_page = inventory_page.go_to_cart()

    checkout_page = cart_page.go_to_checkout()

    checkout_page.fill_information('Julian', 'Osorio', '98342432')

    overview_page = checkout_page.click_continue()

    assert overview_page.get_product_names() == ['Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt']
