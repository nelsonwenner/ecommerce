from .serializers import OrderSerializer, OrderDetailSerializer
from rest_framework.response import Response
from .permissions import IsOrderOwner
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from .models import Order

class OrderCreateList(generics.ListCreateAPIView):
  name = 'order-create-list'
  permission_classes = [permissions.IsAuthenticated]
  queryset = Order.objects.get_queryset()
  serializer_class = OrderSerializer

  def list(self, request, *args, **kwargs):
    current_user = request.user
    orders = Order.objects.filter(is_active=True, customer=current_user.id).order_by('created_at')
    serializer_order = OrderDetailSerializer(orders, many=True)
    return Response(serializer_order.data, status=status.HTTP_200_OK)

class OrderDetail(generics.RetrieveAPIView):
  name = 'order-detail'
  queryset = Order.objects.get_queryset().filter(is_active=True)
  serializer_class = OrderDetailSerializer
  permission_classes = [permissions.IsAuthenticated, IsOrderOwner]