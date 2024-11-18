import data
from helpers import Helpers


class TestGetOrders:
    def test_get_orders_without_authorization(self, profile_methods, order_methods):
        order_methods.create_order_with_authorization(data.INGREDIENTS)
        response = order_methods.get_orders()
        assert response[0] == 401
        print(response[0])
        print(response[1])

