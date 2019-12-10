from rest_framework_simplejwt.views import TokenObtainPairView
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


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


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

    permission_classes = [permissions.IsAuthenticated, ClientPermissions]

    search_fields = ['^email']


class ClientDetail(RetrieveUpdateDestroyAPIView):
    name = "client-detail"
    queryset = Client.objects.get_queryset().order_by('id')
    serializer_class = ClientSerializer

    permission_classes = [permissions.IsAuthenticated, ClientPermissions]


class AddressListView(ListCreateAPIView):
    name = 'address-list-view'
    queryset = Address.objects.get_queryset().order_by('id')
    serializer_class = AddressSerializer

    permission_classes = [permissions.IsAuthenticated, AddressPermissions]


class AddressDetail(RetrieveUpdateDestroyAPIView):
    name = 'address-detail'
    queryset = Address.objects.get_queryset().order_by('id')
    serializer_class = AddressSerializer

    permission_classes = [permissions.IsAuthenticated, AddressPermissions]


class ManagerListView(ListCreateAPIView):
    name = 'manager-list-view'
    queryset = Manager.objects.get_queryset().order_by('id')
    serializer_class = ManagerSerializer

    permission_classes = [permissions.IsAuthenticated, ManagerPermissions]


class ManagerDetail(RetrieveUpdateDestroyAPIView):
    name = 'manager-detail'
    queryset = Manager.objects.get_queryset().order_by('id')
    serializer_class = ManagerSerializer

    permission_classes = [permissions.IsAuthenticated,  ManagerPermissions]


class StatusListView(ListCreateAPIView):
    name = 'status-list-view'
    queryset = Status.objects.get_queryset().order_by('id')
    serializer_class = StatusSerializer

    permission_classes = [permissions.IsAuthenticated, StatusPermissions]


class StatusDetail(RetrieveUpdateDestroyAPIView):
    name = 'status-detail'
    queryset = Status.objects.get_queryset().order_by('id')
    serializer_class = StatusDetailSerializer
    
    permission_classes = [permissions.IsAuthenticated, StatusPermissions]
       
    
class GenreListView(ListCreateAPIView):
    name = 'genre-list-view'
    queryset = Genre.objects.get_queryset().order_by('id')
    serializer_class = GenreSerializer

    permission_classes = [permissions.IsAuthenticated, GenrerPermissions]


class GenreDetail(RetrieveUpdateDestroyAPIView):
    name = 'genre-detail'
    queryset = Genre.objects.get_queryset().order_by('id')
    serializer_class = GenreSerializer

    permission_classes = [permissions.IsAuthenticated, GenrerPermissions]


class AuthorListView(ListCreateAPIView):
    name = 'author-list-view'
    queryset = Author.objects.get_queryset().order_by('id')
    serializer_class = AuthorSerializer

    permission_classes = [permissions.IsAuthenticated, AuthorPermissions]

    search_fields = ['^name', '^email']
    ordering_fields = ['name', 'email']
    filter_fields = ['name', 'email']


class AuthorDetail(RetrieveUpdateDestroyAPIView):
    name = 'author-detail'
    queryset = Author.objects.get_queryset().order_by('id')
    serializer_class = AuthorSerializer

    permission_classes = [permissions.IsAuthenticated, AuthorPermissions]


class WriteListView(ListCreateAPIView):
    name = 'write-list-view'
    queryset = Write.objects.get_queryset().order_by('id')
    serializer_class = WriteSerializer

    permission_classes = [permissions.IsAuthenticated, WritePermissions]


class WriteDetail(RetrieveUpdateDestroyAPIView):
    name = 'write-detail'
    queryset = Write.objects.get_queryset().order_by('id')
    serializer_class = WriteSerializer

    permission_classes = [permissions.IsAuthenticated, WritePermissions]


class BookListView(ListCreateAPIView):
    name = 'book-list-view'
    queryset = Book.objects.get_queryset().order_by('id')
    serializer_class = BookSerializer

    permission_classes = [BookPermissions]

    search_fields = ['^title', '^genre']
    ordering_fields = ['title', 'genre']
    filter_fields = ['title', 'genre']


class BookDetail(RetrieveUpdateDestroyAPIView):
    name = 'book-detail'
    queryset = Book.objects.get_queryset().order_by('id')
    serializer_class = BookSerializer

    permission_classes = [BookPermissions]


class OrderListView(ListCreateAPIView):
    name = 'order-list-view'
    queryset = Order.objects.get_queryset().order_by('id')
    serializer_class = OrderSerializer

    permission_classes = [permissions.IsAuthenticated, OrderPermissions]

    search_fields = ['^client']
    ordering_fields = ['total']


class OrderDetail(RetrieveUpdateDestroyAPIView):
    name = 'order-detail'
    queryset = Order.objects.get_queryset().order_by('id')
    serializer_class = OrderDetailSerializer

    permission_classes = [permissions.IsAuthenticated, OrderPermissions]


class ItemOrderListView(ListCreateAPIView):
    name = 'item-order-list-view'
    queryset = ItemOrder.objects.get_queryset().order_by('id')
    serializer_class = ItemOrderSerializer

    permission_classes = [permissions.IsAuthenticated, ItemOrderPermissions]

    
class ItemOrderDetail(RetrieveUpdateDestroyAPIView):
    name = 'itemorder-detail'
    queryset = ItemOrder.objects.get_queryset().order_by('id')
    serializer_class = ItemOrderSerializer

    permission_classes = [permissions.IsAuthenticated, ItemOrderPermissions]


class CreditCardListView(ListCreateAPIView):
    name = 'credit-card-list-view'
    queryset = CreditCard.objects.get_queryset().order_by('id')
    serializer_class = CreditCardSerializer

    permission_classes = [permissions.IsAuthenticated, CreditCardPermissions]

class CreditCardDetail(RetrieveUpdateDestroyAPIView):
    name = 'creditcard-detail'
    queryset = CreditCard.objects.get_queryset().order_by('id')
    serializer_class = CreditCardSerializer

    permission_classes = [permissions.IsAuthenticated, CreditCardPermissions]