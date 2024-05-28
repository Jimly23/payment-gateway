from django.urls import path, include
from .views import orders, midtrans_notification

urlpatterns = [
    path('api/orders/', orders),
    path('midtrans-notification/', midtrans_notification),
]