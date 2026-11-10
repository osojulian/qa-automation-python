def test_add_to_cart(inventory_page):
    #Add to Cart
    inventory_page.add_product_to_cart('sauce-labs-bike-light')

    assert int(inventory_page.get_cart_count()) == 1

def test_add_two_products_to_cart(inventory_page):
        
    #Add to Cart
    inventory_page.add_product_to_cart('sauce-labs-bike-light')

    inventory_page.add_product_to_cart('sauce-labs-bolt-t-shirt')

    assert int(inventory_page.get_cart_count()) == 2

    