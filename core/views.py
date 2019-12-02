from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
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
            "address": reverse(AddressListView.name, request=request),
            "clients": reverse(ClientListView.name, request=request),
            "administrators": reverse(AdministratorListView.name, request=request),
            "employees": reverse(EmployeeListView.name, request=request),
            "status": reverse(StatusListView.name, request=request),
            "genres": reverse(GenreListView.name, request=request),
            "authors": reverse(AuthorListView.name, request=request),
            "books": reverse(BookListView.name, request=request),
            "writes": reverse(WriteListView.name, request=request),
            "sales": reverse(SaleListView.name, request=request),
            "itemsales": reverse(ItemsaleListView.name, request=request),
            "administrators-employees": reverse(AdministratorEmployeeList.name, request=request),
            "reports-employess": reverse(ReportEmployee.name, request=request),
            "reports-clients": reverse(ReportClient.name, request=request),
        }
        
        return Response(data, status=status.HTTP_200_OK)


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

    permission_classes = [permissions.IsAdminUser]


class ClientListView(ListCreateAPIView):
    name = 'client-list-view'
    queryset = Client.objects.get_queryset().order_by('id')
    serializer_class = ClientSerializer

    permission_classes = [permissions.IsAuthenticated, ClientPermissions]

    search_fields = ['^name', '^email']


class ClientDetail(RetrieveUpdateDestroyAPIView):
    name = 'client-detail'
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


class AdministratorListView(ListCreateAPIView):
    name = 'administrator-list-view'
    queryset = Administrator.objects.get_queryset().order_by('id')
    serializer_class = AdministratorSerializer
    
    permission_classes = [permissions.IsAuthenticated, AdministratorPermissions]


class AdministratorDetail(RetrieveUpdateDestroyAPIView):
    name = 'administrator-detail'
    queryset = Administrator.objects.get_queryset().order_by('id')
    serializer_class = AdministratorSerializer

    permission_classes = [permissions.IsAuthenticated, AdministratorPermissions]


class EmployeeListView(ListCreateAPIView):
    name = 'employee-list-view'
    queryset = Employee.objects.get_queryset().order_by('id')
    serializer_class = EmployeeSerializer

    permission_classes = [permissions.IsAuthenticated, AdministratorPermissions]


class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    name = 'employee-detail'
    queryset = Employee.objects.get_queryset().order_by('id')
    serializer_class = EmployeeSerializer

    permission_classes = [permissions.IsAuthenticated, AdministratorPermissions]


class StatusListView(ListCreateAPIView):
    name = 'status-list-view'
    queryset = Status.objects.get_queryset().order_by('id')
    serializer_class = StatusSerializer

    permission_classes = [permissions.IsAuthenticated, AdministratorPermissions]


class StatusDetail(RetrieveUpdateDestroyAPIView):
    name = 'status-detail'
    queryset = Status.objects.get_queryset().order_by('id')
    serializer_class = StatusDetailSerializer
    
    permission_classes = [permissions.IsAuthenticated,AdministratorPermissions]
       
    
class GenreListView(ListCreateAPIView):
    name = 'genre-list-view'
    queryset = Genre.objects.get_queryset().order_by('id')
    serializer_class = GenreSerializer

    permission_classes = [permissions.IsAuthenticated, AdministratorPermissions]


class GenreDetail(RetrieveUpdateDestroyAPIView):
    name = 'genre-detail'
    queryset = Genre.objects.get_queryset().order_by('id')
    serializer_class = GenreSerializer

    permission_classes = [permissions.IsAuthenticated, AdministratorPermissions]


class AuthorListView(ListCreateAPIView):
    name = 'author-list-view'
    queryset = Author.objects.get_queryset().order_by('id')
    serializer_class = AuthorSerializer

    permission_classes = [permissions.IsAuthenticated, AdministratorPermissions]

    search_fields = ['^name', '^email']
    ordering_fields = ['name', 'email']
    filter_fields = ['name', 'email']


class AuthorDetail(RetrieveUpdateDestroyAPIView):
    name = 'author-detail'
    queryset = Author.objects.get_queryset().order_by('id')
    serializer_class = AuthorSerializer

    permission_classes = [permissions.IsAuthenticated,  AdministratorPermissions]


class WriteListView(ListCreateAPIView):
    name = 'write-list-view'
    queryset = Write.objects.get_queryset().order_by('id')
    serializer_class = WriteSerializer

    permission_classes = [permissions.IsAuthenticated,  AdministratorPermissions]


class WriteDetail(RetrieveUpdateDestroyAPIView):
    name = 'write-detail'
    queryset = Write.objects.get_queryset().order_by('id')
    serializer_class = WriteSerializer

    permission_classes = [permissions.IsAuthenticated,  AdministratorPermissions]


class BookListView(ListCreateAPIView):
    name = 'book-list-view'
    queryset = Book.objects.get_queryset().order_by('id')
    serializer_class = BookSerializer

    permission_classes = [permissions.IsAuthenticated, AdministratorPermissions]

    search_fields = ['^title', '^genre']
    ordering_fields = ['title', 'genre']
    filter_fields = ['title', 'genre']


class BookDetail(RetrieveUpdateDestroyAPIView):
    name = 'book-detail'
    queryset = Book.objects.get_queryset().order_by('id')
    serializer_class = BookSerializer

    permission_classes = [
    permissions.IsAuthenticated, AdministratorPermissions | BookPermission]
    
    def delete(self, request, *args, **kwargs):
        is_employee = Employee.objects.filter(email=request.user.email).exists()
        
        if not is_employee:
            return super().delete(request, *args, **kwargs)
        return Response({
        'error':"Only admin or administrator can perform this operation. "},
        status = status.HTTP_401_UNAUTHORIZED)
    

