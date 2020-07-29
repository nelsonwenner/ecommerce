from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import serializers
from rest_framework import status
from django.db import transaction
from .models import *

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

class AddressSerializer(serializers.ModelSerializer):
    customer = serializers.CharField(write_only=True)

    class Meta:
        model = Address
        fields = ['id', 'customer', 'street', 'suite', 'city', 'zipcode']
        read_only_fields = ['customer']
    
    def create(self, validated_data):
        user_id = validated_data.pop('customer')
        customer = Customer.objects.get(id=user_id)
        return Address.objects.create(customer=customer, **validated_data)

class CreditCardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CreditCard
        fields = '__all__'
    
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
    image_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

    def get_image_url(self, obj):
        return obj.image.url

class CheckoutItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckoutItem
        fields = '__all__'
        read_only_fields = ['checkout']

class CheckoutSerializer(serializers.ModelSerializer):
    items = CheckoutItemSerializer(many=True)
    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Checkout
        fields = '__all__'

    def get_total(self, obj):
        return obj.total

    def create(self, validated_data):
        try:
            with transaction.atomic():
                items = list(validated_data.pop('items'))
                checkout = Checkout.objects.create(**validated_data)
                checkout_items = []
                for item in items:
                    item['checkout'] = checkout
                    checkout_items.append(CheckoutItem(**item))
                checkout.items = checkout.checkout_items.bulk_create(checkout_items)
                return checkout
        except Exception as e:
            raise Exception("Error: {}".format(e))

class TokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        
        data['id'] = self.user.id
        data['username'] = self.user.username
        data['email'] = self.user.email
        
        return data