from rest_framework import serializers

from provider.models import Client
from provider.models import Product
from provider.models import Sale
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


class SaleSerializer(serializers.ModelSerializer):
    invoice_number = serializers.IntegerField()
    amount = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    client = ClientSerializer()
    seller = SellerSerializer()
    product = ProductSerializer()

    def create(self, validated_data):
        client_data = validated_data.pop('client')
        seller_data = validated_data.pop('seller')
        product_data = validated_data.pop('product')

        client_obj = Client.objects.get(email=client_data['email'])
        seller_obj = Seller.objects.get(email=seller_data['email'])
        product_obj = Product.objects.get(
            product_code=product_data['product_code']
        )

        sale = Sale.objects.create(
            **validated_data,
            client=client_obj,
            seller=seller_obj,
            product=product_obj,
        )

        return sale

    def update(self, sale, validated_data):
        client_data = validated_data['client']
        seller_data = validated_data['seller']
        product_data = validated_data['product']

        client_obj = Client.objects.get(email=client_data['email'])
        seller_obj = Seller.objects.get(email=seller_data['email'])
        product_obj = Product.objects.get(
            product_code=product_data['product_code']
        )

        Sale.objects.filter(
            invoice_number=validated_data['invoice_number']
        ).update(
            amount=validated_data['amount'],
            created_at=validated_data['created_at'],
            client=client_obj,
            seller=seller_obj,
            product=product_obj,
        )

        return sale

    class Meta:
        fields = (
            'id',
            'invoice_number',
            'amount',
            'created_at',
            'client',
            'seller',
            'product',
        )

        model = Sale
