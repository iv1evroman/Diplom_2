import allure
import data
import requests
from data import BASE_URL, ORDER_URL, REGISTER_URL
from helpers import Helpers


class TestCreateOrder:
    @allure.title('Проверка на создание заказа без авторизации')
    def test_create_order_without_authorization(self, order_methods):
        response = order_methods.create_order_without_authorization(data.INGREDIENTS)
        assert response[0] == 200 and "success" in response[1]

    @allure.title('Проверка на создание заказа c авторизацией')
    def test_create_order_with_authorization(self, order_methods):
        response = order_methods.create_order_with_authorization(data.INGREDIENTS)
        assert response[0] == 200 and "success" in response[1]

    @allure.title('Проверка на создание заказа без авторизации и без ингредиентов')
    def test_test_create_order_without_authorization_and_without_ingredients(self, order_methods):
        response = order_methods.create_order_without_authorization('')
        assert response[0] == 400 and {"success": False, "message": "Ingredient ids must be provided"} == response[1]

    @allure.title('Проверка на создание заказа c авторизацией и без ингредиентов')
    def test_test_create_order_with_authorization_and_without_ingredients(self, order_methods):
        response = order_methods.create_order_with_authorization('')
        assert response[0] == 400 and {"success": False, "message": "Ingredient ids must be provided"} == response[1]

    @allure.title('Проверка на создание заказа без авторизации и c неверным хэшем ингредиентов')
    def test_test_create_order_without_authorization_and_with_incorrect_ingredients(self, order_methods):
        payload = {
            "ingredients": data.INCORRECT_INGREDIENTS
        }
        response = requests.post(f'{BASE_URL}{ORDER_URL}', data=payload)
        assert response.status_code == 500

    @allure.title('Проверка на создание заказа c авторизацией и c неверным хэшем ингредиентов')
    def test_test_create_order_with_authorization_and_with_incorrect_ingredients(self, order_methods):
        payload_for_token = {
            "email": Helpers.random_email(self),
            "password": data.PASSWORD,
            "name": data.NAME
        }
        response = requests.post(f'{BASE_URL}{REGISTER_URL}', data=payload_for_token)
        tok = response.json().get("accessToken")
        formatted_token = tok[7:]
        payload = {
            "ingredients": data.INCORRECT_INGREDIENTS
        }
        response = requests.post(f'{BASE_URL}{ORDER_URL}', headers={'Authorization': formatted_token}, data=payload)
        assert response.status_code == 500