class SaleListView(ListCreateAPIView):
    name = 'sale-list-view'
    queryset = Sale.objects.get_queryset().order_by('id')
    serializer_class = SaleSerializer

    permission_classes = [permissions.IsAuthenticated, AdministratorPermissions | 
    SalePermissions]

    search_fields = ['^client', '^employee']
    ordering_fields = ['total']


class SaleDetail(RetrieveUpdateDestroyAPIView):
    name = 'sale-detail'
    queryset = Sale.objects.get_queryset().order_by('id')
    serializer_class = SaleDetailSerializer

    permission_classes = [permissions.IsAuthenticated, AdministratorPermissions | 
    SalePermissions]


class ItemsaleListView(ListCreateAPIView):
    name = 'itemsale-list-view'
    queryset = Itemsale.objects.get_queryset().order_by('id')
    serializer_class = ItemsaleSerializer

    permission_classes = [permissions.IsAuthenticated, AdministratorPermissions | 
    ItemsalePermissions]

    
class ItemsaleDetail(RetrieveUpdateDestroyAPIView):
    name = 'itemsale-detail'
    queryset = Itemsale.objects.get_queryset().order_by('id')
    serializer_class = ItemsaleSerializer

    permission_classes = [permissions.IsAuthenticated, AdministratorPermissions | 
    ItemsalePermissions]


class AdministratorEmployeeList(ListAPIView):
    name = 'administrator-employee-list'
    queryset = Administrator.objects.get_queryset().order_by('id')
    serializer_class = AdministratorEmployeeSerializer

    permission_classes = [permissions.IsAdminUser]

    search_fields = ['^name', '^email', '^salary']
    ordering_fields = ['name', 'salary']
    filter_fields = ['name', 'email', 'salary']
   

class AdministratorEmployeeDetail(ListAPIView):
    name = 'administrator-employee-detail'
    queryset = Administrator.objects.get_queryset().order_by('id')
    serializer_class = AdministratorEmployeeSerializer

    permission_classes = [permissions.IsAdminUser]


class ReportEmployee(APIView):
    name = 'report-employee'
    
    permission_classes = [permissions.IsAuthenticated, ReportPermissions]

    def get(self, request, format=None):
        employees = Employee.objects.all()
        
        _list = []
        
        for employee in employees:
            new_list = {}

            new_list['url'] = reverse('employee-detail', args=
            [Employee.objects.get(pk=employee.pk).id],request=request)
            
            new_list['name'] = employee.name 

            sales = Sale.objects.filter(employee=employee)
            
            new_list['money_books_shopping'] = 0.0
            new_list['books_shopping'] = 0
            new_list['count_clients'] = 0
            new_list['clients'] = []
            
            for sale in sales:
                client_list = {} 

                client_list['url'] = reverse('client-detail', args=
                [Client.objects.get(pk=sale.client.pk).id],request=request)

                client_list['name'] = sale.client.name
                client_list['shopping'] = []

                sale_list = {}

                sale_list['url'] = reverse('sale-detail', args=
                [Sale.objects.get(pk=sale.pk).id],request=request)

                sale_list['employee'] = reverse('employee-detail', args=
                [Employee.objects.get(pk=sale.employee.pk).id],request=request)

                sale_list['total'] = sale.total
                sale_list['status'] = sale.status.message
                sale_list['date_created'] = sale.date_created

                sale_list['books'] = []

                items_sales = Itemsale.objects.filter(sale=sale)

                for item_sale in items_sales:
                    book = {}

                    book['url'] = reverse('book-detail', args=
                    [Book.objects.get(pk=item_sale.book.pk).id],request=request)

                    book['title'] = item_sale.book.title
                    book['amount'] = item_sale.amount
                    book['subtotal'] = item_sale.subtotal

                    sale_list['books'].append(book)

                    if sale_list['status'] == "Compra Finalizada":
                        new_list['books_shopping'] += book['amount']
                        new_list['money_books_shopping'] += book['subtotal'] 

                client_list['shopping'].append(sale_list)
                new_list['clients'].append(client_list)
            
            new_list['count_clients'] += len(new_list['clients'])

            _list.append(new_list)

        return Response(_list, status=status.HTTP_200_OK)


class ReportClient(APIView):
    name = 'report-client'
    
    permission_classes = [permissions.IsAuthenticated, ReportPermissions]

    def get(self, request, format=None):
        sales = Sale.objects.all()

        _list = []

        for sale in sales:
            client_list = {}
            
            client_list['url'] = reverse('client-detail', args=
            [Client.objects.get(pk=sale.client.pk).id],request=request)
            
            client_list['name'] = sale.client.name
            client_list['shopping'] = []

            sale_list = {}

            sale_list['url'] = reverse('sale-detail', args=
            [Sale.objects.get(pk=sale.pk).id],request=request)
            
            sale_list['employee'] = reverse('employee-detail', args=
            [Employee.objects.get(pk=sale.employee.pk).id],request=request)
            
            sale_list['total'] = sale.total
            sale_list['status'] = sale.status.message
            sale_list['date_created'] = sale.date_created

            sale_list['books'] = []

            items_sales = Itemsale.objects.filter(sale=sale)

            for item_sale in items_sales:
                book = {}

                book['url'] = reverse('book-detail', args=
                [Book.objects.get(pk=item_sale.book.pk).id],request=request)
                
                book['title'] = item_sale.book.title
                book['amount'] = item_sale.amount
                book['subtotal'] = item_sale.subtotal

                sale_list['books'].append(book)

            client_list['shopping'].append(sale_list)
        
        _list.append(client_list)

        return Response(_list, status=status.HTTP_200_OK)
