import requests
from data import BASE_URL, REGISTER_URL, LOGIN_URL, USER_URL


class ProfileMethods:
    def create_new_profile(self, email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(f'{BASE_URL}{REGISTER_URL}', data=payload)
        return response.status_code, response.json()

    def login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(f'{BASE_URL}{LOGIN_URL}', data=payload)
        return response.status_code, response.json()

    def change_profile_data(self, token, new_data):
        response = requests.patch(f'{BASE_URL}{USER_URL}',
                                  headers={'Authorization': token},
                                  data=new_data)
        return response.status_code, response.json()

    def delete_profile(self, token):
        response = requests.delete(f'{BASE_URL}{USER_URL}', headers={'Authorization': token})
        return response.status_code, response.json()