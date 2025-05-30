import pytest
import allure

import data
from errors import UserErrors
from methods.user_methods import UserMethods
from data_generator import generate_user_data

class TestChangeUserData:

    @allure.title('Редактирование данных пользователя, доступно изменить каждое поле, получен статус 200 и новые данные')
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_change_user_data(self, field):
        user = UserMethods
        payload = generate_user_data()
        _, response_context = user.create(payload)
        token = response_context.get('accessToken')
        payload[field] = payload[field][1:]
        status_code, response_context = user.change(payload, token)
        payload.pop('password')
        assert status_code == 200 and response_context.get('user') == payload

    @allure.title('Редактирование данных пользователя без авторизации, получен статус 401 и текст ошибки')
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_change_user_data_no_token_get_error(self, field):
        user = UserMethods
        payload = data.USER_PAYLOAD
        status_code, response_context = user.change(payload, '')
        assert status_code == 401 and response_context.get('message') == UserErrors.not_authorised