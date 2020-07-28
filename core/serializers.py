from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import serializers
from rest_framework import status
from .models import *

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ('customer',)

class CreditCardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CreditCard
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(source='auth_core.user.password', write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'password', 'phone', 'personal_document']

    def create(self, validated_data):
        if Customer.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError("Error: This email already exists")
        user_data = validated_data.pop('auth_core')['user']
        user_data['username'] = validated_data['name']
        user_data['email'] = validated_data['email']
        userClient = UserClient.objects.create_client(**user_data)
        customer = Customer.objects.create(id=userClient.id, user=userClient, **validated_data)
        return customer
    
class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'

class StatusDetailSerializer(serializers.ModelSerializer):
    message = serializers.CharField(style={'input_type': 'charfild'})

    class Meta:
        model = Status
        fields = ['url', 'message']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = '__all__'

class WriteSerializer(serializers.ModelSerializer):

     class Meta:
        model = Write
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    total = serializers.FloatField(style={'input_type': 'interger'})

    class Meta:
        model = Order
        fields = ['id', 'customer', 'status', 'total']

class ItemOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemOrder
        fields = '__all__'
    
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
    
class TokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        
        data['id'] = self.user.id
        data['username'] = self.user.username
        data['email'] = self.user.email
        
        return data