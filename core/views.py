from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.generics import *
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
            "authors": reverse(AuthorListView.name, request=request),
            "books": reverse(BookListView.name, request=request),
            "writes": reverse(WriteListView.name, request=request),
            "credits-cards": reverse(CreditCardListView.name, request=request),
            "orders": reverse(OrderListView.name, request=request),
            "items-orders": reverse(ItemOrderListView.name, request=request),
        }
        
        return Response(data, status=status.HTTP_200_OK)


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

class ClientListView(CreateAPIView):
    name = "client-list"
    queryset = Customer.objects.get_queryset()
    serializer_class = ClientSerializer

class ClientDetail(RetrieveUpdateDestroyAPIView):
    name = "client-detail"
    queryset = Customer.objects.get_queryset()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

class AddressListView(CreateAPIView):
    name = 'address-list-view'
    queryset = Address.objects.get_queryset()
    serializer_class = AddressSerializer

class AddressDetail(RetrieveUpdateDestroyAPIView):
    name = 'address-detail'
    queryset = Address.objects.get_queryset()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

class StatusListView(ListAPIView):
    name = 'status-list-view'
    queryset = Status.objects.get_queryset()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated, ReadOnlyPermission]

class StatusDetail(RetrieveUpdateDestroyAPIView):
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

class AuthorListView(ListAPIView):
    name = 'author-list-view'
    queryset = Author.objects.get_queryset()
    serializer_class = AuthorSerializer

class AuthorDetail(RetrieveAPIView):
    name = 'author-detail'
    queryset = Author.objects.get_queryset()
    serializer_class = AuthorSerializer

class WriteListView(ListAPIView):
    name = 'write-list-view'
    queryset = Write.objects.get_queryset()
    serializer_class = WriteSerializer

class WriteDetail(RetrieveAPIView):
    name = 'write-detail'
    queryset = Write.objects.get_queryset()
    serializer_class = WriteSerializer

class BookListView(ListAPIView):
    name = 'book-list-view'
    queryset = Book.objects.get_queryset()
    serializer_class = BookSerializer

class BookDetail(RetrieveAPIView):
    name = 'book-detail'
    queryset = Book.objects.get_queryset()
    serializer_class = BookSerializer

class OrderListView(CreateAPIView):
    name = 'order-list-view'
    queryset = Order.objects.get_queryset()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderDetail(RetrieveAPIView):
    name = 'order-detail'
    queryset = Order.objects.get_queryset()
    serializer_class = OrderDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

class ItemOrderListView(CreateAPIView):
    name = 'item-order-list-view'
    queryset = ItemOrder.objects.get_queryset()
    serializer_class = ItemOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class ItemOrderDetail(RetrieveAPIView):
    name = 'itemorder-detail'
    queryset = ItemOrder.objects.get_queryset()
    serializer_class = ItemOrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

class CreditCardListView(ListAPIView):
    name = 'credit-card-list-view'
    queryset = CreditCard.objects.get_queryset()
    serializer_class = CreditCardSerializer
    permission_classes = [permissions.IsAuthenticated]

class CreditCardDetail(RetrieveAPIView):
    name = 'creditcard-detail'
    queryset = CreditCard.objects.get_queryset()
    serializer_class = CreditCardSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
