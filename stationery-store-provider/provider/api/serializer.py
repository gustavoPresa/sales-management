from rest_framework import serializers

from provider.models import Client
from provider.models import Product
from provider.models import Seller


class ClientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)
    name = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=12)

    class Meta:
        fields = ('id', 'email', 'name', 'phone_number')
        model = Client


class ProductSerializer(serializers.ModelSerializer):
    product_code = serializers.CharField(max_length=50)
    unitary_value = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField(max_length=255)
    commission_percentage = serializers.IntegerField()

    class Meta:
        fields = (
            'id',
            'description',
            'product_code',
            'unitary_value',
            'commission_percentage'
        )

        model = Product


class SellerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)
    name = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=12)

    class Meta:
        fields = ('id', 'email', 'name', 'phone_number')
        model = Seller
