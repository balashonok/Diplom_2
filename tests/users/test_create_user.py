import pytest
import allure

import data
from methods.user_methods import UserMethods
from errors import UserErrors
from data_generator import generate_user_data

class TestCreateUser:

    @allure.title('Успешное создание пользователя, получен статус 200')
    def test_create_user(self):
        user = UserMethods
        payload = generate_user_data()
        status_code, response_context = user.create(payload)
        assert status_code == 200

    @allure.title('Создание пользователя с существующим логином, получена ошибка 403')
    def test_create_same_user(self):
        user = UserMethods
        status_code, response_context = user.create(data.USER_PAYLOAD)
        assert status_code == 403 and response_context.get('message') == UserErrors.already_exists

    @allure.title('Создание пользователя, в запросе пропущено обязательное поле')
    @pytest.mark.parametrize('missing_field', ['email', 'password', 'name'])
    def test_create_user_missing_field(self, missing_field):
        user = UserMethods
        payload = generate_user_data()
        payload.pop(missing_field)
        status_code, response_context = user.create(payload)
        assert status_code == 403 and response_context.get('message') == UserErrors.field_missed
