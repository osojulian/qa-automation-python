from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_add_to_cart(driver):

    #Open and login

    login_page = LoginPage(driver)
    
    login_page.open()
    
    login_page.login('standard_user', 'secret_sauce')

    inventory_page = InventoryPage(driver)

    #Add to Cart
    inventory_page.add_product_to_cart('sauce-labs-bike-light')

    assert int(inventory_page.get_cart_count()) == 1


    