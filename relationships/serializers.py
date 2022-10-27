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
        fields = ["id","title"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id","book","name"]

class CustomerSerializer(serializers.ModelSerializer):
    # book = BookSerializer(read_only=True)
    class Meta:
        model = Customer
        fields = ["id","name"]
        # fields = ["id","book","kana","name","age","post_no"]
    def to_representation(self, instance):
        rep = super(CustomerSerializer, self).to_representation(instance)
        bank = instance.bank.latest("created_at")
        rep["number"] = bank.number
        return rep

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

