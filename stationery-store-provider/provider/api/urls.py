from django.urls import path

from provider.api.views import ClientView
from provider.api.views import CommissionReportView
from provider.api.views import ProductView
from provider.api.views import SaleView
from provider.api.views import SellerView


urlpatterns = [
    path('client/', ClientView.as_view()),
    path('client/<str:client_id>/', ClientView.as_view()),
    path(
        'commission_report/<str:from_date>/<str:to_date>/',
        CommissionReportView.as_view()
    ),
    path('product/', ProductView.as_view()),
    path('product/<str:product_id>/', ProductView.as_view()),
    path('sale/', SaleView.as_view()),
    path('sale/<str:sale_id>/', SaleView.as_view()),
    path('seller/', SellerView.as_view()),
    path('seller/<str:seller_id>/', SellerView.as_view()),
]
