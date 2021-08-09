from .api import PaymentMethodList, PaymentGatewayList
from django.urls import path

app_name = 'payment_gateway'

urlpatterns = [
  path('gateways', PaymentGatewayList.as_view(), name=PaymentGatewayList.name),
  path('methods', PaymentMethodList.as_view(), name=PaymentMethodList.name),
]