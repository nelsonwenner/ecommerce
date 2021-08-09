from .serializers import PaymentMethodSerializer, PaymentGatewaySerializer
from .models import PaymentMethod, PaymentGateway
from rest_framework import permissions
from rest_framework import generics

class PaymentMethodList(generics.ListAPIView):
  name = 'payment-method-list'
  queryset = PaymentMethod.objects.get_queryset().order_by('id')
  serializer_class = PaymentMethodSerializer
  permission_classes = [permissions.IsAuthenticated]

class PaymentGatewayList(generics.ListAPIView):
  name = 'payment-gateway-list'
  queryset = PaymentGateway.objects.get_queryset().order_by('id')
  serializer_class = PaymentGatewaySerializer
  permission_classes = [permissions.IsAuthenticated]