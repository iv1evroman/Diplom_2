import data
from helpers import Helpers
import allure

class TestProfileInfoChanges:
    @allure.title('Проверка на успешное изменение имени пользователя')
    def test_change_profile_name(self, profile_methods):
        email = Helpers.random_email(self)
        r = profile_methods.create_new_profile(email, data.PASSWORD, data.NAME)
        print(r[0])
        print(r[1])
        tok = r[1].get("accessToken")
        formatted_token = tok[7:]
        print((formatted_token))
        new_data = {
            "name": "Дмитрий"
        }
        response = profile_methods.change_profile_data(f'{formatted_token}', new_data)
        print(response[0])
        print(response[1])

