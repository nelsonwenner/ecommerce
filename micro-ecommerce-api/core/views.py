from rest_framework_simplejwt.views import TokenObtainPairView
from payment_gateway.models import PaymentGateway
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.reverse import reverse
from payment_gateway.serializers import *
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.generics import *
from rest_framework import status
from .permissions import *
from .serializers import *
from .models import *

class ApiRoot(APIView):
    name = 'api-root'
    
    def get(self, request, *args, **kwargs):

        data = {
            "clients": reverse(ClientListView.name, request=request),
            "address": reverse(AddressListView.name, request=request),
            "status": reverse(StatusListView.name, request=request),
            "categories": reverse(CategoryListView.name, request=request),
            "products": reverse(ProductListView.name, request=request),
            "checkouts": reverse(CheckoutListView.name, request=request),
            "checkoutitems": reverse(CheckoutItemListView.name, request=request),
            "paymentmethods": reverse(PaymentMethodListView.name, request=request),
            "paymentgateways": reverse(PaymentGatewayListView.name, request=request),
        }
        
        return Response(data, status=status.HTTP_200_OK)


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

class ClientListView(CreateAPIView):
    name = "client-list"
    queryset = Customer.objects.get_queryset()
    serializer_class = ClientSerializer

class ClientDetail(RetrieveUpdateAPIView):
    name = "client-detail"
    queryset = Customer.objects.get_queryset()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, IsClientOwner]

class AddressListView(ListCreateAPIView):
    name = 'address-list-view'
    queryset = Address.objects.get_queryset()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        current_user = request.user
        address = Address.objects.filter(customer=current_user.id)
        address_serializer = AddressSerializer(address, many=True)
        return Response(address_serializer.data, status=status.HTTP_200_OK)

class AddressDetail(RetrieveUpdateDestroyAPIView):
    name = 'address-detail'
    queryset = Address.objects.get_queryset()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated, IsAddressOwnerDetail]

class StatusListView(ListAPIView):
    name = 'status-list-view'
    queryset = Status.objects.get_queryset()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated, ReadOnlyPermission]

class StatusDetail(RetrieveAPIView):
    name = 'status-detail'
    queryset = Status.objects.get_queryset()
    serializer_class = StatusDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CategoryListView(ListAPIView):
    name = 'category-list-view'
    queryset = Category.objects.get_queryset()
    serializer_class = CategorySerializer

class CategoryDetail(RetrieveAPIView):
    name = 'category-detail'
    queryset = Category.objects.get_queryset()
    serializer_class = CategorySerializer

class ProductListView(ListAPIView):
    name = 'product-list-view'
    queryset = Product.objects.get_queryset()
    serializer_class = ProductSerializer

class ProductDetail(RetrieveAPIView):
    name = 'product-detail'
    queryset = Product.objects.get_queryset()
    serializer_class = ProductSerializer

class CheckoutListView(ListCreateAPIView):
    name = 'checkout-list-view'
    queryset = Checkout.objects.get_queryset()
    serializer_class = CheckoutSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        current_user = request.user
        checkouts = Checkout.objects.filter(customer=current_user.id)
        serializer_checkout = CheckoutDetailSerializer(checkouts, many=True)
        return Response(serializer_checkout.data, status=status.HTTP_200_OK)

class CheckoutDetail(RetrieveAPIView):
    name = 'checkout-detail'
    queryset = Checkout.objects.get_queryset()
    serializer_class = CheckoutSerializer
    permission_classes = [permissions.IsAuthenticated, IsCheckoutOwner]

class CheckoutItemListView(CreateAPIView):
    name = 'checkouitem-list-view'
    queryset = CheckoutItem.objects.get_queryset()
    serializer_class = CheckoutItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class CheckoutItemDetail(RetrieveAPIView):
    name = 'checkoutitem-detail'
    queryset = CheckoutItem.objects.get_queryset()
    serializer_class = CheckoutItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsCheckoutItemOwner]

class PaymentMethodListView(ListAPIView):
    name = 'payment-method-list-view'
    queryset = PaymentMethod.objects.get_queryset()
    serializer_class = PaymentMethodSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentGatewayListView(ListAPIView):
    name = 'payment-gateway-list-view'
    queryset = PaymentGateway.objects.get_queryset()
    serializer_class = PaymentGatewaySerializer
    permission_classes = [permissions.IsAuthenticated]