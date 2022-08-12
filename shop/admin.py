from django.contrib import admin

from .forms import OrderDetailForm, OrderForm

from .models import Customer, Order, OrderDetail, Product


@admin.register(Customer)
class CustomerFilter(admin.ModelAdmin):
    readonly_fields = ["id"]
    list_display = ["id", "created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]
    list_per_page = 20


@admin.register(Order)
class OrderFilter(admin.ModelAdmin):
    ordering = ["-created_at"]
    readonly_fields = ["value", "status", "id"]
    list_display = ["id", "created_at", "status"]
    search_fields = ["id", "created_at", "status", "customer_id"]
    list_filter = ["created_at", "updated_at"]
    list_per_page = 20
    form = OrderForm


# FAZER FORM ADMIN


@admin.register(OrderDetail)
class OrderDetailFilter(admin.ModelAdmin):
    readonly_fields = ["id"]
    list_display = ["id", "order_id"]
    search_fields = ["id", "order_id", "products"]
    list_filter = ["created_at", "updated_at"]
    list_per_page = 20
    form = OrderDetailForm


@admin.register(Product)
class ProductFilter(admin.ModelAdmin):
    readonly_fields = ["id"]
    list_display = ["name"]
    list_filter = ["created_at", "updated_at"]
    list_per_page = 20
