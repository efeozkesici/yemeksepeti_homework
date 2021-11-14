from rest_framework import serializers
from .models import Order, User



class OrderSerializer(serializers.ModelSerializer):
   class Meta:
       model = Order
       fields = ['user', 'foodName', 'categoryName', 'restaurant', 'orderStatus']