import requests

from data import BASE_URL,ORDER_URL

class OrderMethods:

    @staticmethod
    def create(payload, token):
        response = requests.post(f'{BASE_URL}{ORDER_URL}', data=payload, headers={'Authorization':token})
        return response.status_code, response.json()

    @staticmethod
    def get_orders(token):
        response = requests.get(f'{BASE_URL}{ORDER_URL}', headers={'Authorization': token})
        return response.status_code, response.json()