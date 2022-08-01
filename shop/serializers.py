from rest_framework import serializers

from shop.support.utils import process_order

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

class OrderDetailSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="order.status")

    class Meta:
        model = OrderDetail
        fields = "__all__"


# fazer serializer update de pedidos
