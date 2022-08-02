from rest_framework import serializers

from shop.support.utils import perform_update, process_order

from .models import Customer, Order, OrderDetail, Product


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "value"]


class OrderSerializer(serializers.ModelSerializer):
    value = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = ["customer_id", "products", "value"]

    def create(self, validated_data):
        order = process_order(validated_data)
        return order

    def update(self, instance, validated_data):
        return perform_update(instance, validated_data)


class OrderDetailSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="order.status")

    class Meta:
        model = OrderDetail
        fields = "__all__"
