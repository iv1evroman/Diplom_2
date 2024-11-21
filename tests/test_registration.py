from helpers import Helpers
import data
import allure


class TestRegistration:
    @allure.title('Проверка на успешное создание уникального пользователя')
    def test_unique_user_registration(self, profile_methods):
        email = Helpers.random_email(self)
        response = profile_methods.create_new_profile(email, data.PASSWORD, data.NAME)
        assert response[0] == 200 and 'accessToken' in response[1]
        r = profile_methods.login(email, data.PASSWORD)
        tok = r[1].get("accessToken")
        formatted_token = tok[7:]
        re = profile_methods.delete_profile(formatted_token)
        print(re[0])
        print(re[1])

    @allure.title('Проверка на создание уже существующего пользователя')
    def test_registration_of_existing_profile(self, profile_methods):
        email = Helpers.random_email(self)
        profile_methods.create_new_profile(email, data.PASSWORD, data.NAME)
        response = profile_methods.create_new_profile(email, data.PASSWORD, data.NAME)
        assert response[0] == 403 and {'success': False, 'message': 'User already exists'} == response[1]

    @allure.title('Проверка на создание пользователя без ввода email')
    def test_registration_without_email(self, profile_methods):
        response = profile_methods.create_new_profile('', data.PASSWORD, data.NAME)
        assert (response[0] == 403 and
                {'success': False, 'message': 'Email, password and name are required fields'} == response[1])
