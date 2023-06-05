from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from provider.api.serializer import ClientSerializer
from provider.api.serializer import SellerSerializer
from provider.models import Client
from provider.models import Seller


class ClientView(APIView):
    def delete(self, request, client_id: str) -> Response:
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        client.delete()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request, client_id: str) -> Response:
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(client)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        client_data = request.data

        if Client.objects.filter(email=client_data['email']):
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ClientSerializer(data=client_data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, client_id: str) -> Response:
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.update(client, serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class SellerView(APIView):
    def delete(self, request, seller_id: str) -> Response:
        try:
            seller = Seller.objects.get(id=seller_id)
        except Seller.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        seller.delete()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request, seller_id: str) -> Response:
        try:
            seller = Seller.objects.get(id=seller_id)
        except Seller.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = SellerSerializer(seller)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        seller_data = request.data

        if Seller.objects.filter(email=seller_data['email']):
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        serializer = SellerSerializer(data=seller_data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, seller_id: str) -> Response:
        try:
            seller = Seller.objects.get(id=seller_id)
        except Seller.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = SellerSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.update(seller, serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_200_OK)
