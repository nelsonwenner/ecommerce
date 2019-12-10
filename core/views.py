from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.generics import *
from .permissions import *
from .serializers import *

User = get_user_model()

class ApiRoot(GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):

        data = {
            
            "users": reverse(UserListView.name, request=request),
            "clients": reverse(ClientListView.name, request=request),
            "managers": reverse(ManagerListView.name, request=request),
            "address": reverse(AddressListView.name, request=request),
            "status": reverse(StatusListView.name, request=request),
            "genres": reverse(GenreListView.name, request=request),
            "authors": reverse(AuthorListView.name, request=request),
            "books": reverse(BookListView.name, request=request),
            "writes": reverse(WriteListView.name, request=request),
            "credits-cards": reverse(CreditCardListView.name, request=request),
            "orders": reverse(OrderListView.name, request=request),
            "items-orders": reverse(ItemOrderListView.name, request=request),
        }
        
        return Response(data, status=status.HTTP_200_OK)


class UserListView(ListAPIView):
    name = "user-list"
    queryset = User.objects.get_queryset().order_by('id')
    serializer_class = UserSerializer

    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    search_fields = ['^username']


class UserDetail(RetrieveUpdateDestroyAPIView):
    name = "user-detail"
    queryset = User.objects.get_queryset().order_by('id')
    serializer_class = UserSerializer
    
    permission_classes = [permissions.IsAuthenticated, ManagerPermissions]


class ClientListView(ListCreateAPIView):
    name = "client-list"
    queryset = Client.objects.get_queryset().order_by('id')
    serializer_class = ClientSerializer

    #permission_classes = [permissions.IsAuthenticated]

    search_fields = ['^email']


class ClientDetail(RetrieveUpdateDestroyAPIView):
    name = "client-detail"
    queryset = Client.objects.get_queryset().order_by('id')
    serializer_class = ClientSerializer

    #permission_classes = [permissions.IsAuthenticated]


class AddressListView(ListCreateAPIView):
    name = 'address-list-view'
    queryset = Address.objects.get_queryset().order_by('id')
    serializer_class = AddressSerializer

    #permission_classes = [permissions.IsAuthenticated, AddressPermissions]


class AddressDetail(RetrieveUpdateDestroyAPIView):
    name = 'address-detail'
    queryset = Address.objects.get_queryset().order_by('id')
    serializer_class = AddressSerializer

    #permission_classes = [permissions.IsAuthenticated, AddressPermissions]


class ManagerListView(ListCreateAPIView):
    name = 'manager-list-view'
    queryset = Manager.objects.get_queryset().order_by('id')
    serializer_class = ManagerSerializer

    #permission_classes = [permissions.IsAuthenticated]


class ManagerDetail(RetrieveUpdateDestroyAPIView):
    name = 'manager-detail'
    queryset = Manager.objects.get_queryset().order_by('id')
    serializer_class = ManagerSerializer

    #permission_classes = [permissions.IsAuthenticated]


class StatusListView(ListCreateAPIView):
    name = 'status-list-view'
    queryset = Status.objects.get_queryset().order_by('id')
    serializer_class = StatusSerializer

    permission_classes = [permissions.IsAuthenticated, StatusPermission]


class StatusDetail(RetrieveUpdateDestroyAPIView):
    name = 'status-detail'
    queryset = Status.objects.get_queryset().order_by('id')
    serializer_class = StatusDetailSerializer
    
    permission_classes = [permissions.IsAuthenticated, StatusPermission]
       
    
class GenreListView(ListCreateAPIView):
    name = 'genre-list-view'
    queryset = Genre.objects.get_queryset().order_by('id')
    serializer_class = GenreSerializer

    permission_classes = [permissions.IsAuthenticated, GenrerPermission]


class GenreDetail(RetrieveUpdateDestroyAPIView):
    name = 'genre-detail'
    queryset = Genre.objects.get_queryset().order_by('id')
    serializer_class = GenreSerializer

    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, AdministratorPermissions]


class AuthorListView(ListCreateAPIView):
    name = 'author-list-view'
    queryset = Author.objects.get_queryset().order_by('id')
    serializer_class = AuthorSerializer

    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, AdministratorPermissions]

    search_fields = ['^name', '^email']
    ordering_fields = ['name', 'email']
    filter_fields = ['name', 'email']


class AuthorDetail(RetrieveUpdateDestroyAPIView):
    name = 'author-detail'
    queryset = Author.objects.get_queryset().order_by('id')
    serializer_class = AuthorSerializer

    #permission_classes = [permissions.IsAuthenticatedOrReadOnly,  AdministratorPermissions]


class WriteListView(ListCreateAPIView):
    name = 'write-list-view'
    queryset = Write.objects.get_queryset().order_by('id')
    serializer_class = WriteSerializer

    #permission_classes = [permissions.IsAuthenticatedOrReadOnly,  AdministratorPermissions]


class WriteDetail(RetrieveUpdateDestroyAPIView):
    name = 'write-detail'
    queryset = Write.objects.get_queryset().order_by('id')
    serializer_class = WriteSerializer

    #permission_classes = [permissions.IsAuthenticatedOrReadOnly,  AdministratorPermissions]


class BookListView(ListCreateAPIView):
    name = 'book-list-view'
    queryset = Book.objects.get_queryset().order_by('id')
    serializer_class = BookSerializer

    permission_classes = [BookPermission]

    search_fields = ['^title', '^genre']
    ordering_fields = ['title', 'genre']
    filter_fields = ['title', 'genre']


class BookDetail(RetrieveUpdateDestroyAPIView):
    name = 'book-detail'
    queryset = Book.objects.get_queryset().order_by('id')
    serializer_class = BookSerializer

    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, AdministratorPermissions | BookPermission]


class OrderListView(ListCreateAPIView):
    name = 'order-list-view'
    queryset = Order.objects.get_queryset().order_by('id')
    serializer_class = OrderSerializer

    #permission_classes = [permissions.IsAuthenticated, AdministratorPermissions | SalePermissions]

    search_fields = ['^client']
    ordering_fields = ['total']


class OrderDetail(RetrieveUpdateDestroyAPIView):
    name = 'order-detail'
    queryset = Order.objects.get_queryset().order_by('id')
    serializer_class = OrderDetailSerializer

    #permission_classes = [permissions.IsAuthenticated, AdministratorPermissions | SalePermissions]


class ItemOrderListView(ListCreateAPIView):
    name = 'item-order-list-view'
    queryset = ItemOrder.objects.get_queryset().order_by('id')
    serializer_class = ItemOrderSerializer

    #permission_classes = [permissions.IsAuthenticated, AdministratorPermissions | ItemsalePermissions]

    
class ItemOrderDetail(RetrieveUpdateDestroyAPIView):
    name = 'itemorder-detail'
    queryset = ItemOrder.objects.get_queryset().order_by('id')
    serializer_class = ItemOrderSerializer

    #permission_classes = [permissions.IsAuthenticated, AdministratorPermissions | ItemsalePermissions]


class CreditCardListView(ListCreateAPIView):
    name = 'credit-card-list-view'
    queryset = CreditCard.objects.get_queryset().order_by('id')
    serializer_class = CreditCardSerializer


class CreditCardDetail(RetrieveUpdateDestroyAPIView):
    name = 'creditcard-detail'
    queryset = CreditCard.objects.get_queryset().order_by('id')
    serializer_class = CreditCardSerializer