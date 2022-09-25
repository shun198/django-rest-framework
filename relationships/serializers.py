from rest_framework import serializers
from .models import Customer,Book

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["name","age"]
        
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["name", "date"]