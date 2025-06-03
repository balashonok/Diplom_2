import requests

from data import BASE_URL, USER_URL, AUTH_URL, REGISTER_URL, LOGIN_URL

class UserMethods:

    @staticmethod
    def create(payload):
        response = requests.post(f'{BASE_URL}{AUTH_URL}{REGISTER_URL}', data=payload)
        return response.status_code, response.json()

    @staticmethod
    def login(payload):
        response = requests.post(f'{BASE_URL}{AUTH_URL}{LOGIN_URL}', data=payload)
        return response.status_code, response.json()

    @staticmethod
    def change(payload, token):
        response = requests.patch(f'{BASE_URL}{AUTH_URL}{USER_URL}', data=payload, headers={'Authorization':token})
        return response.status_code, response.json()

    @staticmethod
    def delete(token):
        response = requests.delete(f'{BASE_URL}{AUTH_URL}{USER_URL}', headers={'Authorization': token})
        return response.status_code, response.json()