import allure
from models.cart_page import cart


def test_cart_should_have_item(cookie_customer):
    with allure.step('Устанавливаем cookie посетителя в корзину'):
        cart.cookie_customer = cookie_customer

    with allure.step('Добавляем товары в корзину'):
        cart.add_product(31)

    with allure.step('Открытие корзины с товарами'):
        cart.cart_should_have_items('14.1-inch Laptop')


def test_cart_should_have_many_items(cookie_customer):
    with allure.step('Устанавливаем cookie посетителя в корзину'):
        cart.cookie_customer = cookie_customer

    with allure.step('Добавляем товары в корзину'):
        cart.add_product(31)
        cart.add_product(13)

    with allure.step('Открытие корзины с товарами'):
        cart.cart_should_have_items('14.1-inch Laptop', 'Computing and Internet')


def test_cart_should_have_complex_item_from_item_page(cookie_customer):
    with allure.step('Устанавливаем cookie посетителя в корзину'):
        cart.cookie_customer = cookie_customer

    with allure.step('Добавляем сложный товар с параметрами в корзину'):
        cart.add_complex_product_from_detail_page()

    with allure.step('Открытие корзины с товарами'):
        cart.cart_should_have_items('Build your own cheap computer')