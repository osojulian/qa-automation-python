import pytest
from pages.cart_page import CartPage

def test_name_products(inventory_page):

    # Add to Cart
    inventory_page.add_product_to_cart('sauce-labs-bike-light')
    
    inventory_page.add_product_to_cart('sauce-labs-bolt-t-shirt')

    # Go to Cart
    inventory_page.go_to_cart()

    cart_page = CartPage()

    cart_page.get_product_names()


    