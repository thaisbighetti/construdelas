from typing import Dict
from uuid import UUID, uuid4
from model_bakery import baker

import pytest
from django.test import Client

from shop.models import Customer, Product


@pytest.fixture
def client() -> Client:
    return Client()


@pytest.fixture
def payload() -> Dict:
    product_1 = baker.make(Product, value=10)
    product_2 = baker.make(Product, value=2)
    customer = baker.make(Customer)
    payload = {"customer": customer, "products": [product_1, product_2]}
    return payload
