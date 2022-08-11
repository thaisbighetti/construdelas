from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter

from shop.models import Customer, Order, OrderDetail, Product
from shop.serializers import (
    CustomerSerializer,
    CustomerUpdateSerializer,
    OrderDetailSerializer,
    OrderSerializer,
    ProductSerializer,
)


class CustomerViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):

    serializers = {
        "list": CustomerSerializer,
        "create": CustomerSerializer,
        "partial_update": CustomerUpdateSerializer,
        "retrieve": CustomerSerializer,
    }
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        return self.serializers[self.action]


class ProductViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrdersViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrdersDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()
    http_method_names = ["get"]
    filter_backends = [SearchFilter]
    search_fields = ["order__id", "order__customer_id__id", "products__id"]
