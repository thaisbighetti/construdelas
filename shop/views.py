from crypt import methods

from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from shop.models import Customer, Order, OrderDetail, Product
from shop.serializers import CustomerSerializer, OrderDetailSerializer, OrderSerializer, ProductSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    @action(detail=False, methods=["post"], url_path="create")
    def create_customer(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

    @action(detail=True, methods=["get"], url_path="/<pk>/")
    def get_customer(self, request, pk):
        queryset = get_object_or_404(Customer, id=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="list")
    def list_customers(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @action(detail=False, methods=["post"], url_path="create")
    def create_product(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

    @action(detail=True, methods=["get"], url_path="/<pk>/")
    def get_product(self, request, pk):
        queryset = get_object_or_404(Product, id=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="list")
    def list_products(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)


class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    http_method_names = ["get", "post", "delete"]

    @action(detail=False, methods=["post"], url_path="create")
    def create_order(self, request):
        serializer = self.serializer_class(data=request.data)
        print(request.data)
        if serializer.is_valid(True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

    @action(detail=True, methods=["get"], url_path="")
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
