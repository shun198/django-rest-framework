from rest_framework import serializers
from .models import (
    User,
    Book,
    Author,
    Customer,
    Workplace,
    Bank,
)


class UserSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","employee_number",'username', "email", "created_at","updated_at",'password']
        read_only_fields = ["id", "created_at","updated_at",'password']

class LoginSerializer(serializers.ModelSerializer):
    employee_number = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ["employee_number",'email', "username", 'password']


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
        fields = ["id","kana","name","age","post_no","created_at"]
        read_only_fields = ["id","created_at"]

    def to_representation(self, instance):
        # superがあることでretは全てのメソッドとプロパティを引き継ぐ
        # OrderedDictを使える
        ret = super(CustomerSerializer, self).to_representation(instance)
        # 勤務先名
        workplace = instance.workplace
        # 商品番号
        # order = instance.order.latest("created_at")
        # 商品名
        # item = instance.order.latest("created_at").item.latest("created_at")
        ret["workplace_name"] = workplace.name
        # ret["order_no"] = order.order_no
        # ret["item"] = item.name
        return ret


class WorkplaceSerializer(serializers.ModelSerializer):
    # customer = CustomerSerializer(read_only=True)
    class Meta:
        model = Workplace
        fields = ["id","kana","name", "phone_no","created_at"]
        read_only_fields = ["id","created_at"]

    def to_representation(self, instance):
        ret = super(WorkplaceSerializer, self).to_representation(instance)
        customer = instance.customer
        ret["customer_name"] = customer.name
        return ret


class BankSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    class Meta:
        model = Bank
        fields = ["id","customer", "holder","number","type","bank","branch","created_at"]
        read_only_fields = ["id","created_at"]

