from django.urls import path

from provider.api.views import ClientView
from provider.api.views import SellerView


urlpatterns = [
    path('client/', ClientView.as_view()),
    path('client/<str:client_id>/', ClientView.as_view()),
    path('seller/', SellerView.as_view()),
    path('seller/<str:seller_id>/', SellerView.as_view()),
]
