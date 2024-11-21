import data
from helpers import Helpers
import allure
import requests
from data import BASE_URL, USER_URL

class TestProfileInfoChanges:
    @allure.title('Проверка на успешное изменение имени пользователя')
    def test_change_profile_name(self, profile_methods):
        r = profile_methods.create_user_and_get_token_and_email()
        new = {
            "email": r[1],
            "password": "123456",
            "name": "Роман"
        }
        print(r[0])
        print(r[1])
        response = requests.patch(f'{BASE_URL},{USER_URL}', headers={'Authorization': r[0]}, json=new)
        print(response.status_code)
        print(response.text)

