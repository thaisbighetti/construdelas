from math import prod

import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from shop.models import Customer, Order, OrderDetail, Product


@pytest.mark.django_db
class TestCreateOrder:
    def test_should_create_order(self, client):
        customer = baker.make(Customer)
        product = baker.make(Product, value=10)

        create_order_view = reverse("order-list")
        payload = {"customer_id": customer.id, "products": [product.id]}
        response = client.post(
            create_order_view, payload, content_type="application/json"
        )
        order = Order.objects.first()
        order_detail = OrderDetail.objects.first()

        assert Order.objects.count() == 1
        assert response.status_code == status.HTTP_201_CREATED
        assert order.value == product.value
        assert order.products.get() == product
        assert order_detail.order == order
        assert order_detail.products == {
            "products": [[str(product.id), product.name, int(product.value)]]
        }
