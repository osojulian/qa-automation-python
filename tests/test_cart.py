from pages.cart_page import CartPage

def test_name_products(inventory_page, driver):

    # Add to Cart
    inventory_page.add_product_to_cart('sauce-labs-bike-light')
    
    inventory_page.add_product_to_cart('sauce-labs-bolt-t-shirt')

    # Go to Cart
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)

    expected_names = cart_page.get_product_names()

    actual_names = ['Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt']

    assert actual_names == expected_names


    