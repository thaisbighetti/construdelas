import uuid

from django.core.serializers.json import DjangoJSONEncoder
from django.db import models


class BaseModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, verbose_name="Id"
    )

    class Meta:
        abstract = True


class Customer(BaseModelMixin):
    name = models.CharField(max_length=50, verbose_name="Name", null=False, blank=False)
    cpf = models.CharField(
        max_length=14, verbose_name="Cpf", null=False, blank=False, unique=True
    )
    phone = models.CharField(
        max_length=13, verbose_name="Phone", null=False, blank=False
    )
    email = models.EmailField(verbose_name="Email", null=False, blank=False)
    address = models.CharField(
        max_length=255, verbose_name="Address", null=False, blank=False
    )


class Product(BaseModelMixin):
    name = models.CharField(max_length=50, verbose_name="Name", null=False, blank=False)
    description = models.CharField(
        max_length=50, verbose_name="Description", null=False, blank=False
    )
    value = models.DecimalField(
        verbose_name="Value", null=False, blank=False, decimal_places=2, max_digits=10
    )

    def __str__(self):
        return f"{self.name} | {self.value}"


class Order(BaseModelMixin):
    class Status(models.TextChoices):
        AWAYTING_PAYMENT = (
            "awayting_payment",
            "Awayting payment",
        )
        ORDER_PROCESSED = (
            "order_processed",
            "Order processed",
        )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        verbose_name="Customer Id",
        null=False,
        blank=False,
    )
    products = models.ManyToManyField(Product)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        verbose_name="Status",
        null=False,
        blank=False,
    )
    value = models.DecimalField(
        verbose_name="Value", null=True, decimal_places=2, max_digits=10
    )


class OrderDetail(BaseModelMixin):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="Order",
        null=False,
        blank=False,
    )
    products = models.JSONField(encoder=DjangoJSONEncoder)
