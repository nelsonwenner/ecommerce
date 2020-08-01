from payment_gateway.models import PaymentMethodConfig, PaymentGateway
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpRequest
from django.contrib import messages

class CheckPaymentMethodConfigMiddleware(MiddlewareMixin):

    def process_request(self, request: HttpRequest):
        if not PaymentMethodConfig.objects.count():
            add_once_message(request, messages.WARNING, 'Configure the payment method setting!')

class CheckPaymentGatewayDefaultMiddleware(MiddlewareMixin):

    def process_request(self, request: HttpRequest):
        if not PaymentGateway.objects.count():
            add_once_message(request, messages.WARNING, 'Define a default payment gateway')

def add_once_message(request, level, msg):
    if msg not in [m.message for m in messages.get_messages(request)]:
        messages.add_message(request,level, msg)