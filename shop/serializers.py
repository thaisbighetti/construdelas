from django import forms
from rest_framework import serializers

from shop.support.utils import (perform_update, process_order,
                                remove_special_characters)

from .models import Customer, Order, OrderDetail, Product


class CustomerSerializer(serializers.ModelSerializer):
    cpf = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Customer
        fields = "__all__"

    def validate_cpf(self, data):
        return remove_special_characters(data)

    def validate_phone(self, data):
        return remove_special_characters(data)


class CustomerUpdateSerializer(serializers.ModelSerializer):
    class Meta(CustomerSerializer.Meta):
        fields = ["email", "name", "address", "phone"]

    def validate_phone(self, data):
        return remove_special_characters(data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    value = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        exclude = ["status"]

    def create(self, validated_data):
        order = process_order(validated_data)
        return order


class OrderDetailSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="order.status")

    class Meta:
        model = OrderDetail
        fields = ["id", "order", "created_at", "updated_at", "status", "products"]
