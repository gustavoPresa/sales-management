from rest_framework import serializers

from provider.models import Client
from provider.models import Seller


class ClientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    phone_number = serializers.CharField()

    class Meta:
        fields = ('id', 'email', 'name', 'phone_number')
        model = Client


class SellerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    phone_number = serializers.CharField()

    class Meta:
        fields = ('id', 'email', 'name', 'phone_number')
        model = Seller
