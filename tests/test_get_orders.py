import data
from helpers import Helpers


class TestGetOrders:
    def test_get_orders_with_authorization(self, profile_methods, order_methods):
        token = order_methods.get_token(Helpers.random_email(self), data.PASSWORD, data.NAME)
        r = order_methods.create_order_with_authorization(data.INGREDIENTS, token)
        re = order_methods.get_orders_with_authorization(token)
        print(re[0])
        print(re[1])



    def test_get_orders_without_authorization(self, order_methods):
        order_methods.create_order_without_authorization(data.INGREDIENTS)
        response = order_methods.get_orders()
        assert response[0] == 400
