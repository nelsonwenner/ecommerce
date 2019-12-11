from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import serializers
from rest_framework import status
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(source='user.password', write_only=True)
    
    class Meta:
        model = Client
        fields = ['url', 'name', 'email', 'password', 'phone', 'address']
    
    def create(self, validated_data):
        if Client.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError("Error: This email already exists")
        
        user_data = validated_data.pop('user') 
        
        user_data['username'] = validated_data['name'].split()[0]
        user_data['email'] = validated_data['email']

        user_created = User.objects.create_user(**user_data)

        user_created.save()

        return Client.objects.create(user=user_created, **validated_data)


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(source='user.password', write_only=True)
    
    class Meta:
        model = Manager
        fields = ['url', 'name', 'email', 'password', 'cpf', 'salary']

    def create(self, validated_data):
        if Manager.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError("Error: This email already exists")
        
        user_data = validated_data.pop('user') 

        user_data['username'] = validated_data['name'].split()[0]
        user_data['email'] = validated_data['email']

        user_created = User.objects.create_user(**user_data)

        user_created.is_staff = True

        user_created.save()

        return Manager.objects.create(user=user_created, **validated_data)


class AddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


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


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        fields = ['url', 'client', 'manager', 'credit_card', 'status', 'total', 'date_created']


class CreditCardSerializer(serializers.HyperlinkedModelSerializer):
 
    class Meta:
        model = CreditCard
        fields = '__all__'


class OrderDetailSerializer(serializers.HyperlinkedModelSerializer):
    total = serializers.FloatField(style={'input_type': 'interger'})

    class Meta:
        model = Order
        fields = ['url', 'client', 'manager', 'credit_card', 'status', 'total', 'date_created']


class ItemOrderSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ItemOrder
        fields = ['url', 'book', 'amount', 'subtotal', 'order', 'date_created']

    def create(self, validated_data):
        stock = validated_data['book'].stock
        amount = validated_data['amount']
        status = validated_data['order'].status.message
        
        if amount > stock:
            raise serializers.ValidationError("Error: insufficient stock to perform this operation")
        
        if amount < 0:
            raise serializers.ValidationError("Error: Negative amount detected")
        
        if status == "Compra Finalizada":
            raise serializers.ValidationError("Error: The status of this sale is finalized")

        item_order = ItemOrder.objects.create(**validated_data)

        item_order.calc_amount
        item_order.sub_stock
        item_order.add_total_order
        return item_order

    def update(self, instance, validated_data):
        status = validated_data['order'].status.message
        order = validated_data['order']
        book = validated_data['book']

        request = self.context.get('request')
        item_order_pk = request.parser_context.get('kwargs')['pk']
        
        item_order = ItemOrder.objects.get(pk=item_order_pk)

        if status == "Compra Finalizada":
            raise serializers.ValidationError("Error: The status of this sale is finalized")
        
        if item_order.book != book:
            raise serializers.ValidationError("Error: You cannot update with a different book")
        
        if item_order.order != order:
            raise serializers.ValidationError("You cannot update with a different sale")
        
        item_order.sub_total_order
        item_order.add_stock
        
        instance.amount = validated_data.get('amount', instance.amount)

        instance.calc_amount
        instance.sub_stock
        instance.add_total_order

        instance.save()

        return instance


class TokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['token'] = str(refresh.access_token)

        data['user_id'] = self.user.id
        data['username'] = self.user.username
        data['email'] = self.user.email
        
        return data