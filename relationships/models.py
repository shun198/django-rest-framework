import uuid
from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    class Meta:
        ordering = ["name"]
        db_table = "Place"

    def __str__(self):
        return self.name


# class Restaurant(models.Model):
#     place = models.OneToOneField(
#         Place,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     serves_hot_dogs = models.BooleanField(default=False)
#     serves_pizza = models.BooleanField(default=False)

#     class Meta:
#         ordering = ["place"]
#         db_table = "Restaurant"

#     def __str__(self):
#         return self.name


# class Reporter(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()

#     def __str__(self):
#         return f"{self.first_name}" + " " + f"{self.last_name}"

#     class Meta:
#         db_table = "Reporter"


# class Publication(models.Model):
#     class Company(models.TextChoices):
#         NIKKEI = "日系"
#         ASAHI = "朝日"

#     title = models.CharField(max_length=30)
#     company = models.CharField(
#         max_length=6, choices=Company.choices, default=Company.ASAHI
#     )
#     # titleの順に並び替える
#     class Meta:
#         db_table = "Publication"
#         ordering = ["title"]

#     def __str__(self):
#         return self.title


# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     pub_date = models.DateField()
#     reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
#     publications = models.ManyToManyField(Publication)

#     def __str__(self):
#         return self.headline

#     # headlineの順に並び替える
#     class Meta:
#         db_table = "Article"
#         ordering = ["headline"]


# class Fruits(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()

#     def __str__(self):
#         return self.name
