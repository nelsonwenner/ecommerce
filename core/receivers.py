from common.ModelObserver import ModelObserver
from core.serializers import CheckoutSerializer
from core.models import Checkout

checkout_observer = ModelObserver(sender=Checkout, serializer=CheckoutSerializer)
checkout_observer.register()