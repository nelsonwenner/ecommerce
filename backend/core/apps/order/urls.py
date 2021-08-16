from .api import OrderCreateList, OrderDetail
from django.urls import path

app_name = 'order'

urlpatterns = [
  path('checkouts', OrderCreateList.as_view(), name=OrderCreateList.name),
  path('checkouts/<str:pk>', OrderDetail.as_view(), name=OrderDetail.name),
]