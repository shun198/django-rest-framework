from rest_framework import serializers
from .models import (
    Book,
    Author,
    Customer,
    Workplace,
    Bank,
)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id","title","author", "date"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id","name"]

class CustomerSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = Customer
        fields = ["id","kana","name","age","post_no","book"]

class WorkplaceSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    class Meta:
        model = Workplace
        fields = ["id","customer","kana","name", "phone_no"]

class BankSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    class Meta:
        model = Bank
        fields = ["id","customer", "holder","number","type","bank","branch"]

