import requests

import data
from data import BASE_URL, REGISTER_URL, LOGIN_URL, USER_URL
import allure
from helpers import Helpers

class ProfileMethods:
    @allure.step('создаем новый профиль')
    def create_new_profile(self, email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(f'{BASE_URL}{REGISTER_URL}', data=payload)
        return response.status_code, response.json()

    @allure.step('авторизуем пользователя')
    def login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(f'{BASE_URL}{LOGIN_URL}', data=payload)
        return response.status_code, response.json()

    @allure.step('изменяем данные пользователя')
    def change_profile_data(self, token, new_data):
        response = requests.patch(f'{BASE_URL}{USER_URL}', headers={'Authorization': token}, data=new_data)
        return response.status_code, response.json()

    @allure.step('удаляем профиль')
    def delete_profile(self, token):
        response = requests.delete(f'{BASE_URL}{USER_URL}', headers={'Authorization': token})
        return response.status_code, response.json()

    def create_user_and_get_token_and_email(self):
        payload = {
            "email": Helpers.random_email(self),
            "password": data.PASSWORD,
            "name": data.NAME
        }
        response = requests.post(f'{BASE_URL}{REGISTER_URL}', data=payload)
        tok = response.json().get("accessToken")
        formatted_token = str(tok[7:])
        payload1 = {
            "email": Helpers.random_email(self),
            "password": data.PASSWORD
        }
        requests.post(f'{BASE_URL}{LOGIN_URL}', data=payload1)
        return formatted_token, payload1.get("email")
