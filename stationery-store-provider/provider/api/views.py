from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from provider.api.serializer import ClientSerializer
from provider.api.serializer import ProductSerializer
from provider.api.serializer import SaleSerializer
from provider.api.serializer import SellerSerializer
from provider.models import Client
from provider.models import Product
from provider.models import Sale
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


class CommissionReportView(APIView):
    def get(self, request, from_date: str, to_date: str) -> Response:
        from_date = datetime.strptime(from_date, '%d-%m-%Y')
        to_date = datetime.strptime(to_date, '%d-%m-%Y')

        try:
            sallers_list, total_commissions = (
                Product.get_commission_report(from_date, to_date)
            )
        except Exception:
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'data': sallers_list, 'total': total_commissions})


class ProductView(APIView):
    def delete(self, request, product_id: str) -> Response:
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        product.delete()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request, product_id: str) -> Response:
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        product_data = request.data

        if Product.objects.filter(product_code=product_data['product_code']):
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductSerializer(data=product_data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, product_id: str) -> Response:
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.update(product, serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class SaleView(APIView):
    def delete(self, request, sale_id: str) -> Response:
        try:
            sale = Sale.objects.get(id=sale_id)
        except Sale.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        sale.delete()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request, sale_id: str) -> Response:
        try:
            sale = Sale.objects.get(id=sale_id)
        except Sale.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = SaleSerializer(sale)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        sale_data = request.data

        if Sale.objects.filter(
            invoice_number=sale_data['invoice_number']
        ).exists():
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        if not Client.objects.filter(
            email=sale_data['client']['email']
        ).exists():
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        if not Product.objects.filter(
            product_code=sale_data['product']['product_code']
        ).exists():
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        serializer = SaleSerializer(data=sale_data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, sale_id: str) -> Response:
        try:
            sale = Sale.objects.get(id=sale_id)
        except Sale.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = SaleSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.update(sale, serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class SalesView(APIView):
    def get(self, request) -> Response:
        try:
            sales = Sale.objects.all()
        except Sale.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = SaleSerializer(sales, many=True)

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
