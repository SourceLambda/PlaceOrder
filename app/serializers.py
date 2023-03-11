from rest_framework import serializers
from .models import Bill, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    #products = ProductSerializer(many=True)
    class Meta:
        model = Bill
        fields = '__all__'