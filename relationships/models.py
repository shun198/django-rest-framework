import uuid
from django.db import models


class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    class Meta:
        ordering = ["name"]
        db_table = "Place"

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name="タイトル",max_length=20,unique=True)
    price = models.IntegerField(verbose_name="価格",null=True,blank=True)
    created_at = models.DateTimeField(verbose_name="登録日付",auto_now_add=True)
    
    class Meta:
        ordering = ["title"]
        db_table = "Book"

    def __str__(self):
        return self.name
