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

    permission_classes = [permissions.IsAdminUser]

    search_fields = ['^username']


class UserDetail(RetrieveUpdateDestroyAPIView):
    name = "user-detail"
    queryset = User.objects.get_queryset().order_by('id')
    serializer_class = UserSerializer
    
    permission_classes = [ManagerPermissions]


class ClientListView(ListCreateAPIView):
    name = "client-list"
    queryset = Client.objects.get_queryset().order_by('id')
    serializer_class = ClientSerializer
    
    permission_classes = [ClientPermissions]

    search_fields = ['^email']


class ClientDetail(RetrieveUpdateDestroyAPIView):
    name = "client-detail"
    queryset = Client.objects.get_queryset().order_by('id')
    serializer_class = ClientSerializer

    permission_classes = [ClientPermissions]


class AddressListView(ListCreateAPIView):
    name = 'address-list-view'
    queryset = Address.objects.get_queryset().order_by('id')
    serializer_class = AddressSerializer

    permission_classes = [AddressPermissions]


class AddressDetail(RetrieveUpdateDestroyAPIView):
    name = 'address-detail'
    queryset = Address.objects.get_queryset().order_by('id')
    serializer_class = AddressSerializer

    permission_classes = [AddressPermissions]


class ManagerListView(ListCreateAPIView):
    name = 'manager-list-view'
    queryset = Manager.objects.get_queryset().order_by('id')
    serializer_class = ManagerSerializer

    permission_classes = [ManagerPermissions]


class ManagerDetail(RetrieveUpdateDestroyAPIView):
    name = 'manager-detail'
    queryset = Manager.objects.get_queryset().order_by('id')
    serializer_class = ManagerSerializer

    permission_classes = [ManagerPermissions]


class StatusListView(ListCreateAPIView):
    name = 'status-list-view'
    queryset = Status.objects.get_queryset().order_by('id')
    serializer_class = StatusSerializer

    permission_classes = [StatusPermissions]


class StatusDetail(RetrieveUpdateDestroyAPIView):
    name = 'status-detail'
    queryset = Status.objects.get_queryset().order_by('id')
    serializer_class = StatusDetailSerializer
    
    permission_classes = [StatusPermissions]
       
    
class GenreListView(ListCreateAPIView):
    name = 'genre-list-view'
    queryset = Genre.objects.get_queryset().order_by('id')
    serializer_class = GenreSerializer

    permission_classes = [GenrerPermissions]


class GenreDetail(RetrieveUpdateDestroyAPIView):
    name = 'genre-detail'
    queryset = Genre.objects.get_queryset().order_by('id')
    serializer_class = GenreSerializer

    permission_classes = [GenrerPermissions]


class AuthorListView(ListCreateAPIView):
    name = 'author-list-view'
    queryset = Author.objects.get_queryset().order_by('id')
    serializer_class = AuthorSerializer

    permission_classes = [AuthorPermissions]

    search_fields = ['^name', '^email']
    ordering_fields = ['name', 'email']
    filter_fields = ['name', 'email']


class AuthorDetail(RetrieveUpdateDestroyAPIView):
    name = 'author-detail'
    queryset = Author.objects.get_queryset().order_by('id')
    serializer_class = AuthorSerializer

    permission_classes = [AuthorPermissions]


class WriteListView(ListCreateAPIView):
    name = 'write-list-view'
    queryset = Write.objects.get_queryset().order_by('id')
    serializer_class = WriteSerializer

    permission_classes = [WritePermissions]


class WriteDetail(RetrieveUpdateDestroyAPIView):
    name = 'write-detail'
    queryset = Write.objects.get_queryset().order_by('id')
    serializer_class = WriteSerializer

    permission_classes = [WritePermissions]


class BookListView(ListCreateAPIView):
    name = 'book-list-view'
    queryset = Book.objects.get_queryset().order_by('id')
    serializer_class = BookSerializer
    parser_class = [FileUploadParser]
    
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

    permission_classes = [OrderPermissions]

    search_fields = ['^client']
    ordering_fields = ['total']


class OrderDetail(RetrieveUpdateDestroyAPIView):
    name = 'order-detail'
    queryset = Order.objects.get_queryset().order_by('id')
    serializer_class = OrderDetailSerializer

    permission_classes = [OrderPermissions]


class ItemOrderListView(ListCreateAPIView):
    name = 'item-order-list-view'
    queryset = ItemOrder.objects.get_queryset().order_by('id')
    serializer_class = ItemOrderSerializer

    permission_classes = [ItemOrderPermissions]

    
class ItemOrderDetail(RetrieveUpdateDestroyAPIView):
    name = 'itemorder-detail'
    queryset = ItemOrder.objects.get_queryset().order_by('id')
    serializer_class = ItemOrderSerializer

    permission_classes = [ItemOrderPermissions]


class CreditCardListView(ListCreateAPIView):
    name = 'credit-card-list-view'
    queryset = CreditCard.objects.get_queryset().order_by('id')
    serializer_class = CreditCardSerializer

    permission_classes = [CreditCardPermissions]

class CreditCardDetail(RetrieveUpdateDestroyAPIView):
    name = 'creditcard-detail'
    queryset = CreditCard.objects.get_queryset().order_by('id')
    serializer_class = CreditCardSerializer

    permission_classes = [CreditCardPermissions]