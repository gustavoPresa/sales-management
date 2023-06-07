from django.contrib import admin
from django.contrib.admin import ModelAdmin

from provider.models import Client
from provider.models import CommissionConfig
from provider.models import Product
from provider.models import Sale
from provider.models import Seller


@admin.register(Client)
class ClientAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email',)


@admin.register(Sale)
class SaleAdmin(ModelAdmin):
    list_display = (
        'invoice_number',
        'amount',
        'created_at',
        'client',
        'seller',
        'product'
    )
    search_fields = ('invoice_number', 'amount',)


@admin.register(Seller)
class SellerAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email',)


@admin.register(CommissionConfig)
class CommissionConfigAdmin(ModelAdmin):
    list_display = (
        'day',
        'min_commission_percentage',
        'max_commission_percentage'
    )

    search_fields = ('day',)


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = (
        'description',
        'product_code',
        'unitary_value',
        'commission_percentage'
    )

    search_fields = ('description', 'product_code',)
