import pytest
import allure

from methods.user_methods import UserMethods
from data import USER_PAYLOAD
from errors import UserErrors

class TestUserLogin():

    @allure.title('Успешная авторизация пользователя, получен статус 200')
    def test_user_login(self):
        user = UserMethods
        payload = USER_PAYLOAD
        payload.pop('name')
        status_code, response_context = user.login(payload)
        assert status_code == 200

    @allure.title('Авторизация пользователя, в одном из полей ошибка, получен статус 401')
    @pytest.mark.parametrize('wrong_field', ['email', 'password'])
    def test_user_login_wrong_field(self, wrong_field):
        user = UserMethods
        payload = USER_PAYLOAD.copy()
        payload.pop('name')
        payload[wrong_field] = payload[wrong_field][1:]
        status_code, response_context = user.login(payload)
        assert status_code == 401 and response_context['message'] == UserErrors.field_is_incorrect