import data
from helpers import Helpers
import allure


class TestProfileInfoChanges:
    @allure.title('Проверка на успешное изменение имени пользователя c авторизацией')
    def test_change_profile_name_with_authorization(self, profile_methods):
        email = Helpers.random_email(self)
        token = profile_methods.get_token(email, data.PASSWORD, data.NAME)
        response = profile_methods.change_profile_data(token, email, data.PASSWORD, 'Василий')
        assert response[0] == 200 and "success" in response[1]
        profile_methods.delete_profile(token)

    @allure.title('Проверка на успешное изменение email пользователя c авторизацией')
    def test_change_profile_email_with_authorization(self, profile_methods):
        email = Helpers.random_email(self)
        token = profile_methods.get_token(email, data.PASSWORD, data.NAME)
        response = profile_methods.change_profile_data(token, data.EMAIL_TO_CHANGE, data.PASSWORD, data.NAME)
        assert (response[0] == 200 and
                {'success': True, 'user': {'email': 'emailtochange@mail.de', 'name': 'Рома123456'}} == response[1])
        profile_methods.delete_profile(token)

    @allure.title('Проверка на изменение email на уже существующий c авторизацией')
    def test_change_profile_email_to_existing_email_with_authorization(self, profile_methods):
        email = Helpers.random_email(self)
        token = profile_methods.get_token(email, data.PASSWORD, data.NAME)
        response = profile_methods.change_profile_data(token, data.EMAIL, data.PASSWORD, data.NAME)
        assert (response[0] == 403 and response[1] ==
                {"success": False, "message": "User with such email already exists"})
        profile_methods.delete_profile(token)

    @allure.title('Проверка на изменение email на уже существующий без авторизации')
    def test_change_profile_email_to_existing_email_without_authorization(self, profile_methods):
        email = Helpers.random_email(self)
        token = profile_methods.get_token(email, data.PASSWORD, data.NAME)
        response = profile_methods.change_profile_data('', data.EMAIL, data.PASSWORD, data.NAME)
        assert (response[0] == 401 and response[1] == {'message': 'You should be authorised', 'success': False})
        profile_methods.delete_profile(token)

    @allure.title('Проверка на изменение имени пользователя без авторизацией')
    def test_change_profile_name_without_authorization(self, profile_methods):
        email = Helpers.random_email(self)
        token = profile_methods.get_token(email, data.PASSWORD, data.NAME)
        response = profile_methods.change_profile_data('', email, data.PASSWORD, 'Василий')
        assert response[0] == 401 and response[1] == {'message': 'You should be authorised', 'success': False}
        profile_methods.delete_profile(token)

    @allure.title('Проверка на изменение email пользователя без авторизацией')
    def test_change_profile_email_without_authorization(self, profile_methods):
        email = Helpers.random_email(self)
        token = profile_methods.get_token(email, data.PASSWORD, data.NAME)
        response = profile_methods.change_profile_data('', data.EMAIL_TO_CHANGE, data.PASSWORD, data.NAME)
        assert response[0] == 401 and response[1] == {'message': 'You should be authorised', 'success': False}
        profile_methods.delete_profile(token)