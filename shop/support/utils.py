import re
from decimal import Decimal

from shop.models import Order, OrderDetail


def remove_special_characters(value: str) -> str:
    return re.sub(r"\D", "", value)


def get_value(products):
    value = []
    for product in products.all():
        value.append(product.value)
    return sum(value)


def process_order(data):
    order = Order.objects.create(
        customer_id=data["customer"].id, status=Order.Status.AWAYTING_PAYMENT
    )
    order.products.set(data["products"])
    order_detail_products = {"products": []}
    for product in data["products"]:
        order_detail_product = [str(product.id), product.name, product.value]
        order_detail_products["products"].append(order_detail_product)

    order.value = get_value(order.products)
    order.save()
    OrderDetail.objects.create(order_id=order.id, products=order_detail_products)

    return order
