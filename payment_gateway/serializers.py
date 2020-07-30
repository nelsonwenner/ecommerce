from payment_gateway.models import PagarmeGateway, PaymentMethod
from rest_polymorphic.serializers import PolymorphicSerializer
from rest_framework import serializers

class PaymentMethodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PaymentMethod
        fields = '__all__' 

class PagarmeGatewaySerializer(serializers.ModelSerializer):

    class Meta:
        model = PagarmeGateway
        fields = ['id', 'encryption_key']

class PaymentGatewaySerializer(PolymorphicSerializer):
    
    model_serializer_mapping = {
        PagarmeGateway: PagarmeGatewaySerializer,
    }