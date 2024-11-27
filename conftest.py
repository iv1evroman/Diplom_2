import pytest
from methods.order_methods import OrderMethods
from methods.profile_methods import ProfileMethods


@pytest.fixture()
def order_methods():
    return OrderMethods()


@pytest.fixture()
def profile_methods():
    return ProfileMethods()