from django.urls import path

from provider.api.views import ClientView


urlpatterns = [
    path('client/', ClientView.as_view()),
    path('client/<str:client_id>/', ClientView.as_view()),
]
