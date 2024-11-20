import data
from helpers import Helpers


class TestGetOrders:
    def test_get_orders_with_authorization(self, profile_methods, order_methods):
        profile_methods.create_new_profile(data.EMAIL, data.PASSWORD, data.NAME)
        info = profile_methods.login(data.EMAIL, data.PASSWORD)
        tok = info[1].get("accessToken")

        response = order_methods.get_orders_with_authorization(tok)
        print(response[0])
        print(response[1])



    def test_get_orders_without_authorization(self, order_methods):
        order_methods.create_order_without_authorization(data.INGREDIENTS)
        response = order_methods.get_orders()
        assert response[0] == 200
