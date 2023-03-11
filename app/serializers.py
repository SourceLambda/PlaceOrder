from rest_framework import serializers
from .models import Bill, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('_id', 'name', 'description', 'price', 'quantity')

class BillSerializer(serializers.ModelSerializer):
    #products = ProductSerializer(many=True)
    class Meta:
        model = Bill
        fields = ('_idCliente', '_id', 'total', 'date', 'user', 'products')