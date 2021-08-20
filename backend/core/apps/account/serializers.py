from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Address, Customer

class AddressSerializer(serializers.ModelSerializer):  
  class Meta:
    model = Address
    fields = '__all__'
    read_only_fields = ['customer']

  def create(self, validated_data):
    request = self.context.get('request')
    address = Address.objects.create(customer=request.user, **validated_data)
    return address

class CustomUserSerializer(serializers.ModelSerializer):
  username = serializers.CharField(required=True)
  email = serializers.EmailField(required=True)
  password = serializers.CharField(write_only=True)
  address = serializers.SerializerMethodField('get_address')

  class Meta:
    model = Customer
    fields = ['username', 'email', 'password', 'address']
    extra_kwargs = {'password': {'write_only': True}}

  def get_address(self, obj):
    serializer_address = AddressSerializer(obj.get_address, many=True)
    return serializer_address.data
  
  def create(self, validated_data):
    customer_user = Customer.objects.create_user(**validated_data)
    return customer_user

class TokenObtainPairSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
    data = super().validate(attrs)
    refresh = self.get_token(self.user)

    data['refresh'] = str(refresh)
    data['access'] = str(refresh.access_token)

    data['id'] = self.user.id
    data['username'] = self.user.username
    data['email'] = self.user.email
    
    return data