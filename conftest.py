import pytest
from methods.user_methods import UserMethods
from data_generator import generate_user_data
from data import USER_PAYLOAD

@pytest.fixture
def create_new_user_and_delete():
    user = UserMethods
    payload = generate_user_data()
    _, response_context = user.create(payload)
    token = response_context.get('accessToken')
    yield payload, token
    user.delete(token)

@pytest.fixture()
def login_user():
    user = UserMethods
    payload = USER_PAYLOAD.copy()
    payload.pop('name')
    _, response_context = user.login(payload)
    token = response_context.get('accessToken')
    yield token
