from common.ModelObserver import ModelObserver
from core.models import Checkout

checkout_observer = ModelObserver(sender=Checkout)
checkout_observer.register()