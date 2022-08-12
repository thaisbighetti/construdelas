import pytest
from model_bakery import baker

from shop.models import Customer, Order, OrderDetail, Product
from shop.serializers import (
    CustomerSerializer,
    CustomerUpdateSerializer,
    OrderDetailSerializer,
    OrderSerializer,
    ProductSerializer,
)


@pytest.mark.django_db
class TestOrderSerializer:
    def test_order_serializer(self):
        order = baker.make(Order)
        serializer = OrderSerializer(order)
        expected_data = {
            "id": str(order.id),
            "value": order.value,
            "created_at": order.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "updated_at": order.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "customer": order.customer.id,
            "products": [],
        }
        assert serializer.data == expected_data


@pytest.mark.django_db
class TestOrderDetailSerializer:
    def test_order_detail_serializer(self):
        order_detail = baker.make(OrderDetail)
        serializer = OrderDetailSerializer(order_detail)
        expected_data = {
            "id": str(order_detail.id),
            "order": order_detail.order.id,
            "created_at": order_detail.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "updated_at": order_detail.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "status": order_detail.order.status,
            "products": {},
        }
        assert serializer.data == expected_data


@pytest.mark.django_db
class CustomerSerializer:
    def test_customer_serializer(self):
        customer = baker.make(Customer)
        serializer = CustomerSerializer(customer)
        expected_data = {
            "cpf": customer.cpf,
            "name": customer.name,
            "email": customer.email,
            "phone": customer.phone,
            "address": customer.address,
        }
        assert serializer.data == expected_data


@pytest.mark.django_db
class TestCustomerSerializer:
    def test_customer_update_serializer(self):
        customer = baker.make(Customer, name="Pessoa bem legal", address="Rua 1")
        expected_data = {
            "name": customer.name,
            "email": customer.email,
            "phone": "11999999999",
            "address": "Rua 2",
        }
        serializer = CustomerUpdateSerializer(data=expected_data)
        serializer.is_valid(True)
        assert serializer.data == expected_data


@pytest.mark.django_db
class TestProductSerializer:
    def test_product_serializer(self):
        product = baker.make(Product, value=10)
        expected_data = {
            "name": product.name,
            "description": product.description,
            "value": "10.00",
            "id": str(product.id),
            "created_at": product.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "updated_at": product.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        }
        serializer = ProductSerializer(product)
        assert serializer.data == expected_data
