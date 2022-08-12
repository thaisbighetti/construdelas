from decimal import Decimal
from model_bakery import baker

import pytest

from shop.models import Order, Product
from shop.support.utils import get_value, process_order, remove_special_characters


@pytest.mark.django_db
class TestProcessOrder:
    def test_should_process_order(self, payload):
        order = process_order(payload)
        assert order.value == Decimal("12.00")


class TestRemoveSpecialCharacters:
    def test_should_remove_special_characters(self):
        string1 = "111.222.333-00"
        string2 = "(11)9888888888"
        formated_string_1 = remove_special_characters(string1)
        formated_string_2 = remove_special_characters(string2)
        assert formated_string_1.isnumeric()
        assert formated_string_2.isnumeric()


@pytest.mark.django_db
class TestGetValue:
    def test_should_get_value_from_products(self):
        products = baker.make(Product, _quantity=2, value=10)
        order = baker.make(Order, products=products)
        value = get_value(order.products)
        assert value == Decimal("20.00")
