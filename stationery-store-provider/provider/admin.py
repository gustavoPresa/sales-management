from django.contrib import admin
from django.contrib.admin import ModelAdmin

from provider.models import Client
from provider.models import Seller


@admin.register(Client)
class ClientAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email',)


@admin.register(Seller)
class SellerAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email',)
