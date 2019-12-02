from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import serializers
from rest_framework import status
from .models import *

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ['url', 'is_superuser', 'username', 'email', 'is_staff']


class AddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Client
        fields = ['url', 'name', 'email', 'phone', 'address']
    
    def create(self, validated_data):
        if Client.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError("Error: This email already exists")

        user_created = User.objects.create_user(
        username=validated_data['name'].split()[0],
        email=validated_data['email'], password='admin@123')
        return Client.objects.create(user=user_created, **validated_data)


class AdministratorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Administrator
        fields = ['url', 'name', 'email', 'cpf', 'salary']

    def create(self, validated_data):
        if Administrator.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError("Error: This email already exists")

        user_created = User.objects.create_user(
        username=validated_data['name'].split()[0],
        email=validated_data['email'], password='admin@123', is_staff=True)
        return Administrator.objects.create(user=user_created, **validated_data)


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ['url', 'name', 'email', 'cpf', 'salary', 'administrator']

    def create(self, validated_data):
        if Employee.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError("Error: This email already exists")

        user_created = User.objects.create_user(
        username=validated_data['name'].split()[0],
        email=validated_data['email'], password='admin@123', is_staff=True)
        return Employee.objects.create(user=user_created, **validated_data)


class StatusSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'


class StatusDetailSerializer(serializers.HyperlinkedModelSerializer):
    message = serializers.CharField(style={'input_type': 'charfild'})

    class Meta:
        model = Status
        fields = ['url', 'message']


class GenreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Author
        fields = '__all__'


class WriteSerializer(serializers.HyperlinkedModelSerializer):

     class Meta:
        model = Write
        fields = '__all__'


class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def update(self, instance, validated_data):
        request = self.context.get('request')
        book_pk = request.parser_context.get('kwargs')['pk']

        book = Book.objects.get(pk=book_pk)

        title_old = book.title
        prince_old = float(book.prince)
        genre_old = book.genre
        title_new = validated_data.get('title')
        prince_new = validated_data.get('prince')
        genre_new = validated_data.get('genre')

        is_administrator = Administrator.objects.filter(email=request.user.email).exists()
        is_employee = Employee.objects.filter(email=request.user.email).exists()

        if request.user.is_superuser or is_administrator:
            instance.title = validated_data.get('title', instance.title)
            instance.stock = validated_data.get('stock', instance.stock)
            instance.prince = validated_data.get('prince', instance.prince)
            instance.genre = validated_data.get('genre', instance.genre)
            instance.save()
            return instance

        if (is_employee and (title_old == title_new) and 
            (prince_old == prince_new) and 
            (genre_old == genre_new)):
            instance.stock = validated_data.get('stock', instance.stock)
            instance.save()
            return instance
            
        raise serializers.ValidationError(
        "Error: Only admin or administrator can perform this operation")


class SaleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sale
        fields = ['url', 'client', 'employee', 'status', 'total', 'date_created']


class SaleDetailSerializer(serializers.HyperlinkedModelSerializer):
    total = serializers.FloatField(style={'input_type': 'interger'})

    class Meta:
        model = Sale
        fields = ['url', 'client', 'employee', 'status', 'total', 'date_created']


class ItemsaleSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Itemsale
        fields = ['url', 'book', 'amount', 'subtotal', 'sale']

    def create(self, validated_data):
        stock = validated_data['book'].stock
        amount = validated_data['amount']
        status = validated_data['sale'].status.message
        
        if amount > stock:
            raise serializers.ValidationError("Error: insufficient stock to perform this operation")
        
        if amount < 0:
            raise serializers.ValidationError("Error: Negative amount detected")
        
        if status == "Compra Finalizada":
            raise serializers.ValidationError("Error: The status of this sale is finalized")

        item_sale = Itemsale.objects.create(**validated_data)

        item_sale.calc_amount
        item_sale.sub_stock
        item_sale.add_total_sale
        return item_sale

    def update(self, instance, validated_data):
        status = validated_data['sale'].status.message
        sale = validated_data['sale']
        book = validated_data['book']

        request = self.context.get('request')
        item_sale_pk = request.parser_context.get('kwargs')['pk']
        
        item_sale = Itemsale.objects.get(pk=item_sale_pk)

        if status == "Compra Finalizada":
            raise serializers.ValidationError("Error: The status of this sale is finalized")
        
        if item_sale.book != book:
            raise serializers.ValidationError("Error: You cannot update with a different book")
        
        if item_sale.sale != sale:
            raise serializers.ValidationError("You cannot update with a different sale")
        
        item_sale.sub_total_sale
        item_sale.add_stock

        instance.amount = validated_data.get('amount', instance.amount)

        instance.calc_amount
        instance.sub_stock
        instance.add_total_sale

        instance.save()

        return instance

       
class AdministratorEmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employees = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="employee-detail")

    class Meta:
        model = Administrator
        fields = ['url', 'name', 'email', 'cpf', 'salary', 'employees']

    