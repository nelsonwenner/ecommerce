from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.generics import *
from .permissions import *
from .serializers import *
from .models import *


class ApiRoot(GenericAPIView):
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

class ClientListView(ListCreateAPIView):
    name = "client-list"
    queryset = Customer.objects.get_queryset()
    serializer_class = ClientSerializer
    
    search_fields = ['^email']

class ClientDetail(RetrieveUpdateDestroyAPIView):
    name = "client-detail"
    queryset = Customer.objects.get_queryset()
    serializer_class = ClientSerializer

class AddressListView(ListCreateAPIView):
    name = 'address-list-view'
    queryset = Address.objects.get_queryset()
    serializer_class = AddressSerializer

class AddressDetail(RetrieveUpdateDestroyAPIView):
    name = 'address-detail'
    queryset = Address.objects.get_queryset()
    serializer_class = AddressSerializer

class StatusListView(ListCreateAPIView):
    name = 'status-list-view'
    queryset = Status.objects.get_queryset()
    serializer_class = StatusSerializer

class StatusDetail(RetrieveUpdateDestroyAPIView):
    name = 'status-detail'
    queryset = Status.objects.get_queryset()
    serializer_class = StatusDetailSerializer
    
class CategoryListView(ListCreateAPIView):
    name = 'category-list-view'
    queryset = Category.objects.get_queryset()
    serializer_class = CategorySerializer

class CategoryDetail(RetrieveUpdateDestroyAPIView):
    name = 'category-detail'
    queryset = Category.objects.get_queryset()
    serializer_class = CategorySerializer

class AuthorListView(ListCreateAPIView):
    name = 'author-list-view'
    queryset = Author.objects.get_queryset()
    serializer_class = AuthorSerializer

    search_fields = ['^name', '^email']
    ordering_fields = ['name', 'email']
    filter_fields = ['name', 'email']

class AuthorDetail(RetrieveUpdateDestroyAPIView):
    name = 'author-detail'
    queryset = Author.objects.get_queryset()
    serializer_class = AuthorSerializer

class WriteListView(ListCreateAPIView):
    name = 'write-list-view'
    queryset = Write.objects.get_queryset()
    serializer_class = WriteSerializer

class WriteDetail(RetrieveUpdateDestroyAPIView):
    name = 'write-detail'
    queryset = Write.objects.get_queryset()
    serializer_class = WriteSerializer

class BookListView(ListCreateAPIView):
    name = 'book-list-view'
    queryset = Book.objects.get_queryset()
    serializer_class = BookSerializer
    parser_class = [FileUploadParser]

    search_fields = ['^title', '^genre']
    ordering_fields = ['title', 'genre']
    filter_fields = ['title', 'genre']

class BookDetail(RetrieveUpdateDestroyAPIView):
    name = 'book-detail'
    queryset = Book.objects.get_queryset()
    serializer_class = BookSerializer

class OrderListView(ListCreateAPIView):
    name = 'order-list-view'
    queryset = Order.objects.get_queryset()
    serializer_class = OrderSerializer

    search_fields = ['^client']
    ordering_fields = ['total']

class OrderDetail(RetrieveUpdateDestroyAPIView):
    name = 'order-detail'
    queryset = Order.objects.get_queryset()
    serializer_class = OrderDetailSerializer

class ItemOrderListView(ListCreateAPIView):
    name = 'item-order-list-view'
    queryset = ItemOrder.objects.get_queryset()
    serializer_class = ItemOrderSerializer

class ItemOrderDetail(RetrieveUpdateDestroyAPIView):
    name = 'itemorder-detail'
    queryset = ItemOrder.objects.get_queryset()
    serializer_class = ItemOrderSerializer

class CreditCardListView(ListCreateAPIView):
    name = 'credit-card-list-view'
    queryset = CreditCard.objects.get_queryset()
    serializer_class = CreditCardSerializer

class CreditCardDetail(RetrieveUpdateDestroyAPIView):
    name = 'creditcard-detail'
    queryset = CreditCard.objects.get_queryset()
    serializer_class = CreditCardSerializer
