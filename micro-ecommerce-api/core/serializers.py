from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from payment_gateway.proccess_payment import proccess_payment_simulation
from payment_gateway.serializers import PaymentMethodSerializer
from django.db import transaction, IntegrityError
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import serializers
from config.celery import _publish
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
    status = serializers.SerializerMethodField(read_only=True)
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

    def get_status(self, obj):
        return model_to_dict(Status.objects.get(id=obj.status.id))

class TokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        
        data['id'] = self.user.id
        data['username'] = self.user.username
        data['email'] = self.user.email
        
        return data