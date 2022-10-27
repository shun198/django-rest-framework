import uuid
from django.db import models
from django.core.validators import RegexValidator

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]
        db_table = "Book"

    def __str__(self):
        return self.title

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Author"

    def __str__(self):
        return self.name

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kana = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    post_no = models.CharField(
        max_length=7, validators=[RegexValidator(r"^[0-9]{7}$", "7桁の数字を入力してください。")]
    )
    book = models.ManyToManyField("Book")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name", "age"]
        db_table = "Customer"

    def __str__(self):
        return self.name


# 勤務先
class Workplace(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    kana = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone_no = models.CharField(
        max_length=11,
        validators=[RegexValidator(r"^[0-9]{10,11}$","10か11桁の数字を入力してください。")],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Workplace"

    def __str__(self):
        return self.name

# 銀行口座
class Bank(models.Model):
    # 口座種別のenum
    class AccountType(models.IntegerChoices):
        ORDINARY = 0
        CURRENT = 1
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    holder = models.CharField(max_length=255)
    number = models.CharField(
        max_length=11,
        validators=[RegexValidator(r"^[0-9]{7}$","7桁の数字を入力してください。")],
    )
    type = models.PositiveSmallIntegerField(
        choices=AccountType.choices, default=AccountType.ORDINARY
    )
    bank = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Bank"

    def __str__(self):
        return self.customer.name
