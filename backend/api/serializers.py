from rest_framework import serializers
from .views import Orders

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fileds = '__all__'
        exclude = ['order_date']
        read_only_fields = ['order_id', 'order_date']