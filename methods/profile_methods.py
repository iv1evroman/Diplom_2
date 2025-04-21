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
    def change_profile_data(self, token, email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.patch(f'{BASE_URL}{USER_URL}', headers={'Authorization': token}, data=payload)
        return response.status_code, response.json()

    @allure.step('удаляем профиль')
    def delete_profile(self, token):
        response = requests.delete(f'{BASE_URL}{USER_URL}', headers={'Authorization': token})
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
