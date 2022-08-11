from decimal import Decimal
from uuid import uuid4

import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from shop.models import Customer, Order, OrderDetail, Product

content_type = "application/json"


@pytest.mark.django_db
class TestCreateOrder:
    def test_should_create_order(self, client):
        customer = baker.make(Customer)
        product = baker.make(Product, value=10)
        create_order_view = reverse("order-list")
        payload = {"customer": customer.pk, "products": [product.id]}

        response = client.post(create_order_view, payload, content_type=content_type)

        order = Order.objects.first()
        order_detail = OrderDetail.objects.first()

        assert Order.objects.count() == 1
        assert response.status_code == status.HTTP_201_CREATED
        assert order.value == product.value
        assert order.products.get() == product
        assert order_detail.order == order
        assert order_detail.products == {
            "products": [[str(product.id), product.name, "10.00"]]
        }

    def test_should_not_create_order_when_customer_does_not_exist(self, client):
        product = baker.make(Product, value=10)
        create_order_view = reverse("order-list")
        payload = {"customer": uuid4(), "products": [product.id]}

        response = client.post(create_order_view, payload, content_type=content_type)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Order.objects.count() == 0
        assert OrderDetail.objects.count() == 0

    def test_should_not_create_order_when_product_does_not_exist(self, client):
        customer = baker.make(Customer)
        create_order_view = reverse("order-list")
        payload = {"customer": customer.id, "products": uuid4()}

        response = client.post(create_order_view, payload, content_type=content_type)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Order.objects.count() == 0
        assert OrderDetail.objects.count() == 0


@pytest.mark.django_db
class TestCreateCustomer:
    def test_should_create_customer(self, client):
        create_customer_view = reverse("customer-list")
        payload = {
            "cpf": "647.658.780-31",
            "name": "Alírio",
            "email": "alirio@hotmail.com",
            "phone": "(11)958361293",
            "address": "Rua 1, do lado da rua 2",
        }
        response = client.post(create_customer_view, payload, content_type=content_type)
        assert Customer.objects.count() == 1
        assert response.status_code == status.HTTP_201_CREATED

    def test_should_not_create_customer_when_required_field_is_missing(self, client):
        create_customer_view = reverse("customer-list")
        payload = {
            "cpf": "647.658.780-31",
            "name": None,
            "email": "alirio@hotmail.com",
            "phone": None,
            "address": "Rua 1, do lado da rua 2",
        }
        response = client.post(create_customer_view, payload, content_type=content_type)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
