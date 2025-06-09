import allure

from methods.order_methods import OrderMethods
from data import ORDER_PAYLOAD, WRONG_ORDER_PAYLOAD
from errors import OrderErrors

@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Проверка создания заказа, в запросе передан токен и ингредиенты')
    def test_create_order_with_token_and_ingredients(self, login_user):
        order = OrderMethods
        token = login_user
        status_code, response_context = order.create(ORDER_PAYLOAD, token)
        assert status_code == 200 and 'owner' in response_context.get('order')

    @allure.title('Проверка создания заказа, в запросе не передан токен, переданы ингредиенты')
    def test_create_order_no_token_with_ingredients(self):
        order = OrderMethods
        status_code, response_context = order.create(ORDER_PAYLOAD, '')
        assert status_code == 200 and 'order' in response_context

    @allure.title('Проверка создания заказа, в запросе передан токен, нет ингредиентов')
    def test_create_order_with_token_no_ingredients(self, login_user):
        order = OrderMethods
        token = login_user
        status_code, response_context = order.create('', token)
        assert status_code == 400 and response_context.get('message') == OrderErrors.no_ingredients

    @allure.title('Проверка создания заказа, в запросе передан токен и неверный хеш ингредиентов')
    def test_create_order_with_token_and_wrong_ingredients(self, login_user):
        order = OrderMethods
        token = login_user
        status_code, response_context = order.create(WRONG_ORDER_PAYLOAD, token)
        assert status_code == 400 and response_context.get('message') == OrderErrors.wrong_ingredient