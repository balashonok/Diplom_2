import requests
import allure

from data import BASE_URL,ORDER_URL

class OrderMethods:

    @staticmethod
    @allure.step('Создать заказ')
    def create(payload, token):
        response = requests.post(f'{BASE_URL}{ORDER_URL}', data=payload, headers={'Authorization':token})
        return response.status_code, response.json()


    @staticmethod
    @allure.step('Получить список заказов')
    def get_orders(token):
        response = requests.get(f'{BASE_URL}{ORDER_URL}', headers={'Authorization': token})
        return response.status_code, response.json()