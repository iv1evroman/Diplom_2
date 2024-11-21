import requests
import data
from data import BASE_URL, ORDER_URL, PASSWORD, NAME, REGISTER_URL
import allure
from helpers import Helpers


class OrderMethods:
    @allure.step('создаем заказ без авторизации')
    def create_order_without_authorization(self, ingredients):
        payload = {
            "ingredients": ingredients
        }
        response = requests.post(f'{BASE_URL}{ORDER_URL}', data=payload)
        return response.status_code, response.json()

    @allure.step('создаем заказ c авторизацией')
    def create_order_with_authorization(self, ingredients, token):
        payload = {
            "ingredients": ingredients
        }
        response = requests.post(f'{BASE_URL}{ORDER_URL}', headers={'Authorization': token}, data=payload)
        return response.status_code, response.json()

    @allure.step('получаем данные о заказах')
    def get_orders_with_authorization(self, token):
        response = requests.get(f'{BASE_URL}, {ORDER_URL}', headers={'Authorization': token})
        return response.status_code, response.text

    def get_token(self, email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(f'{BASE_URL}{REGISTER_URL}', data=payload)
        tok = response.json().get("accessToken")
        token = str(tok[7:])
        return token
