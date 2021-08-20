from .serializers import CustomUserSerializer, TokenObtainPairSerializer, AddressSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from .permissions import IsUserOwner
from rest_framework import generics
from .models import Customer, Address

class TokenObtainPairView(TokenObtainPairView):
  serializer_class = TokenObtainPairSerializer

class UserCreateView(generics.CreateAPIView):
  name = "user-create"
  permission_classes = [permissions.AllowAny]
  queryset = Customer.objects.get_queryset()
  serializer_class = CustomUserSerializer

class UserDetail(generics.RetrieveUpdateAPIView):
  name = "user-detail-update"
  permission_classes = [permissions.IsAuthenticated, IsUserOwner]
  queryset = Customer.objects.get_queryset()
  serializer_class = CustomUserSerializer

class AddressCreateView(generics.CreateAPIView):
  name = "address-create"
  permission_classes = [permissions.IsAuthenticated]
  queryset = Address.objects.get_queryset()
  serializer_class = AddressSerializer