import pytest
import allure

import data
from errors import UserErrors
from methods.user_methods import UserMethods

@allure.feature('Изменение данных пользователя')
class TestChangeUserData:

    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    @allure.title('Редактирование данных пользователя, при изменении поля {field}, получен статус 200 и новые данные')
    def test_change_user_data(self, create_new_user_and_delete, field):
        payload, token = create_new_user_and_delete
        payload[field] = payload[field][1:]
        user = UserMethods
        status_code, response_context = user.change(payload, token)
        payload.pop('password')
        assert status_code == 200 and response_context.get('user') == payload

    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    @allure.title('Редактирование данных пользователя без авторизации, при редактировании поля {field} получен статус 401 и текст ошибки')
    def test_change_user_data_no_token_get_error(self, field):
        user = UserMethods
        payload = data.USER_PAYLOAD
        status_code, response_context = user.change(payload, '')
        assert status_code == 401 and response_context.get('message') == UserErrors.not_authorised