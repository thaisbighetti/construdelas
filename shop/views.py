from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from shop.models import Customer, Order, OrderDetail, Product
from shop.serializers import (CustomerSerializer, OrderDetailSerializer,
                              OrderSerializer, ProductSerializer)


class CustomerViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    @action(detail=True, methods=["get"], url_path="/<pk>/")
    def get_customer(self, request, pk):
        queryset = get_object_or_404(Customer, id=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="list",permission_classes=[IsAdminUser] )
    def list_customers(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @action(detail=True, methods=["get"], url_path="/<pk>/", permission_classes=[IsAdminUser])
    def get_product(self, request, pk):
        queryset = get_object_or_404(Product, id=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="list")
    def list_products(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)


class OrdersViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    @action(detail=False, methods=["get"], url_path="list", permission_classes=[IsAdminUser])
    def list_orders(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get", "update"], url_path="<pk>")
    def get_order(self, request, pk):
        queryset = get_object_or_404(Product, id=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)


class OrdersDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()
    http_method_names = ["get"]

    @action(detail=True, methods=["get"], url_path="")
    def get_order_detail(self, request, pk):
        queryset = get_object_or_404(Product, id=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
