from payment.views import TestView
from django.urls import path

urlpatterns = [
    path('payme/endpoint/', TestView.as_view(), name='payme'),
]
