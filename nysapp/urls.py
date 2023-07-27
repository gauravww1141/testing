from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('payment-failed', views.Failed.as_view(), name='payment-failed'),
    path('payment-success', views.Success.as_view(), name='payment-success'),
]