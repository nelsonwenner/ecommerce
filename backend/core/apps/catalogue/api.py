from .serializers import CategorySerializer, ProductSerializer
from rest_framework import permissions
from rest_framework import generics
from .models import Category, Product

class CategoryList(generics.ListAPIView):
  name = 'category-list'
  permission_classes = [permissions.AllowAny]
  queryset = Category.objects.get_queryset().filter(is_active=True).order_by('name') 
  serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveAPIView):
  name = 'category-detail'
  permission_classes = [permissions.AllowAny]
  queryset = Category.objects.get_queryset().filter(is_active=True)
  serializer_class = CategorySerializer

class ProductList(generics.ListAPIView):
  name = 'product-list'
  permission_classes = [permissions.AllowAny]
  queryset = Product.objects.get_queryset().filter(is_active=True).order_by('title') 
  serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
  name = 'product-detail'
  permission_classes = [permissions.AllowAny]
  queryset = Product.objects.get_queryset().filter(is_active=True)
  serializer_class = ProductSerializer