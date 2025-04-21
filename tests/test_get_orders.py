import data
from helpers import Helpers
import allure


class TestGetOrders:
    @allure.title('проверка успешного получения заказов конкретного пользователя')
    def test_get_orders_with_authorization(self, profile_methods, order_methods):
        email = Helpers.random_email(self)
        token = order_methods.get_token(email, data.PASSWORD, data.NAME)
        order_methods.create_order_with_authorization(data.INGREDIENTS, token)
        response = order_methods.get_orders_with_authorization(token)
        assert response[0] == 200 and "success" in response[1]
        profile_methods.delete_profile(token)

    @allure.title('проверка что приходит ошибка на запрос получения заказов конкретного пользователя без авторизации')
    def test_get_orders_without_authorization(self, order_methods):
        response = order_methods.get_orders_with_authorization('')
        assert response[0] == 401 and response[1] == {'message': 'You should be authorised', 'success': False}
