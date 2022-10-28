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
        read_only_fields = ["id","created_at"]

    def to_representation(self, instance):
        rep = super(BookSerializer, self).to_representation(instance)
        author = instance.author.name
        rep["author"] = author
        return rep

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id","book","name"]
        read_only_fields = ["id","created_at"]

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id","name","created_at"]
        read_only_fields = ["id","created_at"]

    def to_representation(self, instance):
        rep = super(CustomerSerializer, self).to_representation(instance)
        book_title = instance.book.latest("created_at").title
        rep["book_title"] = book_title
        return rep

class WorkplaceSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    class Meta:
        model = Workplace
        fields = ["id","customer","kana","name", "phone_no","created_at"]
        read_only_fields = ["id","created_at"]

class BankSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    class Meta:
        model = Bank
        fields = ["id","customer", "holder","number","type","bank","branch","created_at"]
        read_only_fields = ["id","created_at"]

