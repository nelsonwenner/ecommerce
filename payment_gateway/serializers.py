from rest_polymorphic.serializers import PolymorphicSerializer
from payment_gateway.models import PagarmeGateway
from rest_framework import serializers


class PagarmeGatewaySerializer(serializers.ModelSerializer):

    class Meta:
        model = PagarmeGateway
        fields = ['id', 'encryption_key']

class PaymentGatewaySerializer(PolymorphicSerializer):
    
    model_serializer_mapping = {
        PagarmeGateway: PagarmeGatewaySerializer,
    }