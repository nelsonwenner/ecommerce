from django.db import transaction, IntegrityError
from .models import Order, OrderItem
from rest_framework import serializers

class OrderItemSerializer(serializers.ModelSerializer):
  title = serializers.SerializerMethodField('get_title')

  class Meta:
    model = OrderItem
    fields = '__all__'
    read_only_fields = ['order', 'price']

  def get_title(self, obj):
    return obj.product.title

class OrderSerializer(serializers.ModelSerializer):
  items = OrderItemSerializer(many=True)
  total = serializers.SerializerMethodField('get_total')
  card_hash = serializers.CharField(write_only=True)

  class Meta:
    model = Order
    fields = '__all__' 
  
  def get_total(self, obj):
    return obj.total

  def create(self, validated_data):
    payment_method = validated_data.get('payment_method')
    card_hash = validated_data.pop('card_hash')

    try:
      with transaction.atomic():
        items = list(validated_data.pop('items'))
        order = Order.objects.create(**validated_data)
        order_items = []
        for item in items:
          product = item.get('product')
          item['price'] = product.regular_price
          item['order'] = order
          order_items.append(OrderItem(**item))
        order.items = order.order_items.bulk_create(order_items)
        return order
    except IntegrityError as e:
      raise serializers.ValidationError('Error: {}'.format(e))

class OrderDetailSerializer(serializers.ModelSerializer):
  items = serializers.SerializerMethodField('get_items')
  total = serializers.SerializerMethodField('get_total')

  class Meta:
    model = Order
    fields = '__all__'

  def get_total(self, obj):
    return obj.total

  def get_items(self, obj):
    data = obj.order_items.all()
    order_serializer = OrderItemSerializer(data, many=True)
    return order_serializer.data