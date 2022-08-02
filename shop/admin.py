from django.contrib import admin

from .models import Customer, Order, OrderDetail, Product


@admin.register(Customer)
class CustomerFilter(admin.ModelAdmin):
    readonly_fields = ["id"]
    list_display = ["id", "created_at", "updated_at"]


@admin.register(Order)
class OrderFilter(admin.ModelAdmin):
    ordering = ["-created_at"]
    readonly_fields = ["value", "status", "id"]
    list_display = ["id", "created_at", "updated_at", "status"]
    search_fields = ["id", "created_at", "status", "customer_id"]


@admin.register(OrderDetail)
class OrderDetailFilter(admin.ModelAdmin):
    readonly_fields = ["id"]
    list_display = ["id", "created_at", "updated_at"]


@admin.register(Product)
class ProductFilter(admin.ModelAdmin):
    readonly_fields = ["id"]
    list_display = ["name", "created_at", "updated_at"]
