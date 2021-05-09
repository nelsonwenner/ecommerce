from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from payment_gateway.proccess_payment import proccess_payment_simulation
from payment_gateway.serializers import PaymentMethodSerializer
from rest_framework.validators import UniqueValidator
from django.db import transaction, IntegrityError
from rest_framework.response import Response
from rest_framework import serializers
from config.celery import _publish
from auth_core.models import User
from rest_framework import status
from django.db import transaction
from .models import *

class UserSerializer(serializers.ModelSerializer):  
    class Meta:
        model = User
        fields = ['username', 'email']

class AddressSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ['customer']

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(write_only=True, 
    validators=[UniqueValidator(queryset=User.objects.all())], required=True)
    password = serializers.CharField(min_length=4, write_only=True, required=True)
    address = AddressSerializer(required=True)
    class Meta:
        model = Customer
        fields = [
            'id', 'user', 'username', 
            'email', 'password', 'phone', 
            'personal_document', 'address'
        ]

    def create(self, validated_data):
        user_fields = ['username', 'email', 'password']
        user_data = {f: validated_data.get(f) for f in user_fields}

        customer_fields = ['phone', 'personal_document']
        customer_data = {f: validated_data.get(f) for f in customer_fields}

        address = validated_data.pop('address')

        user = User.objects.create_user(**user_data)
        customer = Customer.objects.create(id=user.id, user=user, **customer_data)
        customer_address = Address.objects.create(**address, customer=customer)
        customer.address = customer_address
        return customer

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def get_image_url(self, obj):
        return obj.image.url

class CheckoutItemSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CheckoutItem
        fields = '__all__'
        read_only_fields = ['checkout']

    def get_title(self, obj):
        return obj.product.title

class CheckoutSerializer(serializers.ModelSerializer):
    items = CheckoutItemSerializer(many=True)
    total = serializers.SerializerMethodField(read_only=True)
    card_hash = serializers.CharField(write_only=True)

    class Meta:
        model = Checkout
        fields = '__all__'

    def get_total(self, obj):
        return obj.total
    
    def create(self, validated_data):
        payment_method = validated_data['payment_method']
        card_hash = validated_data.pop('card_hash')

        try:
            with transaction.atomic():
                items = list(validated_data.pop('items'))
                checkout = Checkout.objects.create(**validated_data)
                checkout_items = []
                for item in items:
                    item['checkout'] = checkout
                    checkout_items.append(CheckoutItem(**item))
                checkout.items = checkout.checkout_items.bulk_create(checkout_items)

                payload = {
                    'customer': ClientSerializer(validated_data['customer']).data['id'],
                    'payment_method': PaymentMethodSerializer(payment_method).data['name'],
                    'checkout_id': CheckoutSerializer(checkout).data['id'],
                    'card_hash': card_hash
                }
                
                _publish(message=payload, routing_key='payment')
                return checkout
        except IntegrityError as e:
            raise serializers.ValidationError("Error: {}".format(e))

class CheckoutDetailSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField(read_only=True)
    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Checkout
        fields = '__all__'

    def get_total(self, obj):
        return obj.total

    def get_items(self, obj):
        return [{
            'title': check_item.product.title,
            'quantity': check_item.quantity,
            'price': check_item.price
        } for check_item in obj.checkout_items.all()]

class TokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        
        data['id'] = self.user.id
        data['username'] = self.user.username
        data['email'] = self.user.email
        
        return data