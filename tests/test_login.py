import allure
import data
from helpers import Helpers


class TestLogin:
    @allure.title('Проверка на успешный вход зарегестрированного пользователя')
    def test_login_of_existing_user(self, profile_methods):
        response = profile_methods.login(data.EMAIL, data.PASSWORD)
        assert response[0] == 200 and 'accessToken' in response[1]

    @allure.title('Проверка на попытку входа с некорректным email')
    def test_login_with_incorrect_email(self, profile_methods):
        email = Helpers.random_email(self)
        response = profile_methods.login(email, data.PASSWORD)
        assert response[0] == 401 and {"success": False, "message": "email or password are incorrect"} == response[1]

    @allure.title('Проверка на попытку входа с некорректным паролем')
    def test_login_with_incorrect_password(self, profile_methods):
        response = profile_methods.login(data.EMAIL, '1234')
        assert response[0] == 401 and {"success": False, "message": "email or password are incorrect"} == response[1]
