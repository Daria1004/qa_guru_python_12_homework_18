from pages.cart_page import cart


def test_cart_should_have_item(cookie_customer):
    cart.set_customer(cookie_customer)
    cart.add_product(31)
    cart.cart_should_have_items('14.1-inch Laptop')


def test_cart_should_have_many_items(cookie_customer):
    cart.set_customer(cookie_customer)
    cart.add_product(31)
    cart.add_product(13)
    cart.cart_should_have_items('14.1-inch Laptop', 'Computing and Internet')


def test_cart_should_have_complex_item_from_item_page(cookie_customer):
    cart.set_customer(cookie_customer)
    cart.add_complex_product_from_detail_page()
    cart.cart_should_have_items('Build your own cheap computer')
