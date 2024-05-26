import allure
import requests
from selene import browser, have

from tests.conftest import BASE_URL


class Cart:
    cookie_customer: str

    def open_cart(self, cookies_customer):
        with allure.step("Открытие корзины"):
            browser.open('/cart')
            return self

    def add_product(self, product_id):
        with allure.step(f'Добавляем товар {product_id} в корзину'):
            result = requests.post(url=f'{BASE_URL}/addproducttocart/catalog/{product_id}/1/1',
                                   cookies={'Nop.customer': self.cookie_customer})
            assert result.status_code == 200
            assert result.json()['success']

    def add_complex_product_from_detail_page(self):
        result = requests.post(url=f'{BASE_URL}/addproducttocart/details/72/1',
                               data={
                                   'product_attribute_72_5_18': 53,
                                   'product_attribute_72_6_19': 54,
                                   'product_attribute_72_3_20': 57,
                                   'addtocart_72.EnteredQuantity': 1
                               },
                               cookies={'Nop.customer': self.cookie_customer})
        assert result.status_code == 200
        assert result.json()['success']

    def cart_should_have_items(self, *product_names):
        browser.open('/')
        browser.driver.add_cookie({'name': 'Nop.customer', 'value': self.cookie_customer})
        browser.open('/cart')
        for index, product_name in enumerate(product_names):
            browser.element(f'table.cart>tbody>tr:nth-child({index+1})').element('.product-name').should(have.text(product_name[index]))


cart = Cart()
