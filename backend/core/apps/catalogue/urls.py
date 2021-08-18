from .api import CategoryList, CategoryDetail, ProductList, ProductDetail
from django.urls import path

app_name = 'catalogue'

urlpatterns = [
  path('categories', CategoryList.as_view(), name=CategoryList.name),
  path('categories/<str:pk>', CategoryDetail.as_view(), name=CategoryList.name),
  path('products', ProductList.as_view(), name=ProductList.name),
  path('products/<str:pk>', ProductDetail.as_view(), name=ProductDetail.name),
]