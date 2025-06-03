import allure

from errors import UserErrors
from methods.order_methods import OrderMethods
from conftest import login_user

@allure.feature('Получение списка заказов')
class TestGetOrders:

    @allure.title('Проверка получения списка заказов, успешное получение списка заказов')
    def test_get_orders(self, login_user):
        order = OrderMethods
        token = login_user
        status_code, response_context = order.get_orders(token)
        assert status_code == 200 and 'orders' in response_context

    @allure.title('Проверка получения списка заказов, пользователь не авторизован, проверка текста ошибки')
    def test_get_orders_no_token(self):
        order = OrderMethods
        status_code, response_context = order.get_orders('')
        assert status_code == 401 and response_context.get('message') == UserErrors.not_authorised