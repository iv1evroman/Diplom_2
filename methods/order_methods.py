import requests
from data import BASE_URL, ORDER_URL


class OrderMethods:
    def create_order(self, ingredients):
        payload = {
            "ingredients": ingredients
        }
        response = requests.post(f'{BASE_URL}{ORDER_URL}', data=payload)
        return response.status_code, response.json()