import requests
from data import BASE_URL, ORDER_URL, REGISTER_URL
import allure


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
        response = requests.post(f'{BASE_URL}{ORDER_URL}', headers={'Authorization': f'{token}'}, data=payload)
        return response.status_code, response.json()

    @allure.step('получаем данные о заказах')
    def get_orders_with_authorization(self, token):
        response = requests.get(f'{BASE_URL}{ORDER_URL}', headers={'Authorization': f'{token}'})
        return response.status_code, response.json()

    @allure.step('создаем новый профиль и получаем токен')
    def get_token(self, email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(f'{BASE_URL}{REGISTER_URL}', data=payload)
        token = response.json().get("accessToken")
        return token
