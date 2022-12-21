from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import (
    User,
    Book,
    Author,
    Customer,
    Workplace,
    Bank,
)
from django.contrib.auth import (
    authenticate,
)


class AuthTokenSerializer(serializers.Serializer):
    # employee_numberとpassword用のFieldを自作
    employee_number = serializers.CharField()
    password = serializers.CharField(
        # Swaggerを使う際にパスワードを
        # style={"input_type":"password"},
    )

    def validate(self, attrs):
        employee_number = attrs.get("employee_number")
        password = attrs.get("password")
        user = authenticate(
            request=self.context.get("request"),
            username=employee_number,
            password=password,
        )
        if not user:
            raise serializers.ValidationError()

        attrs["user"] = user
        return attrs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "id","employee_number","username","email","role","is_superuser"
        read_only_fields = ["created_at","updated_at","created_by","updated_by"]


class LoginSerializer(serializers.ModelSerializer):
    # uniquekeyを外すためにオーバーライド
    employee_number = serializers.CharField(max_length=8)

    class Meta:
        model = User
        fields = ["employee_number","password"]


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(max_length=64)
    new_password = serializers.CharField(max_length=64)
    confirm_password = serializers.CharField(max_length=64)

    def validate(self, data):
        if data["new_password"] != data["confirm_password"]:
            raise serializers.ValidationError("new password and confirmation password doesn't match")
        validate_password(data["new_password"])
        return data

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

class ResetPasswordSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=64)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("パスワードと確認パスワードは異なります。")
        validate_password(data['password'])
        return data

    class Meta:
        model = User
        fields = ['password', 'confirm_password']

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
        fields = "__all__"
        read_only_fields = ["created_at","created_by","updated_at","updated_by"]

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


class CreateCustomerSerializer(serializers.Serializer):
    file = serializers.FileField()


class DetailCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ["created_at","created_by","updated_at","updated_by"]

    def to_representation(self,instance):
        rep = {
            "workplace" :WorkplaceSerializer(
                instance=instance.workplace, many=True
            ).data,
            "bank" :BankSerializer(
                instance=instance.bank, many=True
            ).data,
        }
        return rep